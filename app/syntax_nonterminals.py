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
    prop_init = 'prop_init'
    subshr = 'subshr'
    subshr_body = 'subshr_body'
    tags = 'tags'
    tags_body = 'tags_body'
    tag_smt = 'tag_smt'
    cmds = 'cmds'
    cmd_stm = 'cmd_stm'
    ids = 'ids'
    passes = 'passes'
    shr_pass = 'shr_pass'
    pass_body = 'pass_body'
    cg_prog = 'cg_prog'
    cg_stm = 'cg_stm'
    preprocessing_stm = 'preprocessing_stm'
    pp_if_stm = 'pp_if_stm'
    pp_cmd = 'pp_cmd'


class prog(Nonterminal):

    def __init__(self, shader, name, lbrace, shader_body, rbrace):
        self.name = name
        self.shader_body = shader_body


class shader_body(Nonterminal):

    def __init__(self, props, subshr):
        self.props = props
        self.subshr = subshr


class props(Nonterminal):
    pass


class propsp3(props):
    def __init__(self, properties, lbrace, props_body, rbrace):
        self.props_body = props_body


class props_body(Nonterminal):
    pass


class props_bodyp5(props_body):

    def __init__(self, prop_stm, props_body):
        self.prop_stm = prop_stm
        self.props_body = props_body


class prop_stm(Nonterminal):

    def __init__(self, varName, lparen, inspectName, comma, varType, rparen, assgin, prop_init):
        self.varName = varName
        self.inspectName = inspectName
        self.varType = varType
        self.prop_init = prop_init


class prop_init(Nonterminal):
    pass


class prop_initp8(prop_init):

    def __init__(self, number):
        self.number = number


class prop_initp9(prop_init):
    def __init__(self, color, lbrace, rbrace):
        self.color = color


class prop_initp10(prop_init):
    def __init__(self, *args):
        self.numbers = []
        for arg in args:
            if arg.kind == TokenType.Number:
                self.numbers.append(arg.value)


class subshr(Nonterminal):
    def __init__(self, subshader, lbrace, subshr_body, rbrace):
        self.subshr_body = subshr_body


class subshr_body(Nonterminal):
    def __init__(self, tags, cmds, passes):
        self.tags = tags
        self.cmds = cmds
        self.passes = passes


class tags(Nonterminal):

    def __init__(self, tags, lbrace, tags_body, rbrace):
        self.tags_body = tags_body


class tags_body(Nonterminal):

    pass


class tags_bodyp14(tags_body):

    def __init__(self, tag_smt, tags_body):
        self.tag_smt = tag_smt
        self.tags_body = tags_body


class tag_smt(Nonterminal):

    def __init__(self, key, assign, value):
        self.key = key
        self.value = value


class cmds(Nonterminal):
    pass


class cmdsp17(cmds):
    def __init__(self, cmd_stm, cmds):
        self.cmd_stm = cmd_stm
        self.cmds = cmds


class cmdsp18(cmds):
    pass


class cmd_stm(Nonterminal):
    def __init__(self, cmd_name, cmd_values):
        self.cmd_name = cmd_name
        self.cmd_values = cmd_values


class ids(Nonterminal):
    pass


class idsp20(ids):
    def __init__(self, id, ids):
        self.id = id
        self.ids = ids

class passes(Nonterminal):
    pass


class passesp22(passes):
    def __init__(self, shr_pass, passes):
        self.shr_pass = shr_pass
        self.passes = passes


class shr_pass(Nonterminal):
    def __init__(self, Pass, lbrace, pass_body, rbrace):
        self.pass_body = pass_body


class pass_body(Nonterminal):
    def __init__(self, CGPROGRAM, cg_prog, ENDCG):
        self.cg_prog = cg_prog


class Test(unittest.TestCase):

    def test(self):
        pass
