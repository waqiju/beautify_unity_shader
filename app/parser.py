from lexer import lexicalAnalyze


def syntacticAnalyze(tokens):
    print(tokens)


if __name__ == '__main__':
    import os
    testFile = os.path.abspath( os.path.join(__file__, r"../../test/test.shader") )

    with open(testFile) as f:
        buf = f.read()
        tokens = lexicalAnalyze(buf)

    ast = syntacticAnalyze(tokens)
    print(ast)

    # outputFile = os.path.abspath( os.path.join(__file__, r"../../test/syntax_output.txt") )
    # with open(outputFile, 'w') as f:
    #     for token in tokens:
    #         f.write(str(token))
    #         f.write('\n')