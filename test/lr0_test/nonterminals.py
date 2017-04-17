from enum import Enum
from app.syntax_nonterminal import Nonterminal
import unittest

NonterminalType = Enum('NonterminalType', (
    'E',
    'T',
))


class E(Nonterminal):

    kind = NonterminalType.E
    leadingProductions = []


class Ep1(E):

    production = None

    def __init__(self, t, e):
        self.lhs = t
        self.rhs = e

    def toDict(self):
        d = {}
        d['lhs'] = self.lhs.toDict()
        d['rhs'] = self.rhs.toDict()
        return d


class Ep2(E):

    production = None

    def __init__(self, t):
        self.single = t

    def toDict(self):
        d = {}
        d['single'] = self.single.toDict()
        return d


class T(Nonterminal):

    kind = NonterminalType.T
    production = None
    leadingProductions = []

    def __init__(self, id):
        self.id = id

    def toDict(self):
        d = {}
        d['ID'] = str(self.id)
        return d


class Test(unittest.TestCase):

    def DDDtest(self):
        t = T('ID')
        print(t.toDict())

        e1 = Ep2(t)
        print(e1.toDict())

        e2 = Ep1(t, e1)
        print(e2.toDict())

    def DDtest2(self):
        ep2 = Ep2('123')
        print(isinstance(ep2, Nonterminal))
        print(issubclass(Nonterminal, Nonterminal))

        print(isinstance(ep2, type))
        print(isinstance(Ep2, type))


def _init():
    g = globals()
    for k, v in g.items():
        if isinstance(v, type) and issubclass(v, Nonterminal) and v is not Nonterminal:
            Nonterminal.registerClass(k, v)

_init()
