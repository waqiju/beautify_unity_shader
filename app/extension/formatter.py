import unittest
from ..symbol_type import SymbolType

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

    def placeGapBefore(self):
        if self.count > 0:
            return ''

        self.count += 1
        return '\n'

    def placeGapAfter(self):
        self.count = 1
        return '\n'

    def placeGap(self, increment):
        self.count += increment
        return ''

    def startNewBlock(self):
        if self.count > 0:
            self.count = 0
            return '\n'
        
        self.count = 0
        return ''


def Token2Code(token):
    global tokenIndex
    tokenIndex += 1

    print(str(token), tokenIndex)

    code = token.text
    return code


def String2Code(s):
    global tokenIndex
    tokenIndex += 1

    # print(s, tokenIndex)

    return s;


def _eatSpace(token):
    enterCount = 0
    while token.kind == SymbolType.TokenType.SpaceLike:
        if token.text == '\n':
            enterCount += 1

        token = token.nextToken

    return token, enterCount


def RestoreComment():
    return '' 

    # if tokenIndex < 0: 
    #     return ''

    # lastToken = tokens[tokenIndex]

    # print('')
    # print('last token = %s , ' % lastToken.text, end=' ')
    # code = ''
    # nextToken = lastToken.nextToken
    # TokenType = SymbolType.TokenType
    # while nextToken.kind not in (TokenType.ID, TokenType.String, TokenType.Number):  # tradeoff
    #     print(nextToken.text, end=' ')
    #     if isKeepComment and nextToken.kind == TokenType.Comment:
    #         code += indenter.toCode() + nextToken.text + '\n'
    #     elif isKeepGap and nextToken.text == '\n':
    #         nextToken, enterCount = _eatSpace(nextToken)
    #         if enterCount >= 2:
    #             code += gapManager.placeGap(1)

    #         continue

    #     nextToken = nextToken.nextToken

    # lastToken = None
    # return code



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


def AAI():
    code = gapManager.startNewBlock()
    code += indenter.preAddAdd()
    return code


def SSI():
    code = gapManager.startNewBlock()
    code += indenter.preSubSub()
    return code


def IAA():
    code = gapManager.startNewBlock()
    code += indenter.postAddAdd()
    return code


def ISS():
    code = gapManager.startNewBlock()
    code += indenter.postSubSub()
    return code


def SetTokens(inputTokens):
    global tokens, tokenIndex
    tokens = inputTokens
    tokenIndex = -1

    print('Len = ', len(tokens))


def STR(s):
    return String2Code(s)


# def GB():
#     code = RestoreComment()
#     return code + gapManager.placeGapBefore()


# def GA():
#     return gapManager.placeGapAfter()


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
