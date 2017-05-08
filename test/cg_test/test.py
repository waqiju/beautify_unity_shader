from app.lr import lr1


def construct():
    import os
    from .productions import productionList
    from app import lexer
    from app.lr import dfm
    import json

    stateListFile = open(os.path.join(__file__, '../0_state_list.txt'), 'w')
    edgesFile = open(os.path.join(__file__, '../0_dfm_edges.txt'), 'w')

    edges = lr1.construct(productionList, stateListOutputFile=stateListFile, edgesOutputFile=edgesFile, isDebug=True)

    stateListFile.close()
    edgesFile.close()

    with open(os.path.join(__file__, '../2_edges.json'), 'w') as f:
        json.dump(edges, f, indent=4)


def verify():
    import os
    from .productions import productionList
    from app import lexer
    from app.lr import dfm
    import json

    def json2Edges(d):
        edges = {}
        for key in d:
            edges[int(key)] = d[key]
        return edges

    with open(os.path.join(__file__, '../2_edges.json')) as f:
        edges = json2Edges(json.load(f))


    # exit()

    # 用shader进行验证
    with open(os.path.join(__file__, '../test.shader')) as f:
        inputText = f.read()
    tokens = lexer.analyze(inputText, isKeepSpace=False, isKeepComment=False, isEnding=True)
    with open(os.path.join(__file__, '../1_lex_output.txt'), 'w') as f:
        for token in tokens:
            f.write(str(token))
            f.write('\n')

    ast = dfm.run(edges, productionList, tokens)

    outputFile = os.path.abspath(os.path.join(__file__, '../2_syntax_output.txt'))
    with open(outputFile, 'w') as f:
        import json
        json.dump(ast.toDict(), f, indent=4)


def profileConstruct():
    import cProfile
    cProfile.run('construct()', 'profile')


if __name__ == '__main__':
    construct()
    # verify()
