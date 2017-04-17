from enum import Enum

TokenType = Enum('TokenType', (
    # 变量
    'ID',
    'String',
    # 标点
    'Times',
    'EQ',
    # Debug
    'NULL',
))

TokenType.getHashValue = lambda obj: str(obj.__hash__())
TokenType.isNonterminal = lambda obj: False
