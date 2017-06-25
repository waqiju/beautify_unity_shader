import os
from .token_name_mapper import TokenNameMapper


# write nonterminls.py
def writeNonterminals(productionList, productionNonterminals):
    with open(os.path.join(__file__, '../output/nonterminals_output.py'), 'w') as f:
        _writeBegin(f)
        _writeNonterminalType(f, productionNonterminals)
        _writeNonterminalClassList(f, productionList, productionNonterminals)
        _writeEnd(f)


def mergeNonterminalsToFile(productionList, productionNonterminals, filePath):
    from io import StringIO
    import re

    # 获得老文件内容
    with open(filePath) as f:
        fileBuf = f.read()

    # 纠正编号
    for production in productionList:
        pattern = r"class %s_(p\d+)\(%s\):\n" % (production.left.text, production.left.text)
        pattern += "    # %s\n" % _replaceRegexKeyWord(production.text)

        match = re.search(pattern, fileBuf)
        if match is None:
            continue

        text = "class %s_%s(%s):\n" % (production.left.text, production.name, production.left.text)
        text += "    # %s\n" % production.text

        fileBuf = fileBuf[:match.start()] + text + fileBuf[match.end():]

    # 完成
    with open(filePath, 'w') as f:
        f.write(fileBuf)


_kws = { '\\', '*', '+', '?', '^', '|', '[', ']', '(', ')', '.' }
def _replaceRegexKeyWord(text):
    newText = ''
    for ch in text:
        if ch in _kws:
            newText += '\\' + ch
        else:
            newText += ch

    return newText


def _writeBegin(file):
    texts = [
        "from app.symbol_type import SymbolType",
        "from app.syntax_nonterminal import Nonterminal",
        "import unittest",
    ]
    texts = map(lambda text: text + '\n', texts)
    file.writelines(texts)


def _writeEnd(file):
    texts = [
        "\n\n"
        "class Test(unittest.TestCase):",
        "\n",
        "    def test(self):",
        "        pass",
    ]
    texts = map(lambda text: text + '\n', texts)
    file.writelines(texts)


def _writeNonterminalType(file, types):
    file.write('\n\n')
    file.write('class NonterminalType(SymbolType):\n')
    file.write('\n')
    for ty in types:
        file.write("    %s = '%s'\n" % (ty, ty))


def _writeNonterminalClassList(file, productionList, types):
    for ty in types:
        _writeBaseClass(file, ty)

    for production in productionList:
        _writeDeriveClass(file, production)


def _writeBaseClass(file, className):
    file.write('\n\n')
    text = "class %s(Nonterminal):\n" % className
    text += "    pass\n"

    file.write(text)


def _writeDeriveClass(file, production):
    file.write('\n\n')
    text = "class %s_%s(%s):\n" % (production.left.text, production.name, production.left.text)
    text += "    # %s\n" % production.text 
    # line 3
    textMapper = TokenNameMapper(production.right)
    text += "    def __init__(self"
    for symbol in production.right:
        if symbol.kind == "ID":
            # symbolStr = symbol.text
            symbolStr = textMapper.get(symbol)
        elif symbol.kind == "String":
            # symbolStr = symbol.text[1:-1]
            symbolStr = TokenNameMapper.avoidPythonKeyword(symbol.text[1:-1])
        else:
            # symbolStr = str(symbol)
            symbolStr = textMapper.getByPunctuator(symbol)
        text += ", %s" % symbolStr
    text += "):\n"
    # line 4 ...
    textMapper.resetUsedCount()
    line4Count = 0
    for symbol in production.right:
        if symbol.kind == "ID":
            # symbolStr = symbol.text
            symbolStr = textMapper.get(symbol)
        else:
            continue

        text += "        self.%s = %s\n" % (symbolStr, symbolStr)
        line4Count += 1

    if line4Count == 0:
        text += "        pass\n"

    file.write(text)


# write productions
def writeProductionList(productionList, productionNonterminals, productionTokens):
    with open(os.path.join(__file__, '../output/productions_output.py'), 'w') as f:
        f.write('productionList = [\n')
        for p in productionList:
            _writeProduction(f, productionNonterminals, productionTokens, p.left, p.right, p.name)
        f.write(']\n')


def _writeProduction(file, NonterminalType, TokenType, left, right, name):
    # line1
    rawProduction = left.text + ' -> '
    for symbol in right:
        rawProduction += ' ' + symbol.text
    text = '    Production("' + rawProduction + '",\n'

    # line2
    text += "               '%s',\n" % name
    # line3
    text += "               N.%s,\n" % left.text
    # line4
    text += "               ("
    for symbol in right:
        # to string
        if symbol.kind == TokenType.String:
            text += symbol.text + ', '
        #
        elif symbol.kind == TokenType.ID:
            # to nonterminal
            if symbol.text in NonterminalType:
                text += 'N.%s, ' % symbol.text
            # to token
            else:
                text += 'T.%s, ' % symbol.text
        # to token
        elif symbol.kind in TokenType:
            text += 'T.%s, ' % symbol.kind
        else:
            print('error: symbol = %s' % symbol)
    text += ")),\n"
    file.write(text)


def mergeProductionListToFile(productionList, productionNonterminals, productionTokens, filePath):
    from io import StringIO
    import re

    memFile = StringIO()
    memFile.write('productionList = [\n')
    for p in productionList:
        _writeProduction(memFile, productionNonterminals, productionTokens, p.left, p.right, p.name)
    memFile.write(']\n')

    with open(filePath) as f:
        fileBuf = f.read()
    match = re.search(r'productionList = \[\n.*\)\),\n\]', fileBuf, re.DOTALL)
    memFile.seek(0)
    newFileBuf = fileBuf[:match.start()] + memFile.read() + fileBuf[match.end():]

    with open(filePath, 'w') as f:
        f.write(newFileBuf)
