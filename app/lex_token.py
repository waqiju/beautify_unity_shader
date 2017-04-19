import unittest


class Token:

    def __init__(self, kind, text=None, value=None):
        self.kind = kind
        self.text = text
        self.value = value

    def __str__(self):
        # return 'kind = %s, text = %s, value = %s' % (self.kind, self.text,
        # self.value)
        if self.value:
            return '%s(%s)' % (self.kind, self.value)
        else:
            return str(self.kind)


class Test(unittest.TestCase):

    def test(self):
        from .lex_tokens import TokenType
        print(Token(TokenType.ID, 'Shader', 'Shader'))
