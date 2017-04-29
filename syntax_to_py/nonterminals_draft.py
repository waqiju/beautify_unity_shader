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
    pass


class shader_body(Nonterminal):
    pass


class props(Nonterminal):
    pass


class props_body(Nonterminal):
    pass


class prop_stm(Nonterminal):
    pass


class prop_init(Nonterminal):
    pass


class subshr(Nonterminal):
    pass


class subshr_body(Nonterminal):
    pass


class tags(Nonterminal):
    pass


class tags_body(Nonterminal):
    pass


class tag_smt(Nonterminal):
    pass


class cmds(Nonterminal):
    pass


class cmd_stm(Nonterminal):
    pass


class ids(Nonterminal):
    pass


class passes(Nonterminal):
    pass


class shr_pass(Nonterminal):
    pass


class pass_body(Nonterminal):
    pass


class cg_prog(Nonterminal):
    pass


class cg_stm(Nonterminal):
    pass


class preprocessing_stm(Nonterminal):
    pass


class pp_if_stm(Nonterminal):
    pass


class pp_cmd(Nonterminal):
    pass


class progp1(prog):

    def __init__(self, Shader, name, LBrace, shader_body, RBrace):
        self.name = name
        self.shader_body = shader_body


class shader_bodyp2(shader_body):

    def __init__(self, props, subshr):
        self.props = props
        self.subshr = subshr


class propsp3(props):

    def __init__(self, Properties, LBrace, props_body, RBrace):
        self.props_body = props_body


class propsp4(props):

    def __init__(self):
        pass


class props_bodyp5(props_body):

    def __init__(self, prop_stm, props_body):
        self.prop_stm = prop_stm
        self.props_body = props_body


class props_bodyp6(props_body):

    def __init__(self):
        pass


class prop_stmp7(prop_stm):

    def __init__(self, varName, LParen, inspectName, Comma, varType, RParen, Assign, prop_init):
        self.varName = varName
        self.inspectName = inspectName
        self.varType = varType
        self.prop_init = prop_init


class prop_initp8(prop_init):

    def __init__(self, number):
        self.number = number


class prop_initp9(prop_init):

    def __init__(self, color, LBrace, RBrace):
        self.color = color


class prop_initp10(prop_init):

    def __init__(self, *args):
        self.numbers = []
        for arg in args:
            if arg.kind == TokenType.Number:
                self.numbers.append(arg.value)


class subshrp11(subshr):

    def __init__(self, SubShader, LBrace, subshr_body, RBrace):
        self.subshr_body = subshr_body


class subshr_bodyp12(subshr_body):

    def __init__(self, tags, cmds, passes):
        self.tags = tags
        self.cmds = cmds
        self.passes = passes


class tagsp13(tags):

    def __init__(self, Tags, LBrace, tags_body, RBrace):
        self.tags_body = tags_body


class tags_bodyp14(tags_body):

    def __init__(self, tag_smt, tags_body):
        self.tag_smt = tag_smt
        self.tags_body = tags_body


class tags_bodyp15(tags_body):

    def __init__(self):
        pass


class tag_smtp16(tag_smt):

    def __init__(self, key, Assign, value):
        self.key = key
        self.value = value


class cmdsp17(cmds):

    def __init__(self, cmd_stm, cmds):
        self.cmd_stm = cmd_stm
        self.cmds = cmds


class cmdsp18(cmds):

    def __init__(self):
        pass


class cmd_stmp19(cmd_stm):

    def __init__(self, cmd_name, cmd_values):
        self.cmd_name = cmd_name
        self.cmd_values = cmd_values


class idsp20(ids):

    def __init__(self, ID, ids):
        self.ID = ID
        self.ids = ids


class idsp21(ids):

    def __init__(self):
        pass


class passesp22(passes):

    def __init__(self, shr_pass, passes):
        self.shr_pass = shr_pass
        self.passes = passes


class passesp23(passes):

    def __init__(self):
        pass


class shr_passp24(shr_pass):

    def __init__(self, Pass, LBrace, pass_body, RBrace):
        self.pass_body = pass_body


class pass_bodyp25(pass_body):

    def __init__(self, CGPROGRAM, cg_prog, ENDCG):
        self.cg_prog = cg_prog


class cg_progp26(cg_prog):

    def __init__(self, cg_stm):
        self.cg_stm = cg_stm


class cg_stmp27(cg_stm):

    def __init__(self, preprocessing_stm):
        self.preprocessing_stm = preprocessing_stm


class preprocessing_stmp28(preprocessing_stm):

    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class preprocessing_stmp29(preprocessing_stm):

    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd


class pp_if_stmp30(pp_if_stm):

    def __init__(self, Pound, _if, ID):
        self.ID = ID


class pp_if_stmp31(pp_if_stm):

    def __init__(self, Pound, ifdef, ID):
        self.ID = ID


class pp_if_stmp32(pp_if_stm):

    def __init__(self, Pound, idndef, ID):
        self.ID = ID


class pp_if_stmp33(pp_if_stm):

    def __init__(self, Pound, _elif, ID):
        self.ID = ID


class pp_if_stmp34(pp_if_stm):

    def __init__(self, Pound, _else):
        pass


class pp_if_stmp35(pp_if_stm):

    def __init__(self, Pound, endif):
        pass


class pp_cmdp36(pp_cmd):

    def __init__(self, Pound, include, String):
        self.String = String


class Test(unittest.TestCase):


    def test(self):
        pass
