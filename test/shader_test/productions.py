from app.syntax_nonterminal import Nonterminal
from app.syntax_production import Production
from app.lex_tokens import TokenType as T
from .nonterminals import NonterminalType as N
import unittest


productionList = [
    Production("prog ->  'Shader' String { shader_body_elms }",
               'p1',
               N.prog,
               ('Shader', T.String, T.LBrace, N.shader_body_elms, T.RBrace, )),
    Production("shader_body_elms ->  shader_body_elm shader_body_elms",
               'p2',
               N.shader_body_elms,
               (N.shader_body_elm, N.shader_body_elms, )),
    Production("shader_body_elms -> ",
               'p3',
               N.shader_body_elms,
               ()),
    Production("shader_body_elm ->  props",
               'p4',
               N.shader_body_elm,
               (N.props, )),
    Production("shader_body_elm ->  category",
               'p5',
               N.shader_body_elm,
               (N.category, )),
    Production("shader_body_elm ->  subshr",
               'p6',
               N.shader_body_elm,
               (N.subshr, )),
    Production("shader_body_elm ->  cg_prog",
               'p7',
               N.shader_body_elm,
               (N.cg_prog, )),
    Production("shader_body_elm ->  fall_back_cmd",
               'p8',
               N.shader_body_elm,
               (N.fall_back_cmd, )),
    Production("shader_body_elm ->  custom_editor_cmd",
               'p9',
               N.shader_body_elm,
               (N.custom_editor_cmd, )),
    Production("shader_body_elm ->  dependency_cmd",
               'p10',
               N.shader_body_elm,
               (N.dependency_cmd, )),
    Production("props ->  'Properties' { props_body }",
               'p11',
               N.props,
               ('Properties', T.LBrace, N.props_body, T.RBrace, )),
    Production("props_body ->  prop_stm props_body",
               'p12',
               N.props_body,
               (N.prop_stm, N.props_body, )),
    Production("props_body -> ",
               'p13',
               N.props_body,
               ()),
    Production("prop_stm ->  ID ( String , prop_type ) = prop_init",
               'p14',
               N.prop_stm,
               (T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_stm ->  [ ID ] ID ( String , prop_type ) = prop_init",
               'p15',
               N.prop_stm,
               (T.LBrack, T.ID, T.RBrack, T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_stm ->  [ ID ] [ ID ] ID ( String , prop_type ) = prop_init",
               'p16',
               N.prop_stm,
               (T.LBrack, T.ID, T.RBrack, T.LBrack, T.ID, T.RBrack, T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_stm ->  [ 'Enum' ( enum_items ) ] ID ( String , prop_type ) = prop_init",
               'p17',
               N.prop_stm,
               (T.LBrack, 'Enum', T.LParen, N.enum_items, T.RParen, T.RBrack, T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_stm ->  [ 'MaterialEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init",
               'p18',
               N.prop_stm,
               (T.LBrack, 'MaterialEnum', T.LParen, N.enum_items, T.RParen, T.RBrack, T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_stm ->  [ 'KeywordEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init",
               'p19',
               N.prop_stm,
               (T.LBrack, 'KeywordEnum', T.LParen, N.enum_items, T.RParen, T.RBrack, T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_stm ->  [ 'Toggle' ( ID ) ] ID ( String , prop_type ) = prop_init",
               'p20',
               N.prop_stm,
               (T.LBrack, 'Toggle', T.LParen, T.ID, T.RParen, T.RBrack, T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_stm ->  [ 'MaterialToggle' ] ID ( String , prop_type ) = prop_init",
               'p21',
               N.prop_stm,
               (T.LBrack, 'MaterialToggle', T.RBrack, T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_stm ->  [ 'ToggleOff' ] ID ( String , prop_type ) = prop_init",
               'p22',
               N.prop_stm,
               (T.LBrack, 'ToggleOff', T.RBrack, T.ID, T.LParen, T.String, T.Comma, N.prop_type, T.RParen, T.Assign, N.prop_init, )),
    Production("prop_type ->  'Color'",
               'p23',
               N.prop_type,
               ('Color', )),
    Production("prop_type ->  'Vector'",
               'p24',
               N.prop_type,
               ('Vector', )),
    Production("prop_type ->  'Range'",
               'p25',
               N.prop_type,
               ('Range', )),
    Production("prop_type ->  'Int'",
               'p26',
               N.prop_type,
               ('Int', )),
    Production("prop_type ->  'Float'",
               'p27',
               N.prop_type,
               ('Float', )),
    Production("prop_type ->  '2D'",
               'p28',
               N.prop_type,
               ('2D', )),
    Production("prop_type ->  'Cube'",
               'p29',
               N.prop_type,
               ('Cube', )),
    Production("prop_type ->  '3D'",
               'p30',
               N.prop_type,
               ('3D', )),
    Production("prop_type ->  'Any'",
               'p31',
               N.prop_type,
               ('Any', )),
    Production("prop_type ->  'Range' ( Number , Number )",
               'p32',
               N.prop_type,
               ('Range', T.LParen, T.Number, T.Comma, T.Number, T.RParen, )),
    Production("prop_init ->  Number",
               'p33',
               N.prop_init,
               (T.Number, )),
    Production("prop_init ->  String { }",
               'p34',
               N.prop_init,
               (T.String, T.LBrace, T.RBrace, )),
    Production("prop_init ->  String { ID }",
               'p35',
               N.prop_init,
               (T.String, T.LBrace, T.ID, T.RBrace, )),
    Production("prop_init ->  ( Number , Number , Number )",
               'p36',
               N.prop_init,
               (T.LParen, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.RParen, )),
    Production("prop_init ->  ( Number , Number , Number , Number )",
               'p37',
               N.prop_init,
               (T.LParen, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.RParen, )),
    Production("enum_items ->  enum_item",
               'p38',
               N.enum_items,
               (N.enum_item, )),
    Production("enum_items ->  enum_item , enum_items",
               'p39',
               N.enum_items,
               (N.enum_item, T.Comma, N.enum_items, )),
    Production("enum_item ->  id_list",
               'p40',
               N.enum_item,
               (N.id_list, )),
    Production("enum_item ->  Number",
               'p41',
               N.enum_item,
               (T.Number, )),
    Production("category ->  'Category' { category_body_elms }",
               'p42',
               N.category,
               ('Category', T.LBrace, N.category_body_elms, T.RBrace, )),
    Production("category_body_elms ->  category_body_elm category_body_elms",
               'p43',
               N.category_body_elms,
               (N.category_body_elm, N.category_body_elms, )),
    Production("category_body_elms -> ",
               'p44',
               N.category_body_elms,
               ()),
    Production("category_body_elm ->  cmd_stm",
               'p45',
               N.category_body_elm,
               (N.cmd_stm, )),
    Production("category_body_elm ->  subshr",
               'p46',
               N.category_body_elm,
               (N.subshr, )),
    Production("subshr ->  'SubShader' { subshr_body_elms }",
               'p47',
               N.subshr,
               ('SubShader', T.LBrace, N.subshr_body_elms, T.RBrace, )),
    Production("subshr_body_elms ->  subshr_body_elm subshr_body_elms",
               'p48',
               N.subshr_body_elms,
               (N.subshr_body_elm, N.subshr_body_elms, )),
    Production("subshr_body_elms -> ",
               'p49',
               N.subshr_body_elms,
               ()),
    Production("subshr_body_elm ->  cmd_stm",
               'p50',
               N.subshr_body_elm,
               (N.cmd_stm, )),
    Production("subshr_body_elm ->  shr_pass",
               'p51',
               N.subshr_body_elm,
               (N.shr_pass, )),
    Production("subshr_body_elm ->  cg_prog",
               'p52',
               N.subshr_body_elm,
               (N.cg_prog, )),
    Production("cmd_stm ->  cmd_name id_or_number_or_placeholder",
               'p53',
               N.cmd_stm,
               (N.cmd_name, N.id_or_number_or_placeholder, )),
    Production("cmd_stm ->  'Alphatest' ID",
               'p54',
               N.cmd_stm,
               ('Alphatest', T.ID, )),
    Production("cmd_stm ->  'Alphatest' ID placeholder",
               'p55',
               N.cmd_stm,
               ('Alphatest', T.ID, N.placeholder, )),
    Production("cmd_stm ->  'BindChannels' { bind_channel_stms }",
               'p56',
               N.cmd_stm,
               ('BindChannels', T.LBrace, N.bind_channel_stms, T.RBrace, )),
    Production("cmd_stm ->  'Blend' ID",
               'p57',
               N.cmd_stm,
               ('Blend', T.ID, )),
    Production("cmd_stm ->  'Blend' id_or_number_or_placeholder id_or_number_or_placeholder",
               'p58',
               N.cmd_stm,
               ('Blend', N.id_or_number_or_placeholder, N.id_or_number_or_placeholder, )),
    Production("cmd_stm ->  'Fog' { 'Mode' ID }",
               'p59',
               N.cmd_stm,
               ('Fog', T.LBrace, 'Mode', T.ID, T.RBrace, )),
    Production("cmd_stm ->  'Fog' { 'Color' ( Number , Number , Number , Number ) }",
               'p60',
               N.cmd_stm,
               ('Fog', T.LBrace, 'Color', T.LParen, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.RParen, T.RBrace, )),
    Production("cmd_stm ->  'Material' { meterial_stms }",
               'p61',
               N.cmd_stm,
               ('Material', T.LBrace, N.meterial_stms, T.RBrace, )),
    Production("cmd_stm ->  'Name' String",
               'p62',
               N.cmd_stm,
               ('Name', T.String, )),
    Production("cmd_stm ->  'Offset' id_or_number_or_placeholder , id_or_number_or_placeholder",
               'p63',
               N.cmd_stm,
               ('Offset', N.id_or_number_or_placeholder, T.Comma, N.id_or_number_or_placeholder, )),
    Production("cmd_stm ->  'Stencil' { stencil_stms }",
               'p64',
               N.cmd_stm,
               ('Stencil', T.LBrace, N.stencil_stms, T.RBrace, )),
    Production("cmd_stm ->  'SetTexture' placeholder { set_texture_stms }",
               'p65',
               N.cmd_stm,
               ('SetTexture', N.placeholder, T.LBrace, N.set_texture_stms, T.RBrace, )),
    Production("cmd_stm ->  'Tags' { tags_stms }",
               'p66',
               N.cmd_stm,
               ('Tags', T.LBrace, N.tags_stms, T.RBrace, )),
    Production("cmd_name ->  'AlphaToMask'",
               'p67',
               N.cmd_name,
               ('AlphaToMask', )),
    Production("cmd_name ->  'ColorMask'",
               'p68',
               N.cmd_name,
               ('ColorMask', )),
    Production("cmd_name ->  'ColorMaterial'",
               'p69',
               N.cmd_name,
               ('ColorMaterial', )),
    Production("cmd_name ->  'Cull'",
               'p70',
               N.cmd_name,
               ('Cull', )),
    Production("cmd_name ->  'Lighting'",
               'p71',
               N.cmd_name,
               ('Lighting', )),
    Production("cmd_name ->  'LOD'",
               'p72',
               N.cmd_name,
               ('LOD', )),
    Production("cmd_name ->  'SeparateSpecular'",
               'p73',
               N.cmd_name,
               ('SeparateSpecular', )),
    Production("cmd_name ->  'ZTest'",
               'p74',
               N.cmd_name,
               ('ZTest', )),
    Production("cmd_name ->  'ZWrite'",
               'p75',
               N.cmd_name,
               ('ZWrite', )),
    Production("id_or_number_or_placeholder ->  ID",
               'p76',
               N.id_or_number_or_placeholder,
               (T.ID, )),
    Production("id_or_number_or_placeholder ->  Number",
               'p77',
               N.id_or_number_or_placeholder,
               (T.Number, )),
    Production("id_or_number_or_placeholder ->  ( Number , Number , Number , Number )",
               'p78',
               N.id_or_number_or_placeholder,
               (T.LParen, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.Comma, T.Number, T.RParen, )),
    Production("id_or_number_or_placeholder ->  placeholder",
               'p79',
               N.id_or_number_or_placeholder,
               (N.placeholder, )),
    Production("placeholder ->  [ ID ]",
               'p80',
               N.placeholder,
               (T.LBrack, T.ID, T.RBrack, )),
    Production("bind_channel_stms ->  bind_channel_stm bind_channel_stms",
               'p81',
               N.bind_channel_stms,
               (N.bind_channel_stm, N.bind_channel_stms, )),
    Production("bind_channel_stms -> ",
               'p82',
               N.bind_channel_stms,
               ()),
    Production("bind_channel_stm ->  'Bind' String , ID",
               'p83',
               N.bind_channel_stm,
               ('Bind', T.String, T.Comma, T.ID, )),
    Production("meterial_stms ->  meterial_stm meterial_stms",
               'p84',
               N.meterial_stms,
               (N.meterial_stm, N.meterial_stms, )),
    Production("meterial_stms -> ",
               'p85',
               N.meterial_stms,
               ()),
    Production("meterial_stm ->  ID id_or_number_or_placeholder",
               'p86',
               N.meterial_stm,
               (T.ID, N.id_or_number_or_placeholder, )),
    Production("stencil_stms ->  stencil_stm stencil_stms",
               'p87',
               N.stencil_stms,
               (N.stencil_stm, N.stencil_stms, )),
    Production("stencil_stms -> ",
               'p88',
               N.stencil_stms,
               ()),
    Production("stencil_stm ->  ID id_or_number_or_placeholder",
               'p89',
               N.stencil_stm,
               (T.ID, N.id_or_number_or_placeholder, )),
    Production("set_texture_stms ->  set_texture_stm set_texture_stms",
               'p90',
               N.set_texture_stms,
               (N.set_texture_stm, N.set_texture_stms, )),
    Production("set_texture_stms -> ",
               'p91',
               N.set_texture_stms,
               ()),
    Production("set_texture_stm ->  'matrix' placeholder",
               'p92',
               N.set_texture_stm,
               ('matrix', N.placeholder, )),
    Production("set_texture_stm ->  'constantColor' id_or_number_or_placeholder",
               'p93',
               N.set_texture_stm,
               ('constantColor', N.id_or_number_or_placeholder, )),
    Production("set_texture_stm ->  'combine' combine_options",
               'p94',
               N.set_texture_stm,
               ('combine', N.combine_options, )),
    Production("combine_options ->  combine_option combine_options",
               'p95',
               N.combine_options,
               (N.combine_option, N.combine_options, )),
    Production("combine_options ->  combine_option , combine_options",
               'p96',
               N.combine_options,
               (N.combine_option, T.Comma, N.combine_options, )),
    Production("combine_options ->  combine_option combine_option_op combine_options",
               'p97',
               N.combine_options,
               (N.combine_option, N.combine_option_op, N.combine_options, )),
    Production("combine_options -> ",
               'p98',
               N.combine_options,
               ()),
    Production("combine_option ->  ID",
               'p99',
               N.combine_option,
               (T.ID, )),
    Production("combine_option ->  ( ID )",
               'p100',
               N.combine_option,
               (T.LParen, T.ID, T.RParen, )),
    Production("combine_option_op ->  +",
               'p101',
               N.combine_option_op,
               (T.Plus, )),
    Production("combine_option_op ->  -",
               'p102',
               N.combine_option_op,
               (T.Minus, )),
    Production("combine_option_op ->  *",
               'p103',
               N.combine_option_op,
               (T.Times, )),
    Production("combine_option_op ->  /",
               'p104',
               N.combine_option_op,
               (T.Divide, )),
    Production("tags_stms ->  tag_smt tags_stms",
               'p105',
               N.tags_stms,
               (N.tag_smt, N.tags_stms, )),
    Production("tags_stms -> ",
               'p106',
               N.tags_stms,
               ()),
    Production("tag_smt ->  String = String",
               'p107',
               N.tag_smt,
               (T.String, T.Assign, T.String, )),
    Production("shr_pass ->  'Pass' { pass_body_elms }",
               'p108',
               N.shr_pass,
               ('Pass', T.LBrace, N.pass_body_elms, T.RBrace, )),
    Production("shr_pass ->  'GrabPass' { pass_body_elms }",
               'p109',
               N.shr_pass,
               ('GrabPass', T.LBrace, N.pass_body_elms, T.RBrace, )),
    Production("shr_pass ->  'UsePass' String",
               'p110',
               N.shr_pass,
               ('UsePass', T.String, )),
    Production("pass_body_elms ->  pass_body_elm pass_body_elms",
               'p111',
               N.pass_body_elms,
               (N.pass_body_elm, N.pass_body_elms, )),
    Production("pass_body_elms -> ",
               'p112',
               N.pass_body_elms,
               ()),
    Production("pass_body_elm ->  cmd_stm",
               'p113',
               N.pass_body_elm,
               (N.cmd_stm, )),
    Production("pass_body_elm ->  cg_prog",
               'p114',
               N.pass_body_elm,
               (N.cg_prog, )),
    Production("cg_prog ->  'CGPROGRAM' 'ENDCG'",
               'p115',
               N.cg_prog,
               ('CGPROGRAM', 'ENDCG', )),
    Production("cg_prog ->  'CGINCLUDE' 'ENDCG'",
               'p116',
               N.cg_prog,
               ('CGINCLUDE', 'ENDCG', )),
    Production("fall_back_cmd ->  'FallBack' String",
               'p117',
               N.fall_back_cmd,
               ('FallBack', T.String, )),
    Production("fall_back_cmd ->  'FallBack' 'Off'",
               'p118',
               N.fall_back_cmd,
               ('FallBack', 'Off', )),
    Production("custom_editor_cmd ->  'CustomEditor' String",
               'p119',
               N.custom_editor_cmd,
               ('CustomEditor', T.String, )),
    Production("dependency_cmd ->  'Dependency' String = String",
               'p120',
               N.dependency_cmd,
               ('Dependency', T.String, T.Assign, T.String, )),
    Production("id_list ->  ID",
               'p121',
               N.id_list,
               (T.ID, )),
    Production("id_list ->  ID id_list",
               'p122',
               N.id_list,
               (T.ID, N.id_list, )),
]


































































































class Test(unittest.TestCase):

    def Dtest(self):
        for production in productionList:
            print(production)


    def DtestTokenType(self):
        for ty in T:
            print(ty)


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
                newSt = '-%s-' % str.lower(elm)
                T.add(newSt)
                stTuple += (newSt,)
            else:
                stTuple += (elm,)
        p.right = stTuple


_init()
