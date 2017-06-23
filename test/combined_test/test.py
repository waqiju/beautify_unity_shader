import os
import json
import re
from app.lr import lr1
from app.lr import inspector
from .productions import productionList
from app import lexer
from app import preprocessor
from app.lr import dfm
from . import known_conflicts

def construct():

    edges, stateList, preStateIndex = lr1.construct(productionList, isDebug=True)

    with open(os.path.join(__file__, '../3_state_list.txt'), 'w') as f:
        inspector.printStateList(stateList, preStateIndex, f)
    with open(os.path.join(__file__, '../3_dfm_edges.txt'), 'w') as f:
        inspector.printEdges(edges, f)
    with open(os.path.join(__file__, '../2_edges.json'), 'w') as f:
        json.dump(edges, f, indent=4)


def verify():

    def json2Edges(d):
        edges = {}
        for key in d:
            edges[int(key)] = d[key]
        return edges

    with open(os.path.join(__file__, '../2_edges.json')) as f:
        edges = json2Edges(json.load(f))

    # 消除已知的冲突
    edges = known_conflicts.applyTo(edges)
    with open(os.path.join(__file__, '../2_edges_conflict_free.json'), 'w') as f:
        json.dump(edges, f, indent=4)


    # 用shader进行验证
    with open(os.path.join(__file__, '../test.shader')) as f:
        inputText = f.read()
    tokens = lexer.analyze(inputText, isEnding=True)
    tokens = preprocessor.analyze(tokens)
    with open(os.path.join(__file__, '../1_lex_output.txt'), 'w') as f:
        for token in tokens:
            f.write(str(token))
            f.write('\n')

    ast = dfm.run(edges, productionList, tokens, isDebug=False)

    outputFile = os.path.abspath(os.path.join(__file__, '../2_syntax_output.txt'))
    with open(outputFile, 'w') as f:
        json.dump(ast.toDict(), f, indent=4)

    outputFile = os.path.abspath(os.path.join(__file__, '../3_formatted_code.shader'))
    with open(outputFile, 'w') as f:
        f.write(ast.toCode())


def verifyAll():

    def json2Edges(d):
        edges = {}
        for key in d:
            edges[int(key)] = d[key]
        return edges

    with open(os.path.join(__file__, '../2_edges.json')) as f:
        edges = json2Edges(json.load(f))

    # 消除已知的冲突
    edges = known_conflicts.applyTo(edges)
    with open(os.path.join(__file__, '../2_edges_conflict_free.json'), 'w') as f:
        json.dump(edges, f, indent=4)


    # 用shader进行验证
    shaderFiles = []
    for path, dirs, files in os.walk(r'D:\Protable_Program\Sublime Text Build 3126 x64\Data\Packages\UnityShader'):
        for file in files:
            if os.path.splitext(file)[1] == '.shader':
                filePath = os.path.join(path, file)
                shaderFiles.append(filePath)

    count = 0
    for filePath in shaderFiles:
        if os.path.split(filePath)[1] == 'Internal-DeferredShading.shader':
            continue

        with open(filePath) as f:
            inputText = f.read()
            count += 1

            try:
                tokens = lexer.analyze(inputText, isEnding=True)
                tokens = preprocessor.analyze(tokens)
                ast = dfm.run(edges, productionList, tokens, isDebug=False)

                print(count, filePath, 'ok')
            except Exception as e:
                print(filePath, 'failed')
                with open(os.path.join(__file__, '../test.shader'), 'w') as testShaderFile:
                    testShaderFile.write(inputText)

                raise e



def profileConstruct():
    import cProfile
    cProfile.run('construct()', 'profile')
    import pstats
    p = pstats.Stats('profile')
    p.sort_stats('cumtime').print_stats(20)


if __name__ == '__main__':
    import sys
    if (len(sys.argv) > 1 and sys.argv[1] == 'construct'):
        # profileConstruct()
        construct()
        exit()

    # verify()
    verifyAll()
