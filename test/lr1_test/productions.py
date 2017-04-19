from app.syntax_nonterminal import Nonterminal
from app.syntax_production import Production
from .tokens import TokenType
from .nonterminals import NonterminalType
import unittest


r'''
0 S' -> S $
1 S -> V = E
2 S -> E
3 E -> V
4 V -> ID
5 V -> * E
'''

productionList = [
    Production('S -> V = E',
               'p1',
               NonterminalType.S,
               (NonterminalType.V, TokenType.EQ, NonterminalType.E)),
    Production('S -> E',
               'p2',
               NonterminalType.S,
               (NonterminalType.E, )),
    Production('E -> V',
               'p3',
               NonterminalType.E,
               (NonterminalType.V, )),
    Production('V -> ID',
               'p4',
               NonterminalType.V,
               (TokenType.ID, )),
    Production('V -> * E',
               'p5',
               NonterminalType.V,
               (TokenType.Times, NonterminalType.E, )),
]


class Test(unittest.TestCase):

  def test(self):
    self.assertTrue(len(productionList) == 5)
    for production in productionList:
      print(production)


def _init():
  for p in productionList:
    name1 = p.left
    name2 = name1 + p.name

    cls1 = Nonterminal.getClass(name1)
    cls1.leadingProductions.append(p)
    cls2 = Nonterminal.getClass(name2) or Nonterminal.getClass(name1)
    cls2.production = p

_init()
