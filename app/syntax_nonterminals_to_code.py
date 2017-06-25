import unittest
from .syntax_nonterminal import Nonterminal


# prog --> 'Shader' String { shader_body_elms }
def _p1(self):
    print("hello")


class Test(unittest.TestCase):

    def test(self):
        toCodep1('hi')