from . import lexer
from .lr import dfm
import unittest
from .lr import lr1
from .syntax_productions import productionList


def analyze(tokens):
    # edges = lr1.construct(productionList, isDebug=True)
    edges = lr1.construct(productionList)

    ast = dfm.run(edges, productionList, tokens)
    print(ast)

    import os
    outputFile = os.path.abspath(os.path.join(__file__, '../../test/syntax_output.txt'))
    with open(outputFile, 'w') as f:
        import json
        json.dump(ast.toDict(), f, indent=4)


class Test(unittest.TestCase):

    def _writeTokens(tokens):
        import os
        outputFile = os.path.abspath( os.path.join(__file__, r"../../test/lex_output.txt") )
        with open(outputFile, 'w') as f:
            for token in tokens:
                f.write(str(token))
                f.write('\n')

    def test(self):
        import os
        testFile = os.path.abspath( os.path.join(__file__, r"../../test/test.shader") )

        with open(testFile) as f:
            buf = f.read()
            tokens = lexer.analyze(buf, isKeepSpace=False, isEnding=True)
            Test._writeTokens(tokens)

        ast = analyze(tokens)
