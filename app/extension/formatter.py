import unittest
from ..symbol_type import SymbolType
from ..lex_token import Token
from ..syntax_nonterminal import Nonterminal
from ..syntax_productions import productionList

# todo, 把formatter改写为一个类


# Config
isKeepComment = True
isKeepGap = True


class Indenter:

    IndentWidth = 4

    def __init__(self):
        self.nowLevel = 0

    def toCode(self):
        return ' ' * self.IndentWidth * self.nowLevel

    def postAddAdd(self):
        code = self.toCode()
        self.nowLevel += 1
        return code

    def preAddAdd(self):
        self.nowLevel += 1
        return self.toCode()

    def postSubSub(self):
        code = self.toCode()
        self.nowLevel -= 1
        return code

    def preSubSub(self):
        if self.nowLevel > 0:
            self.nowLevel -= 1
        return self.toCode()


class GapManager:

    def __init__(self):
        self.count = 0
        self.commentListAhead = []
        self.commentListBehind = []

    def insertCommentAhead(self, comment):
        self.commentListAhead.append(comment)

    def insertCommentBehind(self, comment):
        self.commentListBehind.append(comment)

    def placeGap(self, increment):
        self.count += increment
        return ''

    def startNewBlock(self):
        code = ''
        for comment in self.commentListAhead:
            code += comment + '\n'
        if self.count > 0:
            code += '\n'
        for comment in self.commentListBehind:
            code += comment + '\n'

        self.count = 0
        self.commentListAhead = []
        self.commentListBehind = []

        return code


def Token2Code(token):
    global tokenIndex
    tokenIndex += 1

    code = token.text
    return code


def String2Code(s):
    global tokenIndex
    tokenIndex += 1

    return s;


def _eatSpace(token):
    enterCount = 0
    while token.kind == SymbolType.TokenType.SpaceLike:
        if token.text == '\n':
            enterCount += 1

        token = token.nextToken

    return token, enterCount


def RestoreComment():
    TokenType = SymbolType.TokenType

    if tokenIndex < 0: 
        return ''

    commentList = []
    lastToken = tokens[tokenIndex]
    stopToken = tokens[tokenIndex + 1] if tokenIndex + 1 < len(tokens) else None
    nextToken = lastToken.nextToken
    while nextToken is not stopToken:
        if isKeepComment and nextToken.kind == TokenType.Comment:
            commentWithIndent = indenter.toCode() + nextToken.text
            commentList.append(commentWithIndent)
        elif isKeepGap and nextToken.text == '\n':
            nextToken, enterCount = _eatSpace(nextToken)
            if enterCount >= 2:
                gapManager.placeGap(1)

            continue

        nextToken = nextToken.nextToken

    lastToken = None

    code = ''
    if len(commentList) == 0:
        pass
    elif len(commentList) == 1:
        gapManager.insertCommentBehind(commentList[0])
    else:
        gapManager.insertCommentAhead(commentList[0])
        for i in range(1, len(commentList)):
            gapManager.insertCommentBehind(commentList[i])

    return code



indenter = Indenter()
gapManager = GapManager()
tokens = []
tokenIndex = -1


# shortcut for frequently call
def I():
    # 正确的排版，新的一行总会是G()或者I()开头
    code = RestoreComment()
    code += gapManager.startNewBlock()
    code += indenter.toCode()
    return code


def IAA():
    code = RestoreComment()
    code += gapManager.startNewBlock()
    code += indenter.postAddAdd()
    return code


def SSI():
    code = RestoreComment()
    code += gapManager.startNewBlock()
    code += indenter.preSubSub()
    return code


def SetTokens(inputTokens):
    global tokens, tokenIndex
    tokens = inputTokens
    tokenIndex = -1

    # do injection
    from . import syntax_tree_to_code
    syntax_tree_to_code.doInjection(productionList, Token, Nonterminal)



def STR(s):
    return String2Code(s)


def G(increment = 1):
    return gapManager.placeGap(increment)


def E():
    return '\n'


class Test(unittest.TestCase):

    def DtestIndenter(self):
        I = Indenter()
        print(I.toCode())

    def test(self):
        pass
