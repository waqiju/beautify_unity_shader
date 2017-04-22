from app.symbol_type import SymbolType
from app.syntax_nonterminal import Nonterminal
import unittest


class NonterminalType(SymbolType):

    S = 'S'
    E = 'E'
    V = 'V'


class S(Nonterminal):

    kind = NonterminalType.S
    leadingProductions = []


class Sp1(S):

    production = None

    def __init__(self, v, equel, e):
        self.leftValue = v
        self.rightValue = e


class Sp2(S):

    production = None

    def __init__(self, e):
        self.exp = e


class E(Nonterminal):

    kind = NonterminalType.E
    leadingProductions = []
    production = None

    def __init__(self, v):
        self.value = v


class V(Nonterminal):

    kind = NonterminalType.V
    leadingProductions = []


class Vp4(V):

    kind = NonterminalType.V
    production = None

    def __init__(self, id):
        self.ID = id


class Vp5(V):

    kind = NonterminalType.V
    production = None

    def __init__(self, times, e):
        self.exp = e


class Test(unittest.TestCase):

    def test(self):
        s1 = Sp1('v', 'e')
        s2 = Sp2('e')

        e = E('v')

        v1 = Vp4('id')
        v2 = Vp5('e')


def _init():

    g = globals()
    for k, v in g.items():
        if isinstance(v, type) and issubclass(v, Nonterminal) and v is not Nonterminal:
            Nonterminal.registerClass(k, v)

_init()
