from app.symbol_type import SymbolType
from app.syntax_nonterminal import Nonterminal
from app.formatter import I, AAI, IAA, SSI, ISS, GB, GA, RestoreComment
import unittest


class NonterminalType(SymbolType):

    prog = 'prog'
    shader_body_elms = 'shader_body_elms'
    shader_body_elm = 'shader_body_elm'
    props = 'props'
    props_body = 'props_body'
    prop_stm = 'prop_stm'
    prop_type = 'prop_type'
    prop_init = 'prop_init'
    enum_items = 'enum_items'
    enum_item = 'enum_item'
    category = 'category'
    category_body_elms = 'category_body_elms'
    category_body_elm = 'category_body_elm'
    subshr = 'subshr'
    subshr_body_elms = 'subshr_body_elms'
    subshr_body_elm = 'subshr_body_elm'
    cmd_stm = 'cmd_stm'
    cmd_name = 'cmd_name'
    id_or_number_or_placeholder = 'id_or_number_or_placeholder'
    placeholder = 'placeholder'
    bind_channel_stms = 'bind_channel_stms'
    bind_channel_stm = 'bind_channel_stm'
    meterial_stms = 'meterial_stms'
    meterial_stm = 'meterial_stm'
    stencil_stms = 'stencil_stms'
    stencil_stm = 'stencil_stm'
    set_texture_stms = 'set_texture_stms'
    set_texture_stm = 'set_texture_stm'
    combine_options = 'combine_options'
    combine_option = 'combine_option'
    combine_option_op = 'combine_option_op'
    tags_stms = 'tags_stms'
    tag_smt = 'tag_smt'
    shr_pass = 'shr_pass'
    pass_body_elms = 'pass_body_elms'
    pass_body_elm = 'pass_body_elm'
    cg_prog = 'cg_prog'
    fall_back_cmd = 'fall_back_cmd'
    custom_editor_cmd = 'custom_editor_cmd'
    dependency_cmd = 'dependency_cmd'
    id_list = 'id_list'


class prog(Nonterminal):
    pass


class shader_body_elms(Nonterminal):
    pass


class shader_body_elm(Nonterminal):
    pass


class props(Nonterminal):
    pass


class props_body(Nonterminal):
    pass


class prop_stm(Nonterminal):
    pass


class prop_type(Nonterminal):
    pass


class prop_init(Nonterminal):
    pass


class enum_items(Nonterminal):
    pass


class enum_item(Nonterminal):
    pass


class category(Nonterminal):
    pass


class category_body_elms(Nonterminal):
    pass


class category_body_elm(Nonterminal):
    pass


class subshr(Nonterminal):
    pass


class subshr_body_elms(Nonterminal):
    pass


class subshr_body_elm(Nonterminal):
    pass


class cmd_stm(Nonterminal):
    pass


class cmd_name(Nonterminal):
    pass


class id_or_number_or_placeholder(Nonterminal):
    pass


class placeholder(Nonterminal):
    pass


class bind_channel_stms(Nonterminal):
    pass


class bind_channel_stm(Nonterminal):
    pass


class meterial_stms(Nonterminal):
    pass


class meterial_stm(Nonterminal):
    pass


class stencil_stms(Nonterminal):
    pass


class stencil_stm(Nonterminal):
    pass


class set_texture_stms(Nonterminal):
    pass


class set_texture_stm(Nonterminal):
    pass


class combine_options(Nonterminal):
    pass


class combine_option(Nonterminal):
    pass


class combine_option_op(Nonterminal):
    pass


class tags_stms(Nonterminal):
    pass


class tag_smt(Nonterminal):
    pass


class shr_pass(Nonterminal):
    pass


class pass_body_elms(Nonterminal):
    pass


class pass_body_elm(Nonterminal):
    pass


class cg_prog(Nonterminal):
    pass


class fall_back_cmd(Nonterminal):
    pass


class custom_editor_cmd(Nonterminal):
    pass


class dependency_cmd(Nonterminal):
    pass


class id_list(Nonterminal):
    pass


class progp1(prog):
    # prog --> 'Shader' String { shader_body_elms }
    def __init__(self, Shader, String, LBrace, shader_body_elms, RBrace):
        self.String = String
        self.shader_body_elms = shader_body_elms

    def toCode(self):
        return 'Shader' + self.String.toCode() + '{' + self.shader_body_elms.toCode() + '}'


class shader_body_elmsp2(shader_body_elms):
    # shader_body_elms --> shader_body_elm shader_body_elms
    def __init__(self, shader_body_elm, shader_body_elms):
        self.shader_body_elm = shader_body_elm
        self.shader_body_elms = shader_body_elms

    def toCode(self):
        return self.shader_body_elm.toCode() + self.shader_body_elms.toCode()


class shader_body_elmsp3(shader_body_elms):
    # shader_body_elms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class shader_body_elmp4(shader_body_elm):
    # shader_body_elm --> props
    def __init__(self, props):
        self.props = props

    def toCode(self):
        return self.props.toCode()


class shader_body_elmp5(shader_body_elm):
    # shader_body_elm --> category
    def __init__(self, category):
        self.category = category

    def toCode(self):
        return self.category.toCode()


class shader_body_elmp6(shader_body_elm):
    # shader_body_elm --> subshr
    def __init__(self, subshr):
        self.subshr = subshr

    def toCode(self):
        return self.subshr.toCode()


class shader_body_elmp7(shader_body_elm):
    # shader_body_elm --> cg_prog
    def __init__(self, cg_prog):
        self.cg_prog = cg_prog

    def toCode(self):
        return self.cg_prog.toCode()


class shader_body_elmp8(shader_body_elm):
    # shader_body_elm --> fall_back_cmd
    def __init__(self, fall_back_cmd):
        self.fall_back_cmd = fall_back_cmd

    def toCode(self):
        return self.fall_back_cmd.toCode()


class shader_body_elmp9(shader_body_elm):
    # shader_body_elm --> custom_editor_cmd
    def __init__(self, custom_editor_cmd):
        self.custom_editor_cmd = custom_editor_cmd

    def toCode(self):
        return self.custom_editor_cmd.toCode()


class shader_body_elmp10(shader_body_elm):
    # shader_body_elm --> dependency_cmd
    def __init__(self, dependency_cmd):
        self.dependency_cmd = dependency_cmd

    def toCode(self):
        return self.dependency_cmd.toCode()


class propsp11(props):
    # props --> 'Properties' { props_body }
    def __init__(self, Properties, LBrace, props_body, RBrace):
        self.props_body = props_body

    def toCode(self):
        return 'Properties' + '{' + self.props_body.toCode() + '}'


class props_bodyp12(props_body):
    # props_body --> prop_stm props_body
    def __init__(self, prop_stm, props_body):
        self.prop_stm = prop_stm
        self.props_body = props_body

    def toCode(self):
        return self.prop_stm.toCode() + self.props_body.toCode()


class props_bodyp13(props_body):
    # props_body -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class prop_stmp14(prop_stm):
    # prop_stm --> ID ( String , prop_type ) = prop_init
    def __init__(self, ID, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp15(prop_stm):
    # prop_stm --> [ ID ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, ID1, RBrack, ID2, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID1 = ID1
        self.ID2 = ID2
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + self.ID1.toCode() + ']' + self.ID2.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp16(prop_stm):
    # prop_stm --> [ ID ] [ ID ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack1, ID1, RBrack1, LBrack2, ID2, RBrack2, ID3, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID1 = ID1
        self.ID2 = ID2
        self.ID3 = ID3
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + self.ID1.toCode() + ']' + '[' + self.ID2.toCode() + ']' + self.ID3.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp17(prop_stm):
    # prop_stm --> [ 'Enum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, Enum, LParen1, enum_items, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.enum_items = enum_items
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'Enum' + '(' + self.enum_items.toCode() + ')' + ']' + self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp18(prop_stm):
    # prop_stm --> [ 'MaterialEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, MaterialEnum, LParen1, enum_items, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.enum_items = enum_items
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'MaterialEnum' + '(' + self.enum_items.toCode() + ')' + ']' + self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp19(prop_stm):
    # prop_stm --> [ 'KeywordEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, KeywordEnum, LParen1, enum_items, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.enum_items = enum_items
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'KeywordEnum' + '(' + self.enum_items.toCode() + ')' + ']' + self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp20(prop_stm):
    # prop_stm --> [ 'Toggle' ( ID ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, Toggle, LParen1, ID1, RParen1, RBrack, ID2, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.ID1 = ID1
        self.ID2 = ID2
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'Toggle' + '(' + self.ID1.toCode() + ')' + ']' + self.ID2.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp21(prop_stm):
    # prop_stm --> [ 'MaterialToggle' ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, MaterialToggle, RBrack, ID, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'MaterialToggle' + ']' + self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp22(prop_stm):
    # prop_stm --> [ 'ToggleOff' ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, ToggleOff, RBrack, ID, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'ToggleOff' + ']' + self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_typep23(prop_type):
    # prop_type --> 'Color'
    def __init__(self, Color):
        pass

    def toCode(self):
        return 'Color'


class prop_typep24(prop_type):
    # prop_type --> 'Vector'
    def __init__(self, Vector):
        pass

    def toCode(self):
        return 'Vector'


class prop_typep25(prop_type):
    # prop_type --> 'Range'
    def __init__(self, Range):
        pass

    def toCode(self):
        return 'Range'


class prop_typep26(prop_type):
    # prop_type --> 'Int'
    def __init__(self, Int):
        pass

    def toCode(self):
        return 'Int'


class prop_typep27(prop_type):
    # prop_type --> 'Float'
    def __init__(self, Float):
        pass

    def toCode(self):
        return 'Float'


class prop_typep28(prop_type):
    # prop_type --> '2D'
    def __init__(self, 2D):
        pass

    def toCode(self):
        return '2D'


class prop_typep29(prop_type):
    # prop_type --> 'Cube'
    def __init__(self, Cube):
        pass

    def toCode(self):
        return 'Cube'


class prop_typep30(prop_type):
    # prop_type --> '3D'
    def __init__(self, 3D):
        pass

    def toCode(self):
        return '3D'


class prop_typep31(prop_type):
    # prop_type --> 'Any'
    def __init__(self, Any):
        pass

    def toCode(self):
        return 'Any'


class prop_typep32(prop_type):
    # prop_type --> 'Range' ( Number , Number )
    def __init__(self, Range, LParen, Number1, Comma, Number2, RParen):
        self.Number1 = Number1
        self.Number2 = Number2

    def toCode(self):
        return 'Range' + '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ')'


class prop_initp33(prop_init):
    # prop_init --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class prop_initp34(prop_init):
    # prop_init --> String { }
    def __init__(self, String, LBrace, RBrace):
        self.String = String

    def toCode(self):
        return self.String.toCode() + '{' + '}'


class prop_initp35(prop_init):
    # prop_init --> String { ID }
    def __init__(self, String, LBrace, ID, RBrace):
        self.String = String
        self.ID = ID

    def toCode(self):
        return self.String.toCode() + '{' + self.ID.toCode() + '}'


class prop_initp36(prop_init):
    # prop_init --> ( Number , Number , Number )
    def __init__(self, LParen, Number1, Comma1, Number2, Comma2, Number3, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3

    def toCode(self):
        return '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ',' + self.Number3.toCode() + ')'


class prop_initp37(prop_init):
    # prop_init --> ( Number , Number , Number , Number )
    def __init__(self, LParen, Number1, Comma1, Number2, Comma2, Number3, Comma3, Number4, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3
        self.Number4 = Number4

    def toCode(self):
        return '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ',' + self.Number3.toCode() + ',' + self.Number4.toCode() + ')'


class enum_itemsp38(enum_items):
    # enum_items --> enum_item
    def __init__(self, enum_item):
        self.enum_item = enum_item

    def toCode(self):
        return self.enum_item.toCode()


class enum_itemsp39(enum_items):
    # enum_items --> enum_item , enum_items
    def __init__(self, enum_item, Comma, enum_items):
        self.enum_item = enum_item
        self.enum_items = enum_items

    def toCode(self):
        return self.enum_item.toCode() + ',' + self.enum_items.toCode()


class enum_itemp40(enum_item):
    # enum_item --> id_list
    def __init__(self, id_list):
        self.id_list = id_list

    def toCode(self):
        return self.id_list.toCode()


class enum_itemp41(enum_item):
    # enum_item --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class categoryp42(category):
    # category --> 'Category' { category_body_elms }
    def __init__(self, Category, LBrace, category_body_elms, RBrace):
        self.category_body_elms = category_body_elms

    def toCode(self):
        return 'Category' + '{' + self.category_body_elms.toCode() + '}'


class category_body_elmsp43(category_body_elms):
    # category_body_elms --> category_body_elm category_body_elms
    def __init__(self, category_body_elm, category_body_elms):
        self.category_body_elm = category_body_elm
        self.category_body_elms = category_body_elms

    def toCode(self):
        return self.category_body_elm.toCode() + self.category_body_elms.toCode()


class category_body_elmsp44(category_body_elms):
    # category_body_elms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class category_body_elmp45(category_body_elm):
    # category_body_elm --> cmd_stm
    def __init__(self, cmd_stm):
        self.cmd_stm = cmd_stm

    def toCode(self):
        return self.cmd_stm.toCode()


class category_body_elmp46(category_body_elm):
    # category_body_elm --> subshr
    def __init__(self, subshr):
        self.subshr = subshr

    def toCode(self):
        return self.subshr.toCode()


class subshrp47(subshr):
    # subshr --> 'SubShader' { subshr_body_elms }
    def __init__(self, SubShader, LBrace, subshr_body_elms, RBrace):
        self.subshr_body_elms = subshr_body_elms

    def toCode(self):
        return 'SubShader' + '{' + self.subshr_body_elms.toCode() + '}'


class subshr_body_elmsp48(subshr_body_elms):
    # subshr_body_elms --> subshr_body_elm subshr_body_elms
    def __init__(self, subshr_body_elm, subshr_body_elms):
        self.subshr_body_elm = subshr_body_elm
        self.subshr_body_elms = subshr_body_elms

    def toCode(self):
        return self.subshr_body_elm.toCode() + self.subshr_body_elms.toCode()


class subshr_body_elmsp49(subshr_body_elms):
    # subshr_body_elms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class subshr_body_elmp50(subshr_body_elm):
    # subshr_body_elm --> cmd_stm
    def __init__(self, cmd_stm):
        self.cmd_stm = cmd_stm

    def toCode(self):
        return self.cmd_stm.toCode()


class subshr_body_elmp51(subshr_body_elm):
    # subshr_body_elm --> shr_pass
    def __init__(self, shr_pass):
        self.shr_pass = shr_pass

    def toCode(self):
        return self.shr_pass.toCode()


class subshr_body_elmp52(subshr_body_elm):
    # subshr_body_elm --> cg_prog
    def __init__(self, cg_prog):
        self.cg_prog = cg_prog

    def toCode(self):
        return self.cg_prog.toCode()


class cmd_stmp53(cmd_stm):
    # cmd_stm --> cmd_name id_or_number_or_placeholder
    def __init__(self, cmd_name, id_or_number_or_placeholder):
        self.cmd_name = cmd_name
        self.id_or_number_or_placeholder = id_or_number_or_placeholder

    def toCode(self):
        return self.cmd_name.toCode() + self.id_or_number_or_placeholder.toCode()


class cmd_stmp54(cmd_stm):
    # cmd_stm --> 'Alphatest' ID
    def __init__(self, Alphatest, ID):
        self.ID = ID

    def toCode(self):
        return 'Alphatest' + self.ID.toCode()


class cmd_stmp55(cmd_stm):
    # cmd_stm --> 'Alphatest' ID placeholder
    def __init__(self, Alphatest, ID, placeholder):
        self.ID = ID
        self.placeholder = placeholder

    def toCode(self):
        return 'Alphatest' + self.ID.toCode() + self.placeholder.toCode()


class cmd_stmp56(cmd_stm):
    # cmd_stm --> 'BindChannels' { bind_channel_stms }
    def __init__(self, BindChannels, LBrace, bind_channel_stms, RBrace):
        self.bind_channel_stms = bind_channel_stms

    def toCode(self):
        return 'BindChannels' + '{' + self.bind_channel_stms.toCode() + '}'


class cmd_stmp57(cmd_stm):
    # cmd_stm --> 'Blend' ID
    def __init__(self, Blend, ID):
        self.ID = ID

    def toCode(self):
        return 'Blend' + self.ID.toCode()


class cmd_stmp58(cmd_stm):
    # cmd_stm --> 'Blend' id_or_number_or_placeholder id_or_number_or_placeholder
    def __init__(self, Blend, id_or_number_or_placeholder1, id_or_number_or_placeholder2):
        self.id_or_number_or_placeholder1 = id_or_number_or_placeholder1
        self.id_or_number_or_placeholder2 = id_or_number_or_placeholder2

    def toCode(self):
        return 'Blend' + self.id_or_number_or_placeholder1.toCode() + self.id_or_number_or_placeholder2.toCode()


class cmd_stmp59(cmd_stm):
    # cmd_stm --> 'Fog' { 'Mode' ID }
    def __init__(self, Fog, LBrace, Mode, ID, RBrace):
        self.ID = ID

    def toCode(self):
        return 'Fog' + '{' + 'Mode' + self.ID.toCode() + '}'


class cmd_stmp60(cmd_stm):
    # cmd_stm --> 'Fog' { 'Color' ( Number , Number , Number , Number ) }
    def __init__(self, Fog, LBrace, Color, LParen, Number1, Comma1, Number2, Comma2, Number3, Comma3, Number4, RParen, RBrace):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3
        self.Number4 = Number4

    def toCode(self):
        return 'Fog' + '{' + 'Color' + '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ',' + self.Number3.toCode() + ',' + self.Number4.toCode() + ')' + '}'


class cmd_stmp61(cmd_stm):
    # cmd_stm --> 'Material' { meterial_stms }
    def __init__(self, Material, LBrace, meterial_stms, RBrace):
        self.meterial_stms = meterial_stms

    def toCode(self):
        return 'Material' + '{' + self.meterial_stms.toCode() + '}'


class cmd_stmp62(cmd_stm):
    # cmd_stm --> 'Name' String
    def __init__(self, Name, String):
        self.String = String

    def toCode(self):
        return 'Name' + self.String.toCode()


class cmd_stmp63(cmd_stm):
    # cmd_stm --> 'Offset' id_or_number_or_placeholder , id_or_number_or_placeholder
    def __init__(self, Offset, id_or_number_or_placeholder1, Comma, id_or_number_or_placeholder2):
        self.id_or_number_or_placeholder1 = id_or_number_or_placeholder1
        self.id_or_number_or_placeholder2 = id_or_number_or_placeholder2

    def toCode(self):
        return 'Offset' + self.id_or_number_or_placeholder1.toCode() + ',' + self.id_or_number_or_placeholder2.toCode()


class cmd_stmp64(cmd_stm):
    # cmd_stm --> 'Stencil' { stencil_stms }
    def __init__(self, Stencil, LBrace, stencil_stms, RBrace):
        self.stencil_stms = stencil_stms

    def toCode(self):
        return 'Stencil' + '{' + self.stencil_stms.toCode() + '}'


class cmd_stmp65(cmd_stm):
    # cmd_stm --> 'SetTexture' placeholder { set_texture_stms }
    def __init__(self, SetTexture, placeholder, LBrace, set_texture_stms, RBrace):
        self.placeholder = placeholder
        self.set_texture_stms = set_texture_stms

    def toCode(self):
        return 'SetTexture' + self.placeholder.toCode() + '{' + self.set_texture_stms.toCode() + '}'


class cmd_stmp66(cmd_stm):
    # cmd_stm --> 'Tags' { tags_stms }
    def __init__(self, Tags, LBrace, tags_stms, RBrace):
        self.tags_stms = tags_stms

    def toCode(self):
        return 'Tags' + '{' + self.tags_stms.toCode() + '}'


class cmd_namep67(cmd_name):
    # cmd_name --> 'AlphaToMask'
    def __init__(self, AlphaToMask):
        pass

    def toCode(self):
        return 'AlphaToMask'


class cmd_namep68(cmd_name):
    # cmd_name --> 'ColorMask'
    def __init__(self, ColorMask):
        pass

    def toCode(self):
        return 'ColorMask'


class cmd_namep69(cmd_name):
    # cmd_name --> 'ColorMaterial'
    def __init__(self, ColorMaterial):
        pass

    def toCode(self):
        return 'ColorMaterial'


class cmd_namep70(cmd_name):
    # cmd_name --> 'Cull'
    def __init__(self, Cull):
        pass

    def toCode(self):
        return 'Cull'


class cmd_namep71(cmd_name):
    # cmd_name --> 'Lighting'
    def __init__(self, Lighting):
        pass

    def toCode(self):
        return 'Lighting'


class cmd_namep72(cmd_name):
    # cmd_name --> 'LOD'
    def __init__(self, LOD):
        pass

    def toCode(self):
        return 'LOD'


class cmd_namep73(cmd_name):
    # cmd_name --> 'SeparateSpecular'
    def __init__(self, SeparateSpecular):
        pass

    def toCode(self):
        return 'SeparateSpecular'


class cmd_namep74(cmd_name):
    # cmd_name --> 'ZTest'
    def __init__(self, ZTest):
        pass

    def toCode(self):
        return 'ZTest'


class cmd_namep75(cmd_name):
    # cmd_name --> 'ZWrite'
    def __init__(self, ZWrite):
        pass

    def toCode(self):
        return 'ZWrite'


class id_or_number_or_placeholderp76(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class id_or_number_or_placeholderp77(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class id_or_number_or_placeholderp78(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> ( Number , Number , Number , Number )
    def __init__(self, LParen, Number1, Comma1, Number2, Comma2, Number3, Comma3, Number4, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3
        self.Number4 = Number4

    def toCode(self):
        return '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ',' + self.Number3.toCode() + ',' + self.Number4.toCode() + ')'


class id_or_number_or_placeholderp79(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> placeholder
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def toCode(self):
        return self.placeholder.toCode()


class placeholderp80(placeholder):
    # placeholder --> [ ID ]
    def __init__(self, LBrack, ID, RBrack):
        self.ID = ID

    def toCode(self):
        return '[' + self.ID.toCode() + ']'


class bind_channel_stmsp81(bind_channel_stms):
    # bind_channel_stms --> bind_channel_stm bind_channel_stms
    def __init__(self, bind_channel_stm, bind_channel_stms):
        self.bind_channel_stm = bind_channel_stm
        self.bind_channel_stms = bind_channel_stms

    def toCode(self):
        return self.bind_channel_stm.toCode() + self.bind_channel_stms.toCode()


class bind_channel_stmsp82(bind_channel_stms):
    # bind_channel_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class bind_channel_stmp83(bind_channel_stm):
    # bind_channel_stm --> 'Bind' String , ID
    def __init__(self, Bind, String, Comma, ID):
        self.String = String
        self.ID = ID

    def toCode(self):
        return 'Bind' + self.String.toCode() + ',' + self.ID.toCode()


class meterial_stmsp84(meterial_stms):
    # meterial_stms --> meterial_stm meterial_stms
    def __init__(self, meterial_stm, meterial_stms):
        self.meterial_stm = meterial_stm
        self.meterial_stms = meterial_stms

    def toCode(self):
        return self.meterial_stm.toCode() + self.meterial_stms.toCode()


class meterial_stmsp85(meterial_stms):
    # meterial_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class meterial_stmp86(meterial_stm):
    # meterial_stm --> ID id_or_number_or_placeholder
    def __init__(self, ID, id_or_number_or_placeholder):
        self.ID = ID
        self.id_or_number_or_placeholder = id_or_number_or_placeholder

    def toCode(self):
        return self.ID.toCode() + self.id_or_number_or_placeholder.toCode()


class stencil_stmsp87(stencil_stms):
    # stencil_stms --> stencil_stm stencil_stms
    def __init__(self, stencil_stm, stencil_stms):
        self.stencil_stm = stencil_stm
        self.stencil_stms = stencil_stms

    def toCode(self):
        return self.stencil_stm.toCode() + self.stencil_stms.toCode()


class stencil_stmsp88(stencil_stms):
    # stencil_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class stencil_stmp89(stencil_stm):
    # stencil_stm --> ID id_or_number_or_placeholder
    def __init__(self, ID, id_or_number_or_placeholder):
        self.ID = ID
        self.id_or_number_or_placeholder = id_or_number_or_placeholder

    def toCode(self):
        return self.ID.toCode() + self.id_or_number_or_placeholder.toCode()


class set_texture_stmsp90(set_texture_stms):
    # set_texture_stms --> set_texture_stm set_texture_stms
    def __init__(self, set_texture_stm, set_texture_stms):
        self.set_texture_stm = set_texture_stm
        self.set_texture_stms = set_texture_stms

    def toCode(self):
        return self.set_texture_stm.toCode() + self.set_texture_stms.toCode()


class set_texture_stmsp91(set_texture_stms):
    # set_texture_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class set_texture_stmp92(set_texture_stm):
    # set_texture_stm --> 'matrix' placeholder
    def __init__(self, matrix, placeholder):
        self.placeholder = placeholder

    def toCode(self):
        return 'matrix' + self.placeholder.toCode()


class set_texture_stmp93(set_texture_stm):
    # set_texture_stm --> 'constantColor' id_or_number_or_placeholder
    def __init__(self, constantColor, id_or_number_or_placeholder):
        self.id_or_number_or_placeholder = id_or_number_or_placeholder

    def toCode(self):
        return 'constantColor' + self.id_or_number_or_placeholder.toCode()


class set_texture_stmp94(set_texture_stm):
    # set_texture_stm --> 'combine' combine_options
    def __init__(self, combine, combine_options):
        self.combine_options = combine_options

    def toCode(self):
        return 'combine' + self.combine_options.toCode()


class combine_optionsp95(combine_options):
    # combine_options --> combine_option combine_options
    def __init__(self, combine_option, combine_options):
        self.combine_option = combine_option
        self.combine_options = combine_options

    def toCode(self):
        return self.combine_option.toCode() + self.combine_options.toCode()


class combine_optionsp96(combine_options):
    # combine_options --> combine_option , combine_options
    def __init__(self, combine_option, Comma, combine_options):
        self.combine_option = combine_option
        self.combine_options = combine_options

    def toCode(self):
        return self.combine_option.toCode() + ',' + self.combine_options.toCode()


class combine_optionsp97(combine_options):
    # combine_options --> combine_option combine_option_op combine_options
    def __init__(self, combine_option, combine_option_op, combine_options):
        self.combine_option = combine_option
        self.combine_option_op = combine_option_op
        self.combine_options = combine_options

    def toCode(self):
        return self.combine_option.toCode() + self.combine_option_op.toCode() + self.combine_options.toCode()


class combine_optionsp98(combine_options):
    # combine_options -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class combine_optionp99(combine_option):
    # combine_option --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class combine_optionp100(combine_option):
    # combine_option --> ( ID )
    def __init__(self, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return '(' + self.ID.toCode() + ')'


class combine_option_opp101(combine_option_op):
    # combine_option_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class combine_option_opp102(combine_option_op):
    # combine_option_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class combine_option_opp103(combine_option_op):
    # combine_option_op --> *
    def __init__(self, Times):
        pass

    def toCode(self):
        return '*'


class combine_option_opp104(combine_option_op):
    # combine_option_op --> /
    def __init__(self, Divide):
        pass

    def toCode(self):
        return '/'


class tags_stmsp105(tags_stms):
    # tags_stms --> tag_smt tags_stms
    def __init__(self, tag_smt, tags_stms):
        self.tag_smt = tag_smt
        self.tags_stms = tags_stms

    def toCode(self):
        return self.tag_smt.toCode() + self.tags_stms.toCode()


class tags_stmsp106(tags_stms):
    # tags_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class tag_smtp107(tag_smt):
    # tag_smt --> String = String
    def __init__(self, String1, Assign, String2):
        self.String1 = String1
        self.String2 = String2

    def toCode(self):
        return self.String1.toCode() + '=' + self.String2.toCode()


class shr_passp108(shr_pass):
    # shr_pass --> 'Pass' { pass_body_elms }
    def __init__(self, Pass, LBrace, pass_body_elms, RBrace):
        self.pass_body_elms = pass_body_elms

    def toCode(self):
        return 'Pass' + '{' + self.pass_body_elms.toCode() + '}'


class shr_passp109(shr_pass):
    # shr_pass --> 'GrabPass' { pass_body_elms }
    def __init__(self, GrabPass, LBrace, pass_body_elms, RBrace):
        self.pass_body_elms = pass_body_elms

    def toCode(self):
        return 'GrabPass' + '{' + self.pass_body_elms.toCode() + '}'


class shr_passp110(shr_pass):
    # shr_pass --> 'UsePass' String
    def __init__(self, UsePass, String):
        self.String = String

    def toCode(self):
        return 'UsePass' + self.String.toCode()


class pass_body_elmsp111(pass_body_elms):
    # pass_body_elms --> pass_body_elm pass_body_elms
    def __init__(self, pass_body_elm, pass_body_elms):
        self.pass_body_elm = pass_body_elm
        self.pass_body_elms = pass_body_elms

    def toCode(self):
        return self.pass_body_elm.toCode() + self.pass_body_elms.toCode()


class pass_body_elmsp112(pass_body_elms):
    # pass_body_elms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class pass_body_elmp113(pass_body_elm):
    # pass_body_elm --> cmd_stm
    def __init__(self, cmd_stm):
        self.cmd_stm = cmd_stm

    def toCode(self):
        return self.cmd_stm.toCode()


class pass_body_elmp114(pass_body_elm):
    # pass_body_elm --> cg_prog
    def __init__(self, cg_prog):
        self.cg_prog = cg_prog

    def toCode(self):
        return self.cg_prog.toCode()


class cg_progp115(cg_prog):
    # cg_prog --> 'CGPROGRAM' 'ENDCG'
    def __init__(self, CGPROGRAM, ENDCG):
        pass

    def toCode(self):
        return 'CGPROGRAM' + 'ENDCG'


class cg_progp116(cg_prog):
    # cg_prog --> 'CGINCLUDE' 'ENDCG'
    def __init__(self, CGINCLUDE, ENDCG):
        pass

    def toCode(self):
        return 'CGINCLUDE' + 'ENDCG'


class fall_back_cmdp117(fall_back_cmd):
    # fall_back_cmd --> 'FallBack' String
    def __init__(self, FallBack, String):
        self.String = String

    def toCode(self):
        return 'FallBack' + self.String.toCode()


class fall_back_cmdp118(fall_back_cmd):
    # fall_back_cmd --> 'FallBack' 'Off'
    def __init__(self, FallBack, Off):
        pass

    def toCode(self):
        return 'FallBack' + 'Off'


class custom_editor_cmdp119(custom_editor_cmd):
    # custom_editor_cmd --> 'CustomEditor' String
    def __init__(self, CustomEditor, String):
        self.String = String

    def toCode(self):
        return 'CustomEditor' + self.String.toCode()


class dependency_cmdp120(dependency_cmd):
    # dependency_cmd --> 'Dependency' String = String
    def __init__(self, Dependency, String1, Assign, String2):
        self.String1 = String1
        self.String2 = String2

    def toCode(self):
        return 'Dependency' + self.String1.toCode() + '=' + self.String2.toCode()


class id_listp121(id_list):
    # id_list --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class id_listp122(id_list):
    # id_list --> ID id_list
    def __init__(self, ID, id_list):
        self.ID = ID
        self.id_list = id_list

    def toCode(self):
        return self.ID.toCode() + self.id_list.toCode()


class Test(unittest.TestCase):


    def test(self):
        pass
