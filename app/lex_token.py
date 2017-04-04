from enum import Enum

TokenType = Enum('TokenType', (
    ## 变量
    'ID',
    'String',
    'Int',
    'Number', # Int Float
    'Comment',
    'SpaceLike',
    ## 标点
    'Comma',
    'Colon',
    'Semicolon',
    'LParen',
    'RParen',
    'LBrack',
    'RBrack',
    'LBrace',
    'RBrace',
    'Dot',
    'Plus',
    'Minus',
    'Times',
    'Divide',
    'EQ',
    'NEQ',
    'LT',
    'LE',
    'GT',
    'GE',
    'NOT',
    'AND',
    'OR',
    'Assign',
    'Pound',
    'Question',
    ## 语言保留字
    'if',
    'then',
    'else',
    'while',
    'for',
    'break',
    'none',
    ## Debug
    'ReservedWord',
    'LexicalError',
    'Any',
))


class Token:

    def __init__(self, kind, text, value = None):
        self.kind = kind
        self.text = text
        self.value = value

    def __str__(self):
        # return 'kind = %s, text = %s, value = %s' % (self.kind, self.text, self.value)
        if self.value :
            return '%s(%s)' % (self.kind, self.value)
        else :
            return str(self.kind)