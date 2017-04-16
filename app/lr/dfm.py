

def lrAnalyze(dfmEdges, tokenList):
    pass


if __name__ == "__main__":

    def import_from_file(relativePath):
        import os
        currentModulePath = os.path.abspath(os.path.dirname(__file__))
        targetModulePath = os.path.abspath(
            os.path.join(currentModulePath, relativePath))
        targetModuleFolder, targetModule = os.path.split(targetModulePath)
        print(targetModuleFolder, targetModule)

        import sys
        import importlib
        sys.path.append(targetModuleFolder)
        return importlib.import_module(targetModule)

    productionList = import_from_file('../syntax_productions').SyntaxProductions
    import lr1
    dfmEdges = lr1.construct(productionList)
