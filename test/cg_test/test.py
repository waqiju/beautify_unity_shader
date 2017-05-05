from app.lr import lr1

if __name__ == '__main__':
    import os
    from .productions import productionList
    from app import lexer
    from app.lr import dfm
    import json

    stateListFile = open(os.path.join(__file__, '../0_state_list.txt'), 'w')
    edgesFile = open(os.path.join(__file__, '../0_dfm_edges.txt'), 'w')

    edges = lr1.construct(productionList, stateListOutputFile=stateListFile, edgesOutputFile=edgesFile)

    stateListFile.close()
    edgesFile.close()

    exit()


    # 用shader进行验证
    with open(os.path.join(__file__, '../test.shader')) as f:
        inputText = f.read()
    tokens = lexer.analyze(inputText, isKeepSpace=False, isKeepComment=False, isEnding=True)

    ast = dfm.run(edges, productionList, tokens)

    outputFile = os.path.abspath(os.path.join(__file__, '../2_syntax_output.txt'))
    with open(outputFile, 'w') as f:
        import json
        json.dump(ast.toDict(), f, indent=4)
