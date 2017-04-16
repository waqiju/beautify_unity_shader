from syntax_symbol import SymbolType
from lex_token import Token, TokenType




# todo 优化下规则书写，syntax_reader，syntax.txt -> SyntaxProductions
# syntax = (
#     (Prog,
#         (Token(TokenType.ID, 'Shader', 'Shader'), TokenType.String, TokenType.LBrace, ShaderBody)),
# )


SyntaxProductions = (
    (SymbolType.Prog, (
        Token(TokenType.ID, 'Shader', 'Shader'), TokenType.String, TokenType.LBrace, SymbolType.ShaderBody, TokenType.RBrace)),
)
