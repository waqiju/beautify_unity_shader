from .syntax_nonterminal import Nonterminal
from .syntax_production import Production
from .lex_tokens import TokenType as T
from .syntax_nonterminals import NonterminalType as N
import unittest


productionList = [
    # 1
    Production("prog -> 'Shader' String { shader_body }",
               'p1',
               N.prog,
               ('Shader', T.String, T.LBrace, N.shader_body, T.RBrace)),
    Production("shader_body -> props subshr",
               'p2',
               N.shader_body,
               (N.props, N.subshr)),
    # 2
    Production("props       -> 'Properties' { props_body }",
               'p3',
               N.props,
               ('Properties', T.LBrace, N.props_body, T.RBrace)),
    Production("props_body  -> prop_stm props_body",
               'p4',
               N.props_body,
               (N.prop_stm, N.props_body)),
    Production("props_body  -> ",
               'p5',
               N.props_body,
               ( )),
    Production("prop_stm    -> ID ( String, ID ) = prop_init",
               'p6',
               N.prop_stm,
               (T.ID, T.LParen, T.String, T.Comma, T.ReservedWord, T.RParen, T.Assign, N.prop_init)),
    Production("prop_init   -> Number",
               'p7',
               N.prop_init,
               (T.Number, )),
    Production("prop_init   -> String { }",
               'p8',
               N.prop_init,
               (T.String, T.LBrace, T.RBrace)),
    Production("prop_init    -> ( Number, Number, Number, Number )",
               'p9',
               N.prop_init,
               (T.LParen, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.RParen)),
    # 3
    Production("subshr      -> 'SubShader' { subshr_body }",
               'p10',
               N.subshr,
               ('SubShader', T.LBrace, N.subshr_body, T.RBrace)),
    Production("subshr_body -> tags",
               'p11',
               N.subshr_body,
               (N.tags, )),
    # 4
    Production("tags        -> 'Tags' { tags_body }",
               'p12',
               N.tags,
               ('Tags', T.LBrace, N.tags_body, T.RBrace)),
    Production("tags_body   -> tag_smt tags_body",
               'p13',
               N.tags_body,
               (N.tag_smt, N.tags_body)),
    Production("tags_body   -> ",
               'p14',
               N.tags_body,
               ( )),
    Production("tag_smt     -> String = String",
               'p15',
               N.tag_smt,
               (T.String, T.Assign, T.String)),
]


class Test(unittest.TestCase):

    def test(self):
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
