from .nonterminals import NonterminalType
from app.syntax_nonterminal import Nonterminal
from app.syntax_production import Production
from .tokens import TokenType
import unittest


r'''
0 S -> E $
1 E -> T + E
2 E -> T
3 T -> ID
'''

productionList = [
    Production('E -> T + E',
               'p1',
               NonterminalType.E,
               (NonterminalType.T, TokenType.Plus, NonterminalType.E)),
    Production('E -> T',
               'p2',
               NonterminalType.E,
               (NonterminalType.T, )),
    Production('T -> ID',
               'p3',
               NonterminalType.T,
               (TokenType.ID, )),
]


class Test(unittest.TestCase):

    def test(self):
        self.assertTrue(len(productionList) == 3)
        for production in productionList:
            print(production)


def _init():
    for p in productionList:
        name1 = p.left.name
        name2 = name1 + p.name

        cls1 = Nonterminal.getClass(name1)
        cls1.leadingProductions.append(p)
        cls2 = Nonterminal.getClass(name2) or Nonterminal.getClass(name1)
        cls2.production = p

_init()