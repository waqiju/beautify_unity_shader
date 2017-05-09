import unittest
from .lex_tokens import TokenType

# Config
isKeepComment = True
isKeepGap = True


class Indenter:

    IndentWidth = 4

    def __init__(self):
        self.nowLevel = 1

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

    def startNewBlock(self):
        self.count = 0


def token2Code(token):
    code = token.text

    global lastToken
    lastToken = token

    # code += RestoreComment()

    return code


def _isContainGap(text):
    enterCount = 0
    for ch in text:
        if ch == '\n':
            enterCount += 1
    return enterCount >= 2


def RestoreComment():
    global lastToken
    if lastToken is None:
        return ''

    code = ''
    nextToken = lastToken.nextToken
    while nextToken.kind not in (TokenType.ID, TokenType.String, TokenType.Number, TokenType.ReservedWord):
        if isKeepComment and nextToken.kind == TokenType.Comment:
            code += indenter.toCode() + nextToken.text + '\n'
        elif isKeepGap and _isContainGap(nextToken.text):
            code += gapManager.placeGapBefore()

        nextToken = nextToken.nextToken

    lastToken = None
    return code



indenter = Indenter()
gapManager = GapManager()
lastToken = None


# shortcut for frequently call
def I():
    # 正确的排版，新的一行总会是GB()或者I()开头
    code = RestoreComment()
    gapManager.startNewBlock()
    return code + indenter.toCode()


def AAI():
    gapManager.startNewBlock()
    return indenter.preAddAdd()


def SSI():
    gapManager.startNewBlock()
    return indenter.preSubSub()


def IAA():
    gapManager.startNewBlock()
    return indenter.postAddAdd()


def ISS():
    gapManager.startNewBlock()
    return indenter.postSubSub()


def GB():
    code = RestoreComment()
    return code + gapManager.placeGapBefore()


def GA():
    return gapManager.placeGapAfter()


class Test(unittest.TestCase):

    def DtestIndenter(self):
        I = Indenter()
        print(I.toCode())

    def test(self):
        pass
