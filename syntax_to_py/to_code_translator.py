import os
from .token_name_mapper import TokenNameMapper


# write nonterminls.py
def writeToCode(productionList, productionNonterminals):
    with open(os.path.join(__file__, '../output/syntax_tree_to_code_output.py'), 'w') as f:
        _writeBegin(f)
        _writeNonterminalClassList(f, productionList, productionNonterminals)
        _writeEnd(f)


def mergeToCodeToFile(productionList, productionNonterminals, filePath):
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
        "import unittest",
        "from ..syntax_nonterminal import Nonterminal",
        "from ..syntax_productions import productionList",
    ]
    texts = map(lambda text: text + '\n', texts)
    file.writelines(texts)


def _writeEnd(file):
    texts = [
        "",
        "",
        "def _init():",
        "    for p in productionList:",
        "        if p is None :  # production[0]可能是None",
        "            continue",
        "        levelTwoName = p.left + '_' + p.name",
        "        levelTwoCls = Nonterminal.getClass(levelTwoName)",
        "        localMethond = globals()['_' + p.name]",
        "        setattr(levelTwoCls, 'toCode', localMethond)",
        "",
        "",
        "_init()",
    ]
    texts = map(lambda text: text + '\n', texts)
    file.writelines(texts)


def _writeNonterminalClassList(file, productionList, types):
    for production in productionList:
        _writeDeriveClass(file, production)


def _writeDeriveClass(file, production):
    file.write('\n\n')

    # line 1
    text = "# %s\n" % production.text
    # line 2
    text += "def _%s(self):\n" % production.name
    # line 3
    nameMapper = TokenNameMapper(production.right)
    codeText = ''
    for symbol in production.right:
        codeText +=  (' + ' if codeText != '' else '') 
        if symbol.kind == "ID":
            codeText += 'self.' + nameMapper.get(symbol) + ".toCode()"
        elif symbol.kind == "String":
            codeText += symbol.text
        else :
            codeText += "'%s'" % symbol.text
    if codeText == '':
        text += "    return ''" + '\n'
    else:
        text += "    return " + codeText + '\n'

    file.write(text)
