from app.syntax_nonterminal import Nonterminal
from app.syntax_production import Production
from app.lex_tokens import TokenType as T
from .nonterminals import NonterminalType as N
import unittest


productionList = [
    Production("prog ->  'CGPROGRAM' cg_prog 'ENDCG'",
               'p1',
               N.prog,
               ('CGPROGRAM', N.cg_prog, 'ENDCG', )),
    Production("cg_prog ->  cg_stms",
               'p2',
               N.cg_prog,
               (N.cg_stms, )),
    Production("cg_stms ->  cg_stm cg_stms",
               'p3',
               N.cg_stms,
               (N.cg_stm, N.cg_stms, )),
    Production("cg_stms -> ",
               'p4',
               N.cg_stms,
               ()),
    Production("cg_stm ->  preprocessing_stm",
               'p5',
               N.cg_stm,
               (N.preprocessing_stm, )),
    Production("cg_stm ->  dec",
               'p6',
               N.cg_stm,
               (N.dec, )),
    Production("preprocessing_stm ->  pp_if_stm",
               'p7',
               N.preprocessing_stm,
               (N.pp_if_stm, )),
    Production("preprocessing_stm ->  pp_cmd",
               'p8',
               N.preprocessing_stm,
               (N.pp_cmd, )),
    Production("pp_if_stm ->  # 'if' ID",
               'p9',
               N.pp_if_stm,
               (T.Pound, 'if', T.ID, )),
    Production("pp_if_stm ->  # 'ifdef' ID",
               'p10',
               N.pp_if_stm,
               (T.Pound, 'ifdef', T.ID, )),
    Production("pp_if_stm ->  # 'ifndef' ID",
               'p11',
               N.pp_if_stm,
               (T.Pound, 'ifndef', T.ID, )),
    Production("pp_if_stm ->  # 'elif' ID",
               'p12',
               N.pp_if_stm,
               (T.Pound, 'elif', T.ID, )),
    Production("pp_if_stm ->  # 'else'",
               'p13',
               N.pp_if_stm,
               (T.Pound, 'else', )),
    Production("pp_if_stm ->  # 'endif'",
               'p14',
               N.pp_if_stm,
               (T.Pound, 'endif', )),
    Production("pp_cmd ->  # 'include' String",
               'p15',
               N.pp_cmd,
               (T.Pound, 'include', T.String, )),
    Production("pp_cmd ->  # 'pragma' ids",
               'p16',
               N.pp_cmd,
               (T.Pound, 'pragma', N.ids, )),
    Production("ids ->  ID ids",
               'p17',
               N.ids,
               (T.ID, N.ids, )),
    Production("ids -> ",
               'p18',
               N.ids,
               ()),
    Production("dec ->  dec_specifier_list init_dec_list ;",
               'p19',
               N.dec,
               (N.dec_specifier_list, N.init_dec_list, T.Semicolon, )),
    Production("dec_specifier_list ->  dec_specifier",
               'p20',
               N.dec_specifier_list,
               (N.dec_specifier, )),
    Production("dec_specifier_list ->  dec_specifier_list dec_specifier",
               'p21',
               N.dec_specifier_list,
               (N.dec_specifier_list, N.dec_specifier, )),
    Production("dec_specifier ->  type_specifier",
               'p22',
               N.dec_specifier,
               (N.type_specifier, )),
    Production("dec_specifier ->  type_qualifier",
               'p23',
               N.dec_specifier,
               (N.type_qualifier, )),
    Production("type_specifier ->  'void'",
               'p24',
               N.type_specifier,
               ('void', )),
    Production("type_specifier ->  'char'",
               'p25',
               N.type_specifier,
               ('char', )),
    Production("type_specifier ->  'short'",
               'p26',
               N.type_specifier,
               ('short', )),
    Production("type_specifier ->  'int'",
               'p27',
               N.type_specifier,
               ('int', )),
    Production("type_specifier ->  'long'",
               'p28',
               N.type_specifier,
               ('long', )),
    Production("type_specifier ->  'float'",
               'p29',
               N.type_specifier,
               ('float', )),
    Production("type_specifier ->  'double'",
               'p30',
               N.type_specifier,
               ('double', )),
    Production("type_specifier ->  'sampler2D'",
               'p31',
               N.type_specifier,
               ('sampler2D', )),
    Production("type_qualifier ->  'uniform'",
               'p32',
               N.type_qualifier,
               ('uniform', )),
    Production("init_dec_list ->  ID",
               'p33',
               N.init_dec_list,
               (T.ID, )),
]


class Test(unittest.TestCase):

    def test(self):
        for production in productionList:
            print(production)


def _init():
    for p in productionList:
        # Production <--> Nonterminal
        name1 = p.left
        name2 = name1 + p.name

        cls1 = Nonterminal.getClass(name1)
        if cls1 is None:
            print('error: lack of nonterminal class. production = %s' % p)
        cls1.leadingProductions.append(p)
        cls2 = Nonterminal.getClass(name2) or Nonterminal.getClass(name1)
        cls2.production = p
        p.LeftNonterminalClass = cls2

        # add 'Shader' into TokenType
        stTuple = ()
        for elm in p.right:
            if elm not in T and elm not in N:
                newSt = '-%s-' % elm
                T.add(newSt)
                stTuple += (newSt,)
            else:
                stTuple += (elm,)
        p.right = stTuple


_init()
