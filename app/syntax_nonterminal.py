import unittest
from .lex_token import Token


class NonterminalMeta(type):

    def __new__(cls, name, bases, attrs):
        if name != 'Nonterminal':
            attrs['kind'] = name if Nonterminal is bases[0] else bases[0].__qualname__
            attrs['leadingProductions'] = []
            attrs['production'] = None

        newCls = super().__new__(cls, name, bases, attrs)

        # register
        if name != 'Nonterminal':
            Nonterminal.registerClass(name, newCls)

        return newCls


class Nonterminal(metaclass=NonterminalMeta):

    classDict = {}

    @staticmethod
    def registerClass(name, cls):
        Nonterminal.classDict[name] = cls

    @staticmethod
    def getClass(name):
        cls = Nonterminal.classDict.get(name)
        if cls is not None:
            return cls
        else:
            print('Error, donot have the class, name = %s' % name)
            raise Exception

    def __init__(self):
        pass
        # self.kind = None
        # self.leadingProductions = []

    def toDict(self):
        d = {}
        # d['kind'] = self.kind
        for k in dir(self):
            v = getattr(self, k)
            # token
            if isinstance(v, Token):
                d[k] = str(v)
            # nonterminal
            if isinstance(v, Nonterminal):
                d[k] = v.toDict()
        return d

    def toCode(self):
        code = ''
        for k in dir(self):
            v = getattr(self, k)
            # token
            if isinstance(v, Token):
                code += v.toCode() + ' '
            # nonterminal
            if isinstance(v, Nonterminal):
                code += v.toCode()

        return code


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
        print(e.indenter)

