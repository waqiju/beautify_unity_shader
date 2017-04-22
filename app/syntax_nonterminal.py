import unittest
from .lex_token import Token

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
        d = {}
        d['kind'] = self.kind
        for k in dir(self):
            v = getattr(self, k)
            # token
            if isinstance(v, Token):
                d[k] = str(v)
            # nonterminal
            if isinstance(v, Nonterminal):
                d[k] = v.toDict()
        return d


class Test(unittest.TestCase):

    class E(Nonterminal):

        kind = 'E'
        leadingProductions = []
        production = None

        def __init__(self, v):
            self.value = v

    def test(self):
        e = Test.E('x')
        print(e.toDict())

