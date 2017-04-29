from .syntax_nonterminal import Nonterminal
from .syntax_production import Production
from .lex_tokens import TokenType as T
from .syntax_nonterminals import NonterminalType as N
import unittest


productionList = [
    Production("prog ->  'Shader' String { shader_body }",
               'p1',
               N.prog,
               ('Shader', T.String, T.LBrace, N.shader_body, T.RBrace, )),
    Production("shader_body ->  props subshr",
               'p2',
               N.shader_body,
               (N.props, N.subshr, )),
    Production("props ->  'Properties' { props_body }",
               'p3',
               N.props,
               ('Properties', T.LBrace, N.props_body, T.RBrace, )),
    Production("props -> ",
               'p4',
               N.props,
               ()),
    Production("props_body ->  prop_stm props_body",
               'p5',
               N.props_body,
               (N.prop_stm, N.props_body, )),
    Production("props_body -> ",
               'p6',
               N.props_body,
               ()),
    Production("prop_stm ->  ID ( String , ReservedWord ) = prop_init",
               'p7',
               N.prop_stm,
               (T.ID, T.LParen, T.String, T.Comma, T.ReservedWord, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_init ->  Number",
               'p8',
               N.prop_init,
               (T.Number, )),
    Production("prop_init ->  String { }",
               'p9',
               N.prop_init,
               (T.String, T.LBrace, T.RBrace, )),
    Production("prop_init ->  ( Number , Number , Number , Number )",
               'p10',
               N.prop_init,
               (T.LParen, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.RParen, )),
    Production("subshr ->  'SubShader' { subshr_body }",
               'p11',
               N.subshr,
               ('SubShader', T.LBrace, N.subshr_body, T.RBrace, )),
    Production("subshr_body ->  tags cmds passes",
               'p12',
               N.subshr_body,
               (N.tags, N.cmds, N.passes, )),
    Production("tags ->  'Tags' { tags_body }",
               'p13',
               N.tags,
               ('Tags', T.LBrace, N.tags_body, T.RBrace, )),
    Production("tags_body ->  tag_smt tags_body",
               'p14',
               N.tags_body,
               (N.tag_smt, N.tags_body, )),
    Production("tags_body -> ",
               'p15',
               N.tags_body,
               ()),
    Production("tag_smt ->  String = String",
               'p16',
               N.tag_smt,
               (T.String, T.Assign, T.String, )),
    Production("cmds ->  cmd_stm cmds",
               'p17',
               N.cmds,
               (N.cmd_stm, N.cmds, )),
    Production("cmds -> ",
               'p18',
               N.cmds,
               ()),
    Production("cmd_stm ->  ReservedWord ids",
               'p19',
               N.cmd_stm,
               (T.ReservedWord, N.ids, )),
    Production("ids ->  ID ids",
               'p20',
               N.ids,
               (T.ID, N.ids, )),
    Production("ids -> ",
               'p21',
               N.ids,
               ()),
    Production("passes ->  shr_pass passes",
               'p22',
               N.passes,
               (N.shr_pass, N.passes, )),
    Production("passes -> ",
               'p23',
               N.passes,
               ()),
    Production("shr_pass ->  'Pass' { pass_body }",
               'p24',
               N.shr_pass,
               ('Pass', T.LBrace, N.pass_body, T.RBrace, )),
    Production("pass_body ->  'CGPROGRAM' cg_prog 'ENDCG'",
               'p25',
               N.pass_body,
               ('CGPROGRAM', N.cg_prog, 'ENDCG', )),
    Production("cg_prog ->  cg_stm",
               'p26',
               N.cg_prog,
               (N.cg_stm, )),
    Production("cg_stm ->  preprocessing_stm",
               'p27',
               N.cg_stm,
               (N.preprocessing_stm, )),
    Production("preprocessing_stm ->  pp_if_stm",
               'p28',
               N.preprocessing_stm,
               (N.pp_if_stm, )),
    Production("preprocessing_stm ->  pp_cmd",
               'p29',
               N.preprocessing_stm,
               (N.pp_cmd, )),
    Production("pp_if_stm ->  # 'if' ID",
               'p30',
               N.pp_if_stm,
               (T.Pound, 'if', T.ID, )),
    Production("pp_if_stm ->  # 'ifdef' ID",
               'p31',
               N.pp_if_stm,
               (T.Pound, 'ifdef', T.ID, )),
    Production("pp_if_stm ->  # 'idndef' ID",
               'p32',
               N.pp_if_stm,
               (T.Pound, 'idndef', T.ID, )),
    Production("pp_if_stm ->  # 'elif' ID",
               'p33',
               N.pp_if_stm,
               (T.Pound, 'elif', T.ID, )),
    Production("pp_if_stm ->  # 'else'",
               'p34',
               N.pp_if_stm,
               (T.Pound, 'else', )),
    Production("pp_if_stm ->  # 'endif'",
               'p35',
               N.pp_if_stm,
               (T.Pound, 'endif', )),
    Production("pp_cmd ->  # 'include' String",
               'p36',
               N.pp_cmd,
               (T.Pound, 'include', T.String, )),
]








class Test(unittest.TestCase):

    def testNonterminals(self):
        self.assertTrue(len(productionList) > 0)
        for production in productionList:
            print(production)
            
            from .lex_token import Token
            argsCount = len(production.right)
            args = []
            for i in range(0, argsCount):
                args.append(Token(i))
            production.LeftNonterminalClass(*args)






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
