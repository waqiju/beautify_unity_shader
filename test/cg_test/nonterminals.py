from app.symbol_type import SymbolType
from app.syntax_nonterminal import Nonterminal
import unittest


class NonterminalType(SymbolType):

    prog = 'prog'
    cg_prog = 'cg_prog'
    cg_stms = 'cg_stms'
    cg_stm = 'cg_stm'
    preprocessing_stm = 'preprocessing_stm'
    pp_if_stm = 'pp_if_stm'
    pp_cmd = 'pp_cmd'
    ids = 'ids'
    dec = 'dec'
    dec_specifier_list = 'dec_specifier_list'
    dec_specifier = 'dec_specifier'
    type_specifier = 'type_specifier'
    type_qualifier = 'type_qualifier'
    init_dec_list = 'init_dec_list'


class prog(Nonterminal):
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


class ids(Nonterminal):
    pass


class dec(Nonterminal):
    pass


class dec_specifier_list(Nonterminal):
    pass


class dec_specifier(Nonterminal):
    pass


class type_specifier(Nonterminal):
    pass


class type_qualifier(Nonterminal):
    pass


class init_dec_list(Nonterminal):
    pass


class progp1(prog):
    # prog --> 'CGPROGRAM' cg_prog 'ENDCG'
    def __init__(self, CGPROGRAM, cg_prog, ENDCG):
        self.cg_prog = cg_prog


class cg_progp2(cg_prog):
    # cg_prog --> cg_stms
    def __init__(self, cg_stms):
        self.cg_stms = cg_stms


class cg_stmsp3(cg_stms):
    # cg_stms --> cg_stm cg_stms
    def __init__(self, cg_stm, cg_stms):
        self.cg_stm = cg_stm
        self.cg_stms = cg_stms


class cg_stmsp4(cg_stms):
    # cg_stms -->
    def __init__(self):
        pass


class cg_stmp5(cg_stm):
    # cg_stm --> preprocessing_stm
    def __init__(self, preprocessing_stm):
        self.preprocessing_stm = preprocessing_stm


class cg_stmp6(cg_stm):
    # cg_stm --> dec
    def __init__(self, dec):
        self.dec = dec


class preprocessing_stmp7(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class preprocessing_stmp8(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd


class pp_if_stmp9(pp_if_stm):
    # pp_if_stm --> # 'if' ID
    def __init__(self, Pound, _if, ID):
        self.ID = ID


class pp_if_stmp10(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID


class pp_if_stmp11(pp_if_stm):
    # pp_if_stm --> # 'ifndef' ID
    def __init__(self, Pound, ifndef, ID):
        self.ID = ID


class pp_if_stmp12(pp_if_stm):
    # pp_if_stm --> # 'elif' ID
    def __init__(self, Pound, _elif, ID):
        self.ID = ID


class pp_if_stmp13(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, _else):
        pass


class pp_if_stmp14(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass


class pp_cmdp15(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String


class pp_cmdp16(pp_cmd):
    # pp_cmd --> # 'pragma' ids
    def __init__(self, Pound, pragma, ids):
        self.ids = ids


class idsp17(ids):
    # ids --> ID ids
    def __init__(self, ID, ids):
        self.ID = ID
        self.ids = ids


class idsp18(ids):
    # ids -->
    def __init__(self):
        pass


class decp19(dec):
    # dec --> dec_specifier_list init_dec_list ;
    def __init__(self, dec_specifier_list, init_dec_list, Semicolon):
        self.dec_specifier_list = dec_specifier_list
        self.init_dec_list = init_dec_list


class dec_specifier_listp20(dec_specifier_list):
    # dec_specifier_list --> dec_specifier
    def __init__(self, dec_specifier):
        self.dec_specifier = dec_specifier


class dec_specifier_listp21(dec_specifier_list):
    # dec_specifier_list --> dec_specifier_list dec_specifier
    def __init__(self, dec_specifier_list, dec_specifier):
        self.dec_specifier_list = dec_specifier_list
        self.dec_specifier = dec_specifier


class dec_specifierp22(dec_specifier):
    # dec_specifier --> type_specifier
    def __init__(self, type_specifier):
        self.type_specifier = type_specifier


class dec_specifierp23(dec_specifier):
    # dec_specifier --> type_qualifier
    def __init__(self, type_qualifier):
        self.type_qualifier = type_qualifier


class type_specifierp24(type_specifier):
    # type_specifier --> 'void'
    def __init__(self, void):
        pass


class type_specifierp25(type_specifier):
    # type_specifier --> 'char'
    def __init__(self, char):
        pass


class type_specifierp26(type_specifier):
    # type_specifier --> 'short'
    def __init__(self, short):
        pass


class type_specifierp27(type_specifier):
    # type_specifier --> 'int'
    def __init__(self, int):
        pass


class type_specifierp28(type_specifier):
    # type_specifier --> 'long'
    def __init__(self, long):
        pass


class type_specifierp29(type_specifier):
    # type_specifier --> 'float'
    def __init__(self, float):
        pass


class type_specifierp30(type_specifier):
    # type_specifier --> 'double'
    def __init__(self, double):
        pass


class type_specifierp31(type_specifier):
    # type_specifier --> 'sampler2D'
    def __init__(self, sampler2D):
        pass


class type_qualifierp32(type_qualifier):
    # type_qualifier --> 'uniform'
    def __init__(self, uniform):
        pass


class init_dec_listp33(init_dec_list):
    # init_dec_list --> ID
    def __init__(self, ID):
        self.ID = ID


class Test(unittest.TestCase):


    def test(self):
        pass
