import unittest
from app.lex_token import Token
from app.lex_tokens import TokenType


class TokenNameMapper:

    def __init__(self, tokenList):
        self.totalCount = {}
        self.usedCount = {}
        for token in tokenList:
            name = token.text
            if name not in self.totalCount:
                self.totalCount[name] = 1
                self.usedCount[name] = 0
            else:
                self.totalCount[name] += 1

    def resetUsedCount(self):
        for key in self.usedCount:
            self.usedCount[key] = 0

    def get(self, token):
        name = token.text
        if self.totalCount[name] == 1:
            return name
        else:
            self.usedCount[name] += 1
            if self.usedCount[name] > self.totalCount[name]:
                raise Exception('should not go here!')
            return name + str(self.usedCount[name])

    def getByPunctuator(self, token):
        name = token.text
        if self.totalCount[name] == 1:
            return str(token)
        else:
            self.usedCount[name] += 1
            if self.usedCount[name] > self.totalCount[name]:
                raise Exception('should not go here!')
            return str(token) + str(self.usedCount[name])

    @staticmethod
    def avoidPythonKeyword(name):
        if name in ['if', 'elif', 'else', 'for', 'while', 'continue', 'break', 'return', '2D', '3D']:
            return '_' + name

        return name



class Test(unittest.TestCase):

    def test(self):
        tokens = [Token(TokenType.ID, 'a'), Token(TokenType.ID, 'a'), Token(TokenType.ID, 'a'), Token(TokenType.ID, 'b'), Token(TokenType.Plus, '+'), Token(TokenType.Plus, '+')]
        a = Token(TokenType.ID, 'a')
        b = Token(TokenType.ID, 'b')
        plus = Token(TokenType.Plus, '+')

        m = TokenNameMapper(tokens)

        print(m.get(a))
        print(m.get(a))
        print(m.get(a))
        print(m.get(b))
        print(m.get(plus))
        print(m.getByPunctuator(plus))
