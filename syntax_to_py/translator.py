import os


def writeNonterminalFileBegin():
    texts = [
        "from app.symbol_type import SymbolType",
        "from app.syntax_nonterminal import Nonterminal",
        "from .lex_tokens import TokenType",
        "import unittest",
    ]
    texts = map(lambda text: text + '\n', texts)

    with open(os.path.join(__file__, '../nonterminals_draft.py'), 'w') as f:
        f.writelines(texts)


def writeNonterminalFileEnd():
    texts = [
        "\n\n"
        "class Test(unittest.TestCase):",
        "\n",
        "    def test(self):",
        "        pass",
    ]
    texts = map(lambda text: text + '\n', texts)

    with open(os.path.join(__file__, '../nonterminals_draft.py'), 'a') as f:
        f.writelines(texts)


def writeNonterminalType(types):
    with open(os.path.join(__file__, '../nonterminals_draft.py'), 'a') as f:
        f.write('\n\n')
        f.write('class NonterminalType(SymbolType):\n')
        f.write('\n')
        for ty in types:
            f.write("    %s = '%s'\n" % (ty, ty))


def writeNonterminalClassList(types, productionList):
    with open(os.path.join(__file__, '../nonterminals_draft.py'), 'a') as f:
        for ty in types:
            _writeBaseClass(f, ty)

        for production in productionList:
            _writeDeriveClass(f, production)


def _writeBaseClass(file, className):
    file.write('\n\n')
    text = "class %s(Nonterminal):\n" % className
    text += "    pass\n"

    file.write(text)


def _writeDeriveClass(file, production):
    file.write('\n\n')
    text = "class %s%s(%s):\n" % (production.left.text, production.name, production.left.text)
    text += "\n"
    # line 3
    text += "    def __init__(self"
    for symbol in production.right:
        if symbol.kind == "ID":
            symbolStr = symbol.text
        elif symbol.kind == "String":
            symbolStr = symbol.text[1:-1]
        else:
            symbolStr = str(symbol)
        text += ", %s" % symbolStr
    text += "):\n"
    # line 4 ...
    line4Count = 0
    for symbol in production.right:
        if symbol.kind == "ID":
            symbolStr = symbol.text
        else:
            continue

        text += "        self.%s = %s\n" % (symbolStr, symbolStr)
        line4Count += 1

    if line4Count == 0:
        text += "        pass\n"

    file.write(text)


def writeProductionList(productionList, productionNonterminals, productionTokens):
    with open(os.path.join(__file__, '../productions_draft.py'), 'w') as f:
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
