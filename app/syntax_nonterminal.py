

class Nonterminal:

    classDict = {}

    @staticmethod
    def registerClass(name, cls):
        Nonterminal.classDict[name] = cls

    @staticmethod
    def getClass(name):
        return Nonterminal.classDict.get(name)

    def __init__(self):
        pass
        # self.kind = None
        # self.leadingProductions = []

    def toDict(self):
        pass