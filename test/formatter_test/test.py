import unittest
import os
from app import lexer
from app import parser
from app import preprocessor


class Test(unittest.TestCase):

    def test(self):
        with open(os.path.join(__file__, '../formatted.shader')) as f:
            inputText = f.read()
        tokens = lexer.analyze(inputText, isEnding=True)
        tokens = preprocessor.analyze(tokens)
        ast = parser.analyze(tokens)

        with open(os.path.join(__file__, '../output/lex_output.txt'), 'w') as f:
            for token in tokens:
                f.write(str(token) + '\n')

        from app.extension import formatter
        formatter.SetTokens(tokens)
        outFilePath = os.path.abspath(os.path.join(__file__, '../output/output.shader'))
        with open(outFilePath, 'w') as f:
            f.write(ast.toCode())

        formatter.SetTokens(tokens)
        self.maxDiff = None
        self.assertEqual(inputText, ast.toCode())
