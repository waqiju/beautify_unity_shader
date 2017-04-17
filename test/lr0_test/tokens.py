from enum import Enum

TokenType = Enum('TokenType', (
    # 变量
    'ID',
    'String',
    # 标点
    'Plus',
))