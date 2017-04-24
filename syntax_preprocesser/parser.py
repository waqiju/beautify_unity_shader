import unittest
import os
from app import lexer
from app.lex_tokens import TokenType


def prepare():
    # 引入单引号表示的String
    import re
    from app.lex_token import Token
    from app.lex_rules import rules
    rules.insert( 2,
        # 字符串
        {'pattern': re.compile(r"'[^']*'"),
         'action': lambda text: Token(TokenType.String, text, text)}
    )
    # 引入回车(Enter)和空格(Space)，替代原来的SpaceLike
    rules.insert( 10,
        # 字符串
        {'pattern': re.compile(r"\n"),
         'action': lambda text: Token("Enter", text)}
    )
    rules.insert( 10,
        # 字符串
        {'pattern': re.compile(r"[ \t]+"),
         'action': lambda text: Token(TokenType.SpaceLike, text)}
    )


def collectNonterminalTypeOfProduction(tokens):
    types = []
    pos = 1
    for token in tokens:    
        if pos == 1 and token.kind == TokenType.ID:
            if token.text not in types:
                types.append(token.text)
        elif pos == 2 and token.kind != 'Enter':
            pass
        elif token.kind == TokenType.RightArrow:
            pos = 2
        elif token.kind == 'Enter':
            pos = 1
        else:
            print('error: token = %s' % token)
            break

    return types

def writeNonterminalType(types):
    with open(os.path.join(__file__, '../nonterminals_draft.py'), 'w') as f:
        f.write('class NonterminalType(SymbolType):\n')
        f.write('\n')
        for ty in types:
            f.write("    %s = '%s'\n" % (ty, ty))


class Production:

    def __init__(self, left, right, no):
        self.left = left
        self.right = right
        self.no = no


def analyze(tokens):
    # symbol rather than ST inside
    productionList = []

    # like (1)%left% -> (2)%symbol% %ysmbol% Enter
    pos = 1
    left = None
    right = []
    count = 1
    for token in tokens:
        if pos == 1 and token.kind == TokenType.ID:
            left = token
        elif pos == 2 and token.kind != "Enter":
            right.append(token)
        elif token.kind == TokenType.RightArrow:
            pos = 2
        elif token.kind == "Enter":
            if pos == 2:
                productionList.append(Production(left, right, count))
                count += 1

            pos = 1
            right = []
        else:
            print('error: token = %s' % token)
            break

    return productionList


def writeProductionList(productionList, productionNonterminals):
    with open(os.path.join(__file__, '../productions_draft.py'), 'w') as f:
        f.write('productionList = [\n')
        for p in productionList:
            writeProduction(f, productionNonterminals, p.left, p.right, p.no)
        f.write(']\n')


def writeProduction(file, nonterminalType, left, right, no):
    # line1
    rawProduction = left.text + ' -> '
    for symbol in right:
        rawProduction += ' ' + symbol.text
    text = '    Production("' + rawProduction + '",\n'

    # line2
    text += "               'p%s',\n" % no
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
            # to token
            if symbol.text in nonterminalType:
                text += 'N.%s, ' % symbol.text
            # to nonterminal
            else:
                text += 'T.%s, ' % symbol.text
        # to token
        elif symbol.kind in TokenType:
            text += 'T.%s, ' % symbol.kind
        else:
            print('error: symbol = %s' % symbol)
    text += ")),\n"
    file.write(text)


class Test(unittest.TestCase):

    def test(self):
        prepare()

        # 词法分析
        syntaxFile = os.path.abspath(os.path.join(__file__, '../../doc/syntax.txt'))
        with open(syntaxFile, encoding='utf-8') as f:
            buf = f.read()
        tokens = lexer.analyze(buf, isKeepSpace=False, isKeepComment=False)

        lexOutputFile = os.path.abspath(os.path.join(__file__, '../lex_output.txt'))
        with open(lexOutputFile, 'w', encoding='utf-8') as f:
            for token in tokens:
                f.write(str(token) + '\n')

        # 语法分析
        productionNonterminals = collectNonterminalTypeOfProduction(tokens)
        writeNonterminalType(productionNonterminals)
        
        productionList = analyze(tokens)
        writeProductionList(productionList, productionNonterminals)
