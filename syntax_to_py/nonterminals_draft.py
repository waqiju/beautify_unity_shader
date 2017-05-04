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
    cg_stms = 'cg_stms'
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


class cg_stms(Nonterminal):
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
    # prog --> 'Shader' String { shader_body }
    def __init__(self, Shader, String, LBrace, shader_body, RBrace):
        self.String = String
        self.shader_body = shader_body


class shader_bodyp2(shader_body):
    # shader_body --> props subshr
    def __init__(self, props, subshr):
        self.props = props
        self.subshr = subshr


class propsp3(props):
    # props --> 'Properties' { props_body }
    def __init__(self, Properties, LBrace, props_body, RBrace):
        self.props_body = props_body


class propsp4(props):
    # props -->
    def __init__(self):
        pass


class props_bodyp5(props_body):
    # props_body --> prop_stm props_body
    def __init__(self, prop_stm, props_body):
        self.prop_stm = prop_stm
        self.props_body = props_body


class props_bodyp6(props_body):
    # props_body -->
    def __init__(self):
        pass


class prop_stmp7(prop_stm):
    # prop_stm --> ID ( String , ReservedWord ) = prop_init
    def __init__(self, ID, LParen, String, Comma, ReservedWord, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.ReservedWord = ReservedWord
        self.prop_init = prop_init


class prop_initp8(prop_init):
    # prop_init --> Number
    def __init__(self, Number):
        self.Number = Number


class prop_initp9(prop_init):
    # prop_init --> String { }
    def __init__(self, String, LBrace, RBrace):
        self.String = String


class prop_initp10(prop_init):
    # prop_init --> ( Number , Number , Number , Number )
    def __init__(self, LParen, Number, Comma, Number, Comma, Number, Comma, Number, RParen):
        self.Number = Number
        self.Number = Number
        self.Number = Number
        self.Number = Number


class subshrp11(subshr):
    # subshr --> 'SubShader' { subshr_body }
    def __init__(self, SubShader, LBrace, subshr_body, RBrace):
        self.subshr_body = subshr_body


class subshr_bodyp12(subshr_body):
    # subshr_body --> tags cmds passes
    def __init__(self, tags, cmds, passes):
        self.tags = tags
        self.cmds = cmds
        self.passes = passes


class tagsp13(tags):
    # tags --> 'Tags' { tags_body }
    def __init__(self, Tags, LBrace, tags_body, RBrace):
        self.tags_body = tags_body


class tags_bodyp14(tags_body):
    # tags_body --> tag_smt tags_body
    def __init__(self, tag_smt, tags_body):
        self.tag_smt = tag_smt
        self.tags_body = tags_body


class tags_bodyp15(tags_body):
    # tags_body -->
    def __init__(self):
        pass


class tag_smtp16(tag_smt):
    # tag_smt --> String = String
    def __init__(self, String, Assign, String):
        self.String = String
        self.String = String


class cmdsp17(cmds):
    # cmds --> cmd_stm cmds
    def __init__(self, cmd_stm, cmds):
        self.cmd_stm = cmd_stm
        self.cmds = cmds


class cmdsp18(cmds):
    # cmds -->
    def __init__(self):
        pass


class cmd_stmp19(cmd_stm):
    # cmd_stm --> ReservedWord ids
    def __init__(self, ReservedWord, ids):
        self.ReservedWord = ReservedWord
        self.ids = ids


class idsp20(ids):
    # ids --> ID ids
    def __init__(self, ID, ids):
        self.ID = ID
        self.ids = ids


class idsp21(ids):
    # ids -->
    def __init__(self):
        pass


class passesp22(passes):
    # passes --> shr_pass passes
    def __init__(self, shr_pass, passes):
        self.shr_pass = shr_pass
        self.passes = passes


class passesp23(passes):
    # passes -->
    def __init__(self):
        pass


class shr_passp24(shr_pass):
    # shr_pass --> 'Pass' { pass_body }
    def __init__(self, Pass, LBrace, pass_body, RBrace):
        self.pass_body = pass_body


class pass_bodyp25(pass_body):
    # pass_body --> 'CGPROGRAM' cg_prog 'ENDCG'
    def __init__(self, CGPROGRAM, cg_prog, ENDCG):
        self.cg_prog = cg_prog


class cg_progp26(cg_prog):
    # cg_prog --> cg_stms
    def __init__(self, cg_stms):
        self.cg_stms = cg_stms


class cg_stmsp27(cg_stms):
    # cg_stms --> cg_stm cg_stms
    def __init__(self, cg_stm, cg_stms):
        self.cg_stm = cg_stm
        self.cg_stms = cg_stms


class cg_stmsp28(cg_stms):
    # cg_stms -->
    def __init__(self):
        pass


class cg_stmp29(cg_stm):
    # cg_stm --> preprocessing_stm
    def __init__(self, preprocessing_stm):
        self.preprocessing_stm = preprocessing_stm


class preprocessing_stmp30(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class preprocessing_stmp31(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd


class pp_if_stmp32(pp_if_stm):
    # pp_if_stm --> # 'if' ID
    def __init__(self, Pound, if, ID):
        self.ID = ID


class pp_if_stmp33(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID


class pp_if_stmp34(pp_if_stm):
    # pp_if_stm --> # 'idndef' ID
    def __init__(self, Pound, idndef, ID):
        self.ID = ID


class pp_if_stmp35(pp_if_stm):
    # pp_if_stm --> # 'elif' ID
    def __init__(self, Pound, elif, ID):
        self.ID = ID


class pp_if_stmp36(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, else):
        pass


class pp_if_stmp37(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass


class pp_cmdp38(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String


class pp_cmdp39(pp_cmd):
    # pp_cmd --> # 'pragma' ids
    def __init__(self, Pound, pragma, ids):
        self.ids = ids


class Test(unittest.TestCase):


    def test(self):
        pass
