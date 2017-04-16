from .syntax_nonterminal import Nonterminal
from enum import Enum
import unittest

NonterminalType = Enum('NonterminalType', (
    'Prog',
    'ShaderBody',
))


class Prog(Nonterminal):

    def __init__(self, pos, name, shader_body):
        self.kind = NonterminalType.Prog
        self.pos = pos
        self.name = name  # String
        self.shader_body = shader_body  # nonterminal
        Nonterminal.registerClass(self.kind, Prog)

    def toDict(self):
        d = {}
        d['kind'] = self.kind.name
        d['pos'] = self.pos
        d['name'] = self.name
        d['shader_body'] = self.shader_body.toDict()
        return d


class ShaderBody(Nonterminal):

    def __init__(self, pos, raw):
        self.kind = NonterminalType.ShaderBody
        self.pos = pos
        self.raw = raw

    def toDict(self):
        d = {}
        d['kind'] = self.kind.name
        d['pos'] = self.pos
        d['raw'] = self.raw
        return d


class Test(unittest.TestCase):

    def test(self):
        prog = Prog(1, 'a_shader', 'body')

        cls = Nonterminal.getClass(NonterminalType.Prog)
        self.assertTrue(cls == Prog)