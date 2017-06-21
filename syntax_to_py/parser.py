import unittest
import os
from app import lexer
from app.lex_tokens import TokenType
from . import translator


def prepare():
    # 引入单引号表示的String
    import re
    from app.lex_token import Token
    from app.lex_rules import rules
    rules.insert(2,
                 # 字符串
                 {'pattern': re.compile(r"'[^']*'"),
                  'action': lambda text: Token(TokenType.String, text, text)}
                 )
    # 引入回车(Enter)和空格(Space)，替代原来的SpaceLike
    rules.insert(10,
                 {'pattern': re.compile(r"\n"),
                  'action': lambda text: Token("Enter", text)}
                 )
    rules.insert(10,
                 {'pattern': re.compile(r"[ \t]+"),
                  'action': lambda text: Token(TokenType.SpaceLike, text)}
                 )


def collectNonterminalOfProduction(tokens):
    nonterminals = []
    pos = 1
    for token in tokens:
        if pos == 1 and token.kind == TokenType.ID:
            if token.text not in nonterminals:
                nonterminals.append(token.text)
        elif pos == 2 and token.kind != 'Enter':
            pass
        elif token.kind == TokenType.RightArrow:
            pos = 2
        elif token.kind == 'Enter':
            pos = 1
        else:
            raise Exception('error: token = %s' % token)

    return nonterminals


class Production:

    def __init__(self, left, right, name):
        self.left = left
        self.right = right
        self.name = name
        self.text = left.text + ' -->'
        for token in right:
            self.text += ' ' + token.text


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
                name = 'p' + str(count)
                productionList.append(Production(left, right, name))
                count += 1

            pos = 1
            right = []
        else:
            raise Exception('error: token = %s' % token)

    return productionList


class Test(unittest.TestCase):

    def Dtest(self):
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
        productionNonterminals = collectNonterminalOfProduction(tokens)
        productionList = analyze(tokens)

        translator.writeProductionList(productionList, productionNonterminals, TokenType)
        translator.writeNonterminals(productionList, productionNonterminals)


    def testCg(self):
        prepare()

        # 词法分析
        syntaxFile = os.path.abspath(os.path.join(__file__, '../../test/cg_test/syntax.txt'))
        with open(syntaxFile, encoding='utf-8') as f:
            buf = f.read()
        tokens = lexer.analyze(buf, isKeepSpace=False, isKeepComment=False)

        lexOutputFile = os.path.abspath(os.path.join(__file__, '../output/lex_output.txt'))
        with open(lexOutputFile, 'w', encoding='utf-8') as f:
            for token in tokens:
                f.write(str(token) + '\n')

        # 语法分析
        productionNonterminals = collectNonterminalOfProduction(tokens)
        productionList = analyze(tokens)

        translator.writeProductionList(productionList, productionNonterminals, TokenType)
        translator.mergeProductionListToFile(productionList, productionNonterminals, TokenType, os.path.join(__file__, '../../test/cg_test/productions.py'))
        translator.writeNonterminals(productionList, productionNonterminals)
        translator.mergeNonterminalsToFile(productionList, productionNonterminals, os.path.join(__file__, '../../test/cg_test/nonterminals.py'))


    def DtestShader(self):
        prepare()

        syntaxFile = os.path.abspath(os.path.join(__file__, '../../test/shader_test/syntax.txt'))
        with open(syntaxFile, encoding='utf-8') as f:
            buf = f.read()
        tokens = lexer.analyze(buf, isKeepSpace=False, isKeepComment=False)

        # for debug
        lexOutputFile = os.path.abspath(os.path.join(__file__, '../output/lex_output.txt'))
        with open(lexOutputFile, 'w', encoding='utf-8') as f:
            for token in tokens:
                f.write(str(token) + '\n')

        # 语法分析
        productionNonterminals = collectNonterminalOfProduction(tokens)
        productionList = analyze(tokens)

        translator.writeProductionList(productionList, productionNonterminals, TokenType)
        translator.mergeProductionListToFile(productionList, productionNonterminals, TokenType, os.path.join(__file__, '../../test/shader_test/productions.py'))
        translator.writeNonterminals(productionList, productionNonterminals)
        translator.mergeNonterminalsToFile(productionList, productionNonterminals, os.path.join(__file__, '../../test/shader_test/nonterminals.py'))