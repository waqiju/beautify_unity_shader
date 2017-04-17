from enum import Enum
from app.syntax_nonterminal import Nonterminal
import unittest

NonterminalType = Enum('NonterminalType', (
    'S',
    'E',
    'V',
))

NonterminalType.getHashValue = lambda obj: str(obj.__hash__())
NonterminalType.isNonterminal = lambda obj: True

class S(Nonterminal):

    kind = NonterminalType.S
    leadingProductions = []


class Sp1(Nonterminal):

    production = None

    def __init__(self, v, e):
        self.leftValue = v
        self.rightValue = e


class Sp2(Nonterminal):

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


def Vp4(Nonterminal):

    production = None

    def __init__(self, id):
        self.ID = id


def Vp5(Nonterminal):

    production = None

    def __init__(self, e):
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
