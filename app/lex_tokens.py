import unittest
from .symbol_type import SymbolType

class TokenType(SymbolType):

    # 变量
    ID = "ID"
    String = "String"
    Int = "Int"
    Number = "Number"  # Int Float
    Comment = "Comment"
    SpaceLike = "SpaceLike"
    # 双符号标点
    RightArrow = "RightArrow"
    LeftShiftAssign = "LeftShiftAssign"
    RightShiftAssign = "RightShiftAssign"
    ModAssign = "ModAssign"
    AndAssign = "AndAssign"
    XorAssign = "XorAssign"
    OrAssign = "OrAssign"
    LeftShift = "LeftShift"
    RightShift = "RightShift"
    # 单符号标点
    Comma = "Comma"
    Colon = "Colon"
    Semicolon = "Semicolon"
    LParen = "LParen"
    RParen = "RParen"
    LBrack = "LBrack"
    RBrack = "RBrack"
    LBrace = "LBrace"
    RBrace = "RBrace"
    Dot = "Dot"
    Plus = "Plus"
    Minus = "Minus"
    Times = "Times"
    Divide = "Divide"
    Tilde = "Tilde"
    Percent = "Percent"
    Ampersand = "Ampersand"
    Caret = "Caret"
    VerticalBar = "VerticalBar"

    EQ = "EQ"
    NEQ = "NEQ"
    LT = "LT"
    LE = "LE"
    GT = "GT"
    GE = "GE"
    NOT = "NOT"
    AND = "AND"
    OR = "OR"
    Assign = "Assign"
    Pound = "Pound"
    Question = "Question"
    # 语言保留字
    if_ = "if"
    then_ = "then"
    else_ = "else"
    while_ = "while"
    for_ = "for"
    break_ = "break"
    none_ = "none"
    # Debug
    ReservedWord = "ReservedWord"
    LexicalError = "LexicalError"
    # NULL = 'NULL'
    Any = "Any"

    def isNonterminal(self):
        return False


class Test(unittest.TestCase):

    def test(self):
        print('hi')
        print(TokenType.if_)
