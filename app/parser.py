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

    # import json

    # shaderBody = ShaderBody(10, 'This is Shader Body')
    # prog = Prog(1, 'Shader', shaderBody)
    # # print(prog.toDict())

    # t = json.dumps(prog, default=lambda obj: obj.toDict(), indent=4, sort_keys=True)
    # print(t)

    # # text = json.dumps(prog, default=lambda obj: obj.__dict__)
    # # print(text)