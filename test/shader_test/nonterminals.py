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
    enum_item_successor = 'enum_item_successor'
    ids_with_comma = 'ids_with_comma'
    id_with_comma_successor = 'id_with_comma_successor'
    category = 'category'
    category_body_elms = 'category_body_elms'
    category_body_elm = 'category_body_elm'
    subshr = 'subshr'
    subshr_body_elms = 'subshr_body_elms'
    subshr_body_elm = 'subshr_body_elm'
    tags = 'tags'
    tags_body = 'tags_body'
    tag_smt = 'tag_smt'
    cmd_stm = 'cmd_stm'
    cmd_name = 'cmd_name'
    id_or_number_or_placeholder = 'id_or_number_or_placeholder'
    ids = 'ids'
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
    shr_pass = 'shr_pass'
    pass_body_elms = 'pass_body_elms'
    pass_body_elm = 'pass_body_elm'
    cg_prog = 'cg_prog'
    fall_back_cmd = 'fall_back_cmd'
    custom_editor_cmd = 'custom_editor_cmd'


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


class enum_item_successor(Nonterminal):
    pass


class ids_with_comma(Nonterminal):
    pass


class id_with_comma_successor(Nonterminal):
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


class tags(Nonterminal):
    pass


class tags_body(Nonterminal):
    pass


class tag_smt(Nonterminal):
    pass


class cmd_stm(Nonterminal):
    pass


class cmd_name(Nonterminal):
    pass


class id_or_number_or_placeholder(Nonterminal):
    pass


class ids(Nonterminal):
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


class propsp10(props):
    # props --> 'Properties' { props_body }
    def __init__(self, Properties, LBrace, props_body, RBrace):
        self.props_body = props_body

    def toCode(self):
        return 'Properties' + '{' + self.props_body.toCode() + '}'


class props_bodyp11(props_body):
    # props_body --> prop_stm props_body
    def __init__(self, prop_stm, props_body):
        self.prop_stm = prop_stm
        self.props_body = props_body

    def toCode(self):
        return self.prop_stm.toCode() + self.props_body.toCode()


class props_bodyp12(props_body):
    # props_body -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class prop_stmp13(prop_stm):
    # prop_stm --> ID ( String , prop_type ) = prop_init
    def __init__(self, ID, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp14(prop_stm):
    # prop_stm --> [ ID ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, ID1, RBrack, ID2, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID1 = ID1
        self.ID2 = ID2
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + self.ID1.toCode() + ']' + self.ID2.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp15(prop_stm):
    # prop_stm --> [ 'Enum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, Enum, LParen1, enum_items, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.enum_items = enum_items
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'Enum' + '(' + self.enum_items.toCode() + ')' + ']' + self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp16(prop_stm):
    # prop_stm --> [ 'MaterialEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, MaterialEnum, LParen1, enum_items, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.enum_items = enum_items
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'MaterialEnum' + '(' + self.enum_items.toCode() + ')' + ']' + self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_stmp17(prop_stm):
    # prop_stm --> [ 'KeywordEnum' ( ids_with_comma ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, KeywordEnum, LParen1, ids_with_comma, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.ids_with_comma = ids_with_comma
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init

    def toCode(self):
        return '[' + 'KeywordEnum' + '(' + self.ids_with_comma.toCode() + ')' + ']' + self.ID.toCode() + '(' + self.String.toCode() + ',' + self.prop_type.toCode() + ')' + '=' + self.prop_init.toCode()


class prop_typep18(prop_type):
    # prop_type --> 'Color'
    def __init__(self, Color):
        pass

    def toCode(self):
        return 'Color'


class prop_typep19(prop_type):
    # prop_type --> 'Vector'
    def __init__(self, Vector):
        pass

    def toCode(self):
        return 'Vector'


class prop_typep20(prop_type):
    # prop_type --> 'Range'
    def __init__(self, Range):
        pass

    def toCode(self):
        return 'Range'


class prop_typep21(prop_type):
    # prop_type --> 'Int'
    def __init__(self, Int):
        pass

    def toCode(self):
        return 'Int'


class prop_typep22(prop_type):
    # prop_type --> 'Float'
    def __init__(self, Float):
        pass

    def toCode(self):
        return 'Float'


class prop_typep23(prop_type):
    # prop_type --> '2D'
    def __init__(self, _2D):
        pass

    def toCode(self):
        return '2D'


class prop_typep24(prop_type):
    # prop_type --> 'Cube'
    def __init__(self, Cube):
        pass

    def toCode(self):
        return 'Cube'


class prop_typep25(prop_type):
    # prop_type --> '3D'
    def __init__(self, _3D):
        pass

    def toCode(self):
        return '3D'


class prop_typep26(prop_type):
    # prop_type --> 'Any'
    def __init__(self, Any):
        pass

    def toCode(self):
        return 'Any'


class prop_typep27(prop_type):
    # prop_type --> 'Range' ( Number , Number )
    def __init__(self, Range, LParen, Number1, Comma, Number2, RParen):
        self.Number1 = Number1
        self.Number2 = Number2

    def toCode(self):
        return 'Range' + '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ')'


class prop_initp28(prop_init):
    # prop_init --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class prop_initp29(prop_init):
    # prop_init --> String { }
    def __init__(self, String, LBrace, RBrace):
        self.String = String

    def toCode(self):
        return self.String.toCode() + '{' + '}'


class prop_initp30(prop_init):
    # prop_init --> String { ID }
    def __init__(self, String, LBrace, ID, RBrace):
        self.String = String
        self.ID = ID

    def toCode(self):
        return self.String.toCode() + '{' + self.ID.toCode() + '}'


class prop_initp31(prop_init):
    # prop_init --> ( Number , Number , Number )
    def __init__(self, LParen, Number1, Comma1, Number2, Comma2, Number3, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3

    def toCode(self):
        return '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ',' + self.Number3.toCode() + ')'


class prop_initp32(prop_init):
    # prop_init --> ( Number , Number , Number , Number )
    def __init__(self, LParen, Number1, Comma1, Number2, Comma2, Number3, Comma3, Number4, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3
        self.Number4 = Number4

    def toCode(self):
        return '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ',' + self.Number3.toCode() + ',' + self.Number4.toCode() + ')'


class enum_itemsp33(enum_items):
    # enum_items --> enum_item enum_item_successor
    def __init__(self, enum_item, enum_item_successor):
        self.enum_item = enum_item
        self.enum_item_successor = enum_item_successor

    def toCode(self):
        return self.enum_item.toCode() + self.enum_item_successor.toCode()


class enum_itemp34(enum_item):
    # enum_item --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class enum_itemp35(enum_item):
    # enum_item --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class enum_item_successorp36(enum_item_successor):
    # enum_item_successor --> , enum_item
    def __init__(self, Comma, enum_item):
        self.enum_item = enum_item

    def toCode(self):
        return ',' + self.enum_item.toCode()


class enum_item_successorp37(enum_item_successor):
    # enum_item_successor --> , enum_item enum_item_successor
    def __init__(self, Comma, enum_item, enum_item_successor):
        self.enum_item = enum_item
        self.enum_item_successor = enum_item_successor

    def toCode(self):
        return ',' + self.enum_item.toCode() + self.enum_item_successor.toCode()


class enum_item_successorp38(enum_item_successor):
    # enum_item_successor -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class ids_with_commap39(ids_with_comma):
    # ids_with_comma --> ids id_with_comma_successor
    def __init__(self, ids, id_with_comma_successor):
        self.ids = ids
        self.id_with_comma_successor = id_with_comma_successor

    def toCode(self):
        return self.ids.toCode() + self.id_with_comma_successor.toCode()


class id_with_comma_successorp40(id_with_comma_successor):
    # id_with_comma_successor --> , ids
    def __init__(self, Comma, ids):
        self.ids = ids

    def toCode(self):
        return ',' + self.ids.toCode()


class id_with_comma_successorp41(id_with_comma_successor):
    # id_with_comma_successor --> , ids id_with_comma_successor
    def __init__(self, Comma, ids, id_with_comma_successor):
        self.ids = ids
        self.id_with_comma_successor = id_with_comma_successor

    def toCode(self):
        return ',' + self.ids.toCode() + self.id_with_comma_successor.toCode()


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
    # category_body_elm --> tags
    def __init__(self, tags):
        self.tags = tags

    def toCode(self):
        return self.tags.toCode()


class category_body_elmp46(category_body_elm):
    # category_body_elm --> cmd_stm
    def __init__(self, cmd_stm):
        self.cmd_stm = cmd_stm

    def toCode(self):
        return self.cmd_stm.toCode()


class category_body_elmp47(category_body_elm):
    # category_body_elm --> subshr
    def __init__(self, subshr):
        self.subshr = subshr

    def toCode(self):
        return self.subshr.toCode()


class subshrp48(subshr):
    # subshr --> 'SubShader' { subshr_body_elms }
    def __init__(self, SubShader, LBrace, subshr_body_elms, RBrace):
        self.subshr_body_elms = subshr_body_elms

    def toCode(self):
        return 'SubShader' + '{' + self.subshr_body_elms.toCode() + '}'


class subshr_body_elmsp49(subshr_body_elms):
    # subshr_body_elms --> subshr_body_elm subshr_body_elms
    def __init__(self, subshr_body_elm, subshr_body_elms):
        self.subshr_body_elm = subshr_body_elm
        self.subshr_body_elms = subshr_body_elms

    def toCode(self):
        return self.subshr_body_elm.toCode() + self.subshr_body_elms.toCode()


class subshr_body_elmsp50(subshr_body_elms):
    # subshr_body_elms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class subshr_body_elmp51(subshr_body_elm):
    # subshr_body_elm --> tags
    def __init__(self, tags):
        self.tags = tags

    def toCode(self):
        return self.tags.toCode()


class subshr_body_elmp52(subshr_body_elm):
    # subshr_body_elm --> cmd_stm
    def __init__(self, cmd_stm):
        self.cmd_stm = cmd_stm

    def toCode(self):
        return self.cmd_stm.toCode()


class subshr_body_elmp53(subshr_body_elm):
    # subshr_body_elm --> shr_pass
    def __init__(self, shr_pass):
        self.shr_pass = shr_pass

    def toCode(self):
        return self.shr_pass.toCode()


class subshr_body_elmp54(subshr_body_elm):
    # subshr_body_elm --> cg_prog
    def __init__(self, cg_prog):
        self.cg_prog = cg_prog

    def toCode(self):
        return self.cg_prog.toCode()


class tagsp55(tags):
    # tags --> 'Tags' { tags_body }
    def __init__(self, Tags, LBrace, tags_body, RBrace):
        self.tags_body = tags_body

    def toCode(self):
        return 'Tags' + '{' + self.tags_body.toCode() + '}'


class tags_bodyp56(tags_body):
    # tags_body --> tag_smt tags_body
    def __init__(self, tag_smt, tags_body):
        self.tag_smt = tag_smt
        self.tags_body = tags_body

    def toCode(self):
        return self.tag_smt.toCode() + self.tags_body.toCode()


class tags_bodyp57(tags_body):
    # tags_body -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class tag_smtp58(tag_smt):
    # tag_smt --> String = String
    def __init__(self, key, Assign, value):
        self.key = key
        self.value = value

    def toCode(self):
        return self.key.toCode() + '=' + self.value.toCode()


class cmd_stmp59(cmd_stm):
    # cmd_stm --> cmd_name id_or_number_or_placeholder
    def __init__(self, cmd_name, id_or_number_or_placeholder):
        self.cmd_name = cmd_name
        self.id_or_number_or_placeholder = id_or_number_or_placeholder

    def toCode(self):
        return self.cmd_name.toCode() + self.id_or_number_or_placeholder.toCode()


class cmd_stmp60(cmd_stm):
    # cmd_stm --> 'Alphatest' ID placeholder
    def __init__(self, Alphatest, ID, placeholder):
        self.ID = ID
        self.placeholder = placeholder

    def toCode(self):
        return 'Alphatest' + self.ID.toCode() + self.placeholder.toCode()


class cmd_stmp61(cmd_stm):
    # cmd_stm --> 'BindChannels' { bind_channel_stms }
    def __init__(self, BindChannels, LBrace, bind_channel_stms, RBrace):
        self.bind_channel_stms = bind_channel_stms

    def toCode(self):
        return 'BindChannels' + '{' + self.bind_channel_stms.toCode() + '}'


class cmd_stmp62(cmd_stm):
    # cmd_stm --> 'Blend' id_or_number_or_placeholder id_or_number_or_placeholder
    def __init__(self, Blend, id_or_number_or_placeholder1, id_or_number_or_placeholder2):
        self.id_or_number_or_placeholder1 = id_or_number_or_placeholder1
        self.id_or_number_or_placeholder2 = id_or_number_or_placeholder2

    def toCode(self):
        return 'Blend' + self.id_or_number_or_placeholder1.toCode() + self.id_or_number_or_placeholder2.toCode()


class cmd_stmp63(cmd_stm):
    # cmd_stm --> 'Material' { meterial_stms }
    def __init__(self, Material, LBrace, meterial_stms, RBrace):
        self.meterial_stms = meterial_stms

    def toCode(self):
        return 'Material' + '{' + self.meterial_stms.toCode() + '}'


class cmd_stmp64(cmd_stm):
    # cmd_stm --> 'Name' String
    def __init__(self, Name, String):
        self.String = String

    def toCode(self):
        return 'Name' + self.String.toCode()


class cmd_stmp65(cmd_stm):
    # cmd_stm --> 'Offset' id_or_number_or_placeholder , id_or_number_or_placeholder
    def __init__(self, Offset, id_or_number_or_placeholder1, Comma, id_or_number_or_placeholder2):
        self.id_or_number_or_placeholder1 = id_or_number_or_placeholder1
        self.id_or_number_or_placeholder2 = id_or_number_or_placeholder2

    def toCode(self):
        return 'Offset' + self.id_or_number_or_placeholder1.toCode() + ',' + self.id_or_number_or_placeholder2.toCode()


class cmd_stmp66(cmd_stm):
    # cmd_stm --> 'Stencil' { stencil_stms }
    def __init__(self, Stencil, LBrace, stencil_stms, RBrace):
        self.stencil_stms = stencil_stms

    def toCode(self):
        return 'Stencil' + '{' + self.stencil_stms.toCode() + '}'


class cmd_stmp67(cmd_stm):
    # cmd_stm --> 'SetTexture' placeholder { set_texture_stms }
    def __init__(self, SetTexture, placeholder, LBrace, set_texture_stms, RBrace):
        self.placeholder = placeholder
        self.set_texture_stms = set_texture_stms

    def toCode(self):
        return 'SetTexture' + self.placeholder.toCode() + '{' + self.set_texture_stms.toCode() + '}'


class cmd_namep68(cmd_name):
    # cmd_name --> 'AlphaToMask'
    def __init__(self, AlphaToMask):
        pass

    def toCode(self):
        return 'AlphaToMask'


class cmd_namep69(cmd_name):
    # cmd_name --> 'ColorMask'
    def __init__(self, ColorMask):
        pass

    def toCode(self):
        return 'ColorMask'


class cmd_namep70(cmd_name):
    # cmd_name --> 'ColorMaterial'
    def __init__(self, ColorMaterial):
        pass

    def toCode(self):
        return 'ColorMaterial'


class cmd_namep71(cmd_name):
    # cmd_name --> 'Cull'
    def __init__(self, Cull):
        pass

    def toCode(self):
        return 'Cull'


class cmd_namep72(cmd_name):
    # cmd_name --> 'Lighting'
    def __init__(self, Lighting):
        pass

    def toCode(self):
        return 'Lighting'


class cmd_namep73(cmd_name):
    # cmd_name --> 'LOD'
    def __init__(self, LOD):
        pass

    def toCode(self):
        return 'LOD'


class cmd_namep74(cmd_name):
    # cmd_name --> 'SeparateSpecular'
    def __init__(self, SeparateSpecular):
        pass

    def toCode(self):
        return 'SeparateSpecular'


class cmd_namep75(cmd_name):
    # cmd_name --> 'ZTest'
    def __init__(self, ZTest):
        pass

    def toCode(self):
        return 'ZTest'


class cmd_namep76(cmd_name):
    # cmd_name --> 'ZWrite'
    def __init__(self, ZWrite):
        pass

    def toCode(self):
        return 'ZWrite'


class id_or_number_or_placeholderp77(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class id_or_number_or_placeholderp78(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class id_or_number_or_placeholderp79(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> placeholder
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def toCode(self):
        return self.placeholder.toCode()


class idsp80(ids):
    # ids --> ID ids
    def __init__(self, ID, ids):
        self.ID = ID
        self.ids = ids

    def toCode(self):
        return self.ID.toCode() + self.ids.toCode()


class idsp81(ids):
    # ids -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class placeholderp82(placeholder):
    # placeholder --> [ ID ]
    def __init__(self, LBrack, ID, RBrack):
        self.ID = ID

    def toCode(self):
        return '[' + self.ID.toCode() + ']'


class bind_channel_stmsp83(bind_channel_stms):
    # bind_channel_stms --> bind_channel_stm bind_channel_stms
    def __init__(self, bind_channel_stm, bind_channel_stms):
        self.bind_channel_stm = bind_channel_stm
        self.bind_channel_stms = bind_channel_stms

    def toCode(self):
        return self.bind_channel_stm.toCode() + self.bind_channel_stms.toCode()


class bind_channel_stmsp84(bind_channel_stms):
    # bind_channel_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class bind_channel_stmp85(bind_channel_stm):
    # bind_channel_stm --> 'Bind' String , ID
    def __init__(self, Bind, String, Comma, ID):
        self.String = String
        self.ID = ID

    def toCode(self):
        return 'Bind' + self.String.toCode() + ',' + self.ID.toCode()


class meterial_stmsp86(meterial_stms):
    # meterial_stms --> meterial_stm meterial_stms
    def __init__(self, meterial_stm, meterial_stms):
        self.meterial_stm = meterial_stm
        self.meterial_stms = meterial_stms

    def toCode(self):
        return self.meterial_stm.toCode() + self.meterial_stms.toCode()


class meterial_stmsp87(meterial_stms):
    # meterial_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class meterial_stmp88(meterial_stm):
    # meterial_stm --> ID id_or_number_or_placeholder
    def __init__(self, ID, id_or_number_or_placeholder):
        self.ID = ID
        self.id_or_number_or_placeholder = id_or_number_or_placeholder

    def toCode(self):
        return self.ID.toCode() + self.id_or_number_or_placeholder.toCode()


class stencil_stmsp89(stencil_stms):
    # stencil_stms --> stencil_stm stencil_stms
    def __init__(self, stencil_stm, stencil_stms):
        self.stencil_stm = stencil_stm
        self.stencil_stms = stencil_stms

    def toCode(self):
        return self.stencil_stm.toCode() + self.stencil_stms.toCode()


class stencil_stmsp90(stencil_stms):
    # stencil_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class stencil_stmp91(stencil_stm):
    # stencil_stm --> ID id_or_number_or_placeholder
    def __init__(self, ID, id_or_number_or_placeholder):
        self.ID = ID
        self.id_or_number_or_placeholder = id_or_number_or_placeholder

    def toCode(self):
        return self.ID.toCode() + self.id_or_number_or_placeholder.toCode()


class set_texture_stmsp92(set_texture_stms):
    # set_texture_stms --> set_texture_stm set_texture_stms
    def __init__(self, set_texture_stm, set_texture_stms):
        self.set_texture_stm = set_texture_stm
        self.set_texture_stms = set_texture_stms

    def toCode(self):
        return self.set_texture_stm.toCode() + self.set_texture_stms.toCode()


class set_texture_stmsp93(set_texture_stms):
    # set_texture_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class set_texture_stmp94(set_texture_stm):
    # set_texture_stm --> 'matrix' placeholder
    def __init__(self, matrix, placeholder):
        self.placeholder = placeholder

    def toCode(self):
        return 'matrix' + self.placeholder.toCode()


class set_texture_stmp95(set_texture_stm):
    # set_texture_stm --> 'constantColor' placeholder
    def __init__(self, constantColor, placeholder):
        self.placeholder = placeholder

    def toCode(self):
        return 'constantColor' + self.placeholder.toCode()


class set_texture_stmp96(set_texture_stm):
    # set_texture_stm --> 'constantColor' ( Number , Number , Number , Number )
    def __init__(self, constantColor, LParen, Number1, Comma1, Number2, Comma2, Number3, Comma3, Number4, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3
        self.Number4 = Number4

    def toCode(self):
        return 'constantColor' + '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ',' + self.Number3.toCode() + ',' + self.Number4.toCode() + ')'


class set_texture_stmp97(set_texture_stm):
    # set_texture_stm --> 'combine' combine_options
    def __init__(self, combine, combine_options):
        self.combine_options = combine_options

    def toCode(self):
        return 'combine' + self.combine_options.toCode()


class combine_optionsp98(combine_options):
    # combine_options --> combine_option combine_options
    def __init__(self, combine_option, combine_options):
        self.combine_option = combine_option
        self.combine_options = combine_options

    def toCode(self):
        return self.combine_option.toCode() + self.combine_options.toCode()


class combine_optionsp99(combine_options):
    # combine_options --> combine_option , combine_options
    def __init__(self, combine_option, Comma, combine_options):
        self.combine_option = combine_option
        self.combine_options = combine_options

    def toCode(self):
        return self.combine_option.toCode() + ',' + self.combine_options.toCode()


class combine_optionsp100(combine_options):
    # combine_options --> combine_option combine_option_op combine_options
    def __init__(self, combine_option, combine_option_op, combine_options):
        self.combine_option = combine_option
        self.combine_option_op = combine_option_op
        self.combine_options = combine_options

    def toCode(self):
        return self.combine_option.toCode() + self.combine_option_op.toCode() + self.combine_options.toCode()


class combine_optionsp101(combine_options):
    # combine_options -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class combine_optionp102(combine_option):
    # combine_option --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class combine_optionp103(combine_option):
    # combine_option --> ( ID )
    def __init__(self, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return '(' + self.ID.toCode() + ')'


class combine_option_opp104(combine_option_op):
    # combine_option_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class combine_option_opp105(combine_option_op):
    # combine_option_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class combine_option_opp106(combine_option_op):
    # combine_option_op --> *
    def __init__(self, Times):
        pass

    def toCode(self):
        return '*'


class combine_option_opp107(combine_option_op):
    # combine_option_op --> /
    def __init__(self, Divide):
        pass

    def toCode(self):
        return '/'


class shr_passp108(shr_pass):
    # shr_pass --> 'Pass' { pass_body_elms }
    def __init__(self, Pass, LBrace, pass_body_elms, RBrace):
        self.pass_body_elms = pass_body_elms

    def toCode(self):
        return 'Pass' + '{' + self.pass_body_elms.toCode() + '}'


class shr_passp109(shr_pass):
    # shr_pass --> 'UsePass' String
    def __init__(self, UsePass, String):
        self.String = String

    def toCode(self):
        return 'UsePass' + self.String.toCode()


class pass_body_elmsp110(pass_body_elms):
    # pass_body_elms --> pass_body_elm pass_body_elms
    def __init__(self, pass_body_elm, pass_body_elms):
        self.pass_body_elm = pass_body_elm
        self.pass_body_elms = pass_body_elms

    def toCode(self):
        return self.pass_body_elm.toCode() + self.pass_body_elms.toCode()


class pass_body_elmsp111(pass_body_elms):
    # pass_body_elms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class pass_body_elmp112(pass_body_elm):
    # pass_body_elm --> tags
    def __init__(self, tags):
        self.tags = tags

    def toCode(self):
        return self.tags.toCode()


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


class Test(unittest.TestCase):


    def test(self):
        pass
