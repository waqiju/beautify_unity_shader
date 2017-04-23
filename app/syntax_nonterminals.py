from app.symbol_type import SymbolType
from app.syntax_nonterminal import Nonterminal
from .lex_tokens import TokenType
import unittest


class NonterminalType(SymbolType):

    prog = 'prog'
    shader_body = 'shader_body'
    props = 'props'
    props_body = 'props_body'
    prop_stm = 'prop_stm'
    prop_body = 'prop_body'
    prop_stm = 'prop_stm'
    prop_init = 'prop_init'
    subshr = 'subshr'
    subshr_body = 'subshr_body'
    tags = 'tags'
    tags_body = 'tags_body'
    tag_smt = 'tag_smt'


class prog(Nonterminal):

    def __init__(self, shader, name, lbrace, shader_body, rbrace):
        self.name = name
        self.shader_body = shader_body


class shader_body(Nonterminal):

    def __init__(self, props, subshr):
        self.props = props
        self.subshr = subshr


class props(Nonterminal):

    def __init__(self, properties, lbrace, props_body, rbrace):
        self.props_body = props_body


class props_body(Nonterminal):

    pass


class props_bodyp4(props_body):

    def __init__(self, prop_stm, props_body):
        self.prop_stm = prop_stm
        self.props_body = props_body


class props_bodyp5(props_body):

    def __init__(self):
        pass


class prop_stm(Nonterminal):

    def __init__(self, varName, lparen, inspectName, comma, varType, rparen, assgin, prop_init):
        self.varName = varName
        self.inspectName = inspectName
        self.varType = varType
        self.prop_init = prop_init


class prop_init(Nonterminal):

    pass


class prop_initp7(prop_init):

    def __init__(self, number):
        self.number = number


class prop_initp8(prop_init):

    def __init__(self, color, lbrace, rbrace):
        self.color = color


class prop_initp9(prop_init):

    def __init__(self, *args):
        self.numbers = []
        for arg in args:
            if arg.kind == TokenType.Number:
                self.numbers.append(arg.value)


class subshr(Nonterminal):

    def __init__(self, subshader, lbrace, subshr_body, rbrace):
        self.subshr_body = subshr_body


class subshr_body(Nonterminal):

    def __init__(self, tags):
        self.tags = tags


class tags(Nonterminal):

    def __init__(self, tags, lbrace, tags_body, rbrace):
        self.tags_body = tags_body


class tags_body(Nonterminal):

    pass


class tags_bodyp13(tags_body):

    def __init__(self, tag_smt, tags_body):
        self.tag_smt = tag_smt
        self.tags_body = tags_body


class tags_bodyp14(tags_body):

    pass


class tag_smt(Nonterminal):

    def __init__(self, key, assign, value):
        self.key = key
        self.value = value


class Test(unittest.TestCase):

    def test(self):
        pass
