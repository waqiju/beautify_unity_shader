from syntax_symbol import SymbolType
from syntax_token import Token, TokenType


class Production:

    def __init__(self, left, right):
        self.left = left
        self.right = right


# todo 优化下规则书写，syntax_reader，syntax.txt -> SyntaxProductions
# syntax = (
#     (Prog,
#         (Token(TokenType.ID, 'Shader', 'Shader'), TokenType.String, TokenType.LBrace, ShaderBody)),
# )


SyntaxProductions = (
    (SymbolType.Prog, (
        Token(TokenType.ID, 'Shader', 'Shader'), TokenType.String, TokenType.LBrace, SymbolType.ShaderBody, TokenType.RBrace)),
)
