import unittest
from app.symbol_type import SymbolType


class TokenType(SymbolType):

    # 变量
    ID = 'ID'
    String = 'String'
    # 标点
    Times = 'Times'
    EQ = 'EQ'
    # Debug
    NULL = 'NULL'


class Test(unittest.TestCase):

    def test(self):
        for ty in TokenType:
            print(ty)
