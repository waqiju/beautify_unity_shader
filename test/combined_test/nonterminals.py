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
    cg_prog_body = 'cg_prog_body'
    cg_stms = 'cg_stms'
    cg_stm = 'cg_stm'
    function_definition = 'function_definition'
    preprocessing_stm = 'preprocessing_stm'
    pp_if_stm = 'pp_if_stm'
    pp_cmd = 'pp_cmd'
    marco_unfold = 'marco_unfold'
    dec_list = 'dec_list'
    primary_exp = 'primary_exp'
    postfix_exp = 'postfix_exp'
    argument_exp_list = 'argument_exp_list'
    unary_exp = 'unary_exp'
    unary_op = 'unary_op'
    cast_exp = 'cast_exp'
    binary_exp = 'binary_exp'
    binary_op = 'binary_op'
    conditional_exp = 'conditional_exp'
    assignment_exp = 'assignment_exp'
    assignment_op = 'assignment_op'
    exp = 'exp'
    dec = 'dec'
    dec_specifier = 'dec_specifier'
    type_specifier = 'type_specifier'
    buildin_type_name = 'buildin_type_name'
    type_qualifier = 'type_qualifier'
    storage_class_specifier = 'storage_class_specifier'
    typedef_name = 'typedef_name'
    struct_specifier = 'struct_specifier'
    struct_dec_list = 'struct_dec_list'
    struct_dec = 'struct_dec'
    struct_declarator_list = 'struct_declarator_list'
    struct_declarator = 'struct_declarator'
    declarator = 'declarator'
    parameter_list = 'parameter_list'
    parameter_dec = 'parameter_dec'
    parameter_dec_specifier = 'parameter_dec_specifier'
    init_dec_list = 'init_dec_list'
    init_dec = 'init_dec'
    initializer = 'initializer'
    initializer_list = 'initializer_list'
    stm = 'stm'
    exp_stm = 'exp_stm'
    compound_stm = 'compound_stm'
    block_item_list = 'block_item_list'
    block_item = 'block_item'
    selection_stm = 'selection_stm'
    iteration_stm = 'iteration_stm'
    jump_stm = 'jump_stm'


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


class cg_prog_body(Nonterminal):
    pass


class cg_stms(Nonterminal):
    pass


class cg_stm(Nonterminal):
    pass


class function_definition(Nonterminal):
    pass


class preprocessing_stm(Nonterminal):
    pass


class pp_if_stm(Nonterminal):
    pass


class pp_cmd(Nonterminal):
    pass


class marco_unfold(Nonterminal):
    pass


class dec_list(Nonterminal):
    pass


class primary_exp(Nonterminal):
    pass


class postfix_exp(Nonterminal):
    pass


class argument_exp_list(Nonterminal):
    pass


class unary_exp(Nonterminal):
    pass


class unary_op(Nonterminal):
    pass


class cast_exp(Nonterminal):
    pass


class binary_exp(Nonterminal):
    pass


class binary_op(Nonterminal):
    pass


class conditional_exp(Nonterminal):
    pass


class assignment_exp(Nonterminal):
    pass


class assignment_op(Nonterminal):
    pass


class exp(Nonterminal):
    pass


class dec(Nonterminal):
    pass


class dec_specifier(Nonterminal):
    pass


class type_specifier(Nonterminal):
    pass


class buildin_type_name(Nonterminal):
    pass


class type_qualifier(Nonterminal):
    pass


class storage_class_specifier(Nonterminal):
    pass


class typedef_name(Nonterminal):
    pass


class struct_specifier(Nonterminal):
    pass


class struct_dec_list(Nonterminal):
    pass


class struct_dec(Nonterminal):
    pass


class struct_declarator_list(Nonterminal):
    pass


class struct_declarator(Nonterminal):
    pass


class declarator(Nonterminal):
    pass


class parameter_list(Nonterminal):
    pass


class parameter_dec(Nonterminal):
    pass


class parameter_dec_specifier(Nonterminal):
    pass


class init_dec_list(Nonterminal):
    pass


class init_dec(Nonterminal):
    pass


class initializer(Nonterminal):
    pass


class initializer_list(Nonterminal):
    pass


class stm(Nonterminal):
    pass


class exp_stm(Nonterminal):
    pass


class compound_stm(Nonterminal):
    pass


class block_item_list(Nonterminal):
    pass


class block_item(Nonterminal):
    pass


class selection_stm(Nonterminal):
    pass


class iteration_stm(Nonterminal):
    pass


class jump_stm(Nonterminal):
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
    def __init__(self, _2D):
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
    def __init__(self, _3D):
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
    # cg_prog --> 'CGPROGRAM' cg_prog_body 'ENDCG'
    def __init__(self, CGPROGRAM, cg_prog_body, ENDCG):
        self.cg_prog_body = cg_prog_body

    def toCode(self):
        return 'CGPROGRAM' + self.cg_prog_body.toCode() + 'ENDCG'


class cg_progp116(cg_prog):
    # cg_prog --> 'CGINCLUDE' cg_prog_body 'ENDCG'
    def __init__(self, CGINCLUDE, cg_prog_body, ENDCG):
        self.cg_prog_body = cg_prog_body

    def toCode(self):
        return 'CGINCLUDE' + self.cg_prog_body.toCode() + 'ENDCG'


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


class cg_prog_bodyp123(cg_prog_body):
    # cg_prog_body --> cg_stms
    def __init__(self, cg_stms):
        self.cg_stms = cg_stms

    def toCode(self):
        return self.cg_stms.toCode()


class cg_stmsp124(cg_stms):
    # cg_stms --> cg_stm cg_stms
    def __init__(self, cg_stm, cg_stms):
        self.cg_stm = cg_stm
        self.cg_stms = cg_stms

    def toCode(self):
        return self.cg_stm.toCode() + self.cg_stms.toCode()


class cg_stmsp125(cg_stms):
    # cg_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class cg_stmp126(cg_stm):
    # cg_stm --> preprocessing_stm
    def __init__(self, preprocessing_stm):
        self.preprocessing_stm = preprocessing_stm

    def toCode(self):
        return self.preprocessing_stm.toCode()


class cg_stmp127(cg_stm):
    # cg_stm --> function_definition
    def __init__(self, function_definition):
        self.function_definition = function_definition

    def toCode(self):
        return self.function_definition.toCode()


class cg_stmp128(cg_stm):
    # cg_stm --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class cg_stmp129(cg_stm):
    # cg_stm --> 'CBUFFER_START' ( ID ) dec_list 'CBUFFER_END'
    def __init__(self, CBUFFER_START, LParen, ID, RParen, dec_list, CBUFFER_END):
        self.ID = ID
        self.dec_list = dec_list

    def toCode(self):
        return 'CBUFFER_START' + '(' + self.ID.toCode() + ')' + self.dec_list.toCode() + 'CBUFFER_END'


class function_definitionp130(function_definition):
    # function_definition --> dec_specifier declarator compound_stm
    def __init__(self, dec_specifier, declarator, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm

    def toCode(self):
        return self.dec_specifier.toCode() + self.declarator.toCode() + self.compound_stm.toCode()


class function_definitionp131(function_definition):
    # function_definition --> dec_specifier declarator : ID compound_stm
    def __init__(self, dec_specifier, declarator, Colon, ID, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID = ID
        self.compound_stm = compound_stm

    def toCode(self):
        return self.dec_specifier.toCode() + self.declarator.toCode() + ':' + self.ID.toCode() + self.compound_stm.toCode()


class function_definitionp132(function_definition):
    # function_definition --> [ ID ( Number ) ] dec_specifier declarator compound_stm
    def __init__(self, LBrack, ID, LParen, Number, RParen, RBrack, dec_specifier, declarator, compound_stm):
        self.ID = ID
        self.Number = Number
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm

    def toCode(self):
        return '[' + self.ID.toCode() + '(' + self.Number.toCode() + ')' + ']' + self.dec_specifier.toCode() + self.declarator.toCode() + self.compound_stm.toCode()


class function_definitionp133(function_definition):
    # function_definition --> [ ID ( Number ) ] dec_specifier declarator : ID compound_stm
    def __init__(self, LBrack, ID1, LParen, Number, RParen, RBrack, dec_specifier, declarator, Colon, ID2, compound_stm):
        self.ID1 = ID1
        self.Number = Number
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID2 = ID2
        self.compound_stm = compound_stm

    def toCode(self):
        return '[' + self.ID1.toCode() + '(' + self.Number.toCode() + ')' + ']' + self.dec_specifier.toCode() + self.declarator.toCode() + ':' + self.ID2.toCode() + self.compound_stm.toCode()


class preprocessing_stmp134(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class preprocessing_stmp135(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd

    def toCode(self):
        return self.pp_cmd.toCode()


class preprocessing_stmp136(preprocessing_stm):
    # preprocessing_stm --> marco_unfold
    def __init__(self, marco_unfold):
        self.marco_unfold = marco_unfold

    def toCode(self):
        return self.marco_unfold.toCode()


class pp_if_stmp137(pp_if_stm):
    # pp_if_stm --> # 'if' PPTokens
    def __init__(self, Pound, _if, PPTokens):
        self.PPTokens = PPTokens

    def toCode(self):
        return '#' + 'if' + self.PPTokens.toCode()


class pp_if_stmp138(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'ifdef' + self.ID.toCode()


class pp_if_stmp139(pp_if_stm):
    # pp_if_stm --> # 'ifndef' ID
    def __init__(self, Pound, ifndef, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'ifndef' + self.ID.toCode()


class pp_if_stmp140(pp_if_stm):
    # pp_if_stm --> # 'elif' PPTokens
    def __init__(self, Pound, _elif, PPTokens):
        self.PPTokens = PPTokens

    def toCode(self):
        return '#' + 'elif' + self.PPTokens.toCode()


class pp_if_stmp141(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, _else):
        pass

    def toCode(self):
        return '#' + 'else'


class pp_if_stmp142(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass

    def toCode(self):
        return '#' + 'endif'


class pp_cmdp143(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String

    def toCode(self):
        return '#' + 'include' + self.String.toCode()


class pp_cmdp144(pp_cmd):
    # pp_cmd --> # 'pragma' PPTokens
    def __init__(self, Pound, pragma, PPTokens):
        self.PPTokens = PPTokens

    def toCode(self):
        return '#' + 'pragma' + self.PPTokens.toCode()


class pp_cmdp145(pp_cmd):
    # pp_cmd --> # 'define' PPTokens
    def __init__(self, Pound, define, PPTokens):
        self.PPTokens = PPTokens

    def toCode(self):
        return '#' + 'define' + self.PPTokens.toCode()


class marco_unfoldp146(marco_unfold):
    # marco_unfold --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return self.exp.toCode() + ';'


class dec_listp147(dec_list):
    # dec_list --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class dec_listp148(dec_list):
    # dec_list --> dec_list dec
    def __init__(self, dec_list, dec):
        self.dec_list = dec_list
        self.dec = dec

    def toCode(self):
        return self.dec_list.toCode() + self.dec.toCode()


class primary_expp149(primary_exp):
    # primary_exp --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class primary_expp150(primary_exp):
    # primary_exp --> String
    def __init__(self, String):
        self.String = String

    def toCode(self):
        return self.String.toCode()


class primary_expp151(primary_exp):
    # primary_exp --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class primary_expp152(primary_exp):
    # primary_exp --> ( exp )
    def __init__(self, LParen, exp, RParen):
        self.exp = exp

    def toCode(self):
        return '(' + self.exp.toCode() + ')'


class postfix_expp153(postfix_exp):
    # postfix_exp --> primary_exp
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def toCode(self):
        return self.primary_exp.toCode()


class postfix_expp154(postfix_exp):
    # postfix_exp --> postfix_exp [ exp ]
    def __init__(self, postfix_exp, LBrack, exp, RBrack):
        self.postfix_exp = postfix_exp
        self.exp = exp

    def toCode(self):
        return self.postfix_exp.toCode() + '[' + self.exp.toCode() + ']'


class postfix_expp155(postfix_exp):
    # postfix_exp --> postfix_exp ( )
    def __init__(self, postfix_exp, LParen, RParen):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '(' + ')'


class postfix_expp156(postfix_exp):
    # postfix_exp --> postfix_exp ( argument_exp_list )
    def __init__(self, postfix_exp, LParen, argument_exp_list, RParen):
        self.postfix_exp = postfix_exp
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return self.postfix_exp.toCode() + '(' + self.argument_exp_list.toCode() + ')'


class postfix_expp157(postfix_exp):
    # postfix_exp --> buildin_type_name ( argument_exp_list )
    def __init__(self, buildin_type_name, LParen, argument_exp_list, RParen):
        self.buildin_type_name = buildin_type_name
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return self.buildin_type_name.toCode() + '(' + self.argument_exp_list.toCode() + ')'


class postfix_expp158(postfix_exp):
    # postfix_exp --> postfix_exp . ID
    def __init__(self, postfix_exp, Dot, ID):
        self.postfix_exp = postfix_exp
        self.ID = ID

    def toCode(self):
        return self.postfix_exp.toCode() + '.' + self.ID.toCode()


class postfix_expp159(postfix_exp):
    # postfix_exp --> postfix_exp ++
    def __init__(self, postfix_exp, Increment):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '++'


class postfix_expp160(postfix_exp):
    # postfix_exp --> postfix_exp --
    def __init__(self, postfix_exp, Decrement):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '--'


class argument_exp_listp161(argument_exp_list):
    # argument_exp_list --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class argument_exp_listp162(argument_exp_list):
    # argument_exp_list --> argument_exp_list , assignment_exp
    def __init__(self, argument_exp_list, Comma, assignment_exp):
        self.argument_exp_list = argument_exp_list
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.argument_exp_list.toCode() + ',' + self.assignment_exp.toCode()


class unary_expp163(unary_exp):
    # unary_exp --> postfix_exp
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode()


class unary_expp164(unary_exp):
    # unary_exp --> ++ unary_exp
    def __init__(self, Increment, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return '++' + self.unary_exp.toCode()


class unary_expp165(unary_exp):
    # unary_exp --> -- unary_exp
    def __init__(self, Decrement, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return '--' + self.unary_exp.toCode()


class unary_expp166(unary_exp):
    # unary_exp --> unary_op unary_exp
    def __init__(self, unary_op, unary_exp):
        self.unary_op = unary_op
        self.unary_exp = unary_exp

    def toCode(self):
        return self.unary_op.toCode() + self.unary_exp.toCode()


class unary_opp167(unary_op):
    # unary_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class unary_opp168(unary_op):
    # unary_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class unary_opp169(unary_op):
    # unary_op --> !
    def __init__(self, NOT):
        pass

    def toCode(self):
        return '!'


class unary_opp170(unary_op):
    # unary_op --> ~
    def __init__(self, Tilde):
        pass

    def toCode(self):
        return '~'


class cast_expp171(cast_exp):
    # cast_exp --> unary_exp
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return self.unary_exp.toCode()


class cast_expp172(cast_exp):
    # cast_exp --> ( buildin_type_name ) cast_exp
    def __init__(self, LParen, buildin_type_name, RParen, cast_exp):
        self.buildin_type_name = buildin_type_name
        self.cast_exp = cast_exp

    def toCode(self):
        return '(' + self.buildin_type_name.toCode() + ')' + self.cast_exp.toCode()


class binary_expp173(binary_exp):
    # binary_exp --> cast_exp
    def __init__(self, cast_exp):
        self.cast_exp = cast_exp

    def toCode(self):
        return self.cast_exp.toCode()


class binary_expp174(binary_exp):
    # binary_exp --> binary_exp binary_op unary_exp
    def __init__(self, binary_exp, binary_op, unary_exp):
        self.binary_exp = binary_exp
        self.binary_op = binary_op
        self.unary_exp = unary_exp

    def toCode(self):
        return self.binary_exp.toCode() + self.binary_op.toCode() + self.unary_exp.toCode()


class binary_opp175(binary_op):
    # binary_op --> *
    def __init__(self, Times):
        pass

    def toCode(self):
        return '*'


class binary_opp176(binary_op):
    # binary_op --> /
    def __init__(self, Divide):
        pass

    def toCode(self):
        return '/'


class binary_opp177(binary_op):
    # binary_op --> %
    def __init__(self, Percent):
        pass

    def toCode(self):
        return '%'


class binary_opp178(binary_op):
    # binary_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class binary_opp179(binary_op):
    # binary_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class binary_opp180(binary_op):
    # binary_op --> <<
    def __init__(self, LeftShift):
        pass

    def toCode(self):
        return '<<'


class binary_opp181(binary_op):
    # binary_op --> >>
    def __init__(self, RightShift):
        pass

    def toCode(self):
        return '>>'


class binary_opp182(binary_op):
    # binary_op --> <
    def __init__(self, LT):
        pass

    def toCode(self):
        return '<'


class binary_opp183(binary_op):
    # binary_op --> >
    def __init__(self, GT):
        pass

    def toCode(self):
        return '>'


class binary_opp184(binary_op):
    # binary_op --> <=
    def __init__(self, LE):
        pass

    def toCode(self):
        return '<='


class binary_opp185(binary_op):
    # binary_op --> >=
    def __init__(self, GE):
        pass

    def toCode(self):
        return '>='


class binary_opp186(binary_op):
    # binary_op --> ==
    def __init__(self, EQ):
        pass

    def toCode(self):
        return '=='


class binary_opp187(binary_op):
    # binary_op --> !=
    def __init__(self, NEQ):
        pass

    def toCode(self):
        return '!='


class binary_opp188(binary_op):
    # binary_op --> &
    def __init__(self, Ampersand):
        pass

    def toCode(self):
        return '&'


class binary_opp189(binary_op):
    # binary_op --> ^
    def __init__(self, Caret):
        pass

    def toCode(self):
        return '^'


class binary_opp190(binary_op):
    # binary_op --> |
    def __init__(self, VerticalBar):
        pass

    def toCode(self):
        return '|'


class binary_opp191(binary_op):
    # binary_op --> &&
    def __init__(self, AND):
        pass

    def toCode(self):
        return '&&'


class binary_opp192(binary_op):
    # binary_op --> ||
    def __init__(self, OR):
        pass

    def toCode(self):
        return '||'


class conditional_expp193(conditional_exp):
    # conditional_exp --> binary_exp
    def __init__(self, binary_exp):
        self.binary_exp = binary_exp

    def toCode(self):
        return self.binary_exp.toCode()


class conditional_expp194(conditional_exp):
    # conditional_exp --> binary_exp ? exp : conditional_exp
    def __init__(self, binary_exp, Question, exp, Colon, conditional_exp):
        self.binary_exp = binary_exp
        self.exp = exp
        self.conditional_exp = conditional_exp

    def toCode(self):
        return self.binary_exp.toCode() + '?' + self.exp.toCode() + ':' + self.conditional_exp.toCode()


class assignment_expp195(assignment_exp):
    # assignment_exp --> conditional_exp
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp

    def toCode(self):
        return self.conditional_exp.toCode()


class assignment_expp196(assignment_exp):
    # assignment_exp --> unary_exp assignment_op assignment_exp
    def __init__(self, unary_exp, assignment_op, assignment_exp):
        self.unary_exp = unary_exp
        self.assignment_op = assignment_op
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.unary_exp.toCode() + self.assignment_op.toCode() + self.assignment_exp.toCode()


class assignment_opp197(assignment_op):
    # assignment_op --> =
    def __init__(self, Assign):
        pass

    def toCode(self):
        return '='


class assignment_opp198(assignment_op):
    # assignment_op --> *=
    def __init__(self, AddAssign):
        pass

    def toCode(self):
        return '*='


class assignment_opp199(assignment_op):
    # assignment_op --> /=
    def __init__(self, SubAssign):
        pass

    def toCode(self):
        return '/='


class assignment_opp200(assignment_op):
    # assignment_op --> %=
    def __init__(self, MulAssign):
        pass

    def toCode(self):
        return '%='


class assignment_opp201(assignment_op):
    # assignment_op --> +=
    def __init__(self, DivAssign):
        pass

    def toCode(self):
        return '+='


class assignment_opp202(assignment_op):
    # assignment_op --> -=
    def __init__(self, ModAssign):
        pass

    def toCode(self):
        return '-='


class assignment_opp203(assignment_op):
    # assignment_op --> <<=
    def __init__(self, LeftShiftAssign):
        pass

    def toCode(self):
        return '<<='


class assignment_opp204(assignment_op):
    # assignment_op --> >>=
    def __init__(self, RightShiftAssign):
        pass

    def toCode(self):
        return '>>='


class assignment_opp205(assignment_op):
    # assignment_op --> &=
    def __init__(self, AndAssign):
        pass

    def toCode(self):
        return '&='


class assignment_opp206(assignment_op):
    # assignment_op --> ^=
    def __init__(self, XorAssign):
        pass

    def toCode(self):
        return '^='


class assignment_opp207(assignment_op):
    # assignment_op --> |=
    def __init__(self, OrAssign):
        pass

    def toCode(self):
        return '|='


class expp208(exp):
    # exp --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class expp209(exp):
    # exp --> exp , assignment_exp
    def __init__(self, exp, Comma, assignment_exp):
        self.exp = exp
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.exp.toCode() + ',' + self.assignment_exp.toCode()


class decp210(dec):
    # dec --> struct_specifier ;
    def __init__(self, struct_specifier, Semicolon):
        self.struct_specifier = struct_specifier

    def toCode(self):
        return self.struct_specifier.toCode() + ';'


class decp211(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list

    def toCode(self):
        return self.dec_specifier.toCode() + self.init_dec_list.toCode() + ';'


class dec_specifierp212(dec_specifier):
    # dec_specifier --> type_specifier
    def __init__(self, type_specifier):
        self.type_specifier = type_specifier

    def toCode(self):
        return self.type_specifier.toCode()


class dec_specifierp213(dec_specifier):
    # dec_specifier --> type_qualifier dec_specifier
    def __init__(self, type_qualifier, dec_specifier):
        self.type_qualifier = type_qualifier
        self.dec_specifier = dec_specifier

    def toCode(self):
        return self.type_qualifier.toCode() + self.dec_specifier.toCode()


class dec_specifierp214(dec_specifier):
    # dec_specifier --> storage_class_specifier dec_specifier
    def __init__(self, storage_class_specifier, dec_specifier):
        self.storage_class_specifier = storage_class_specifier
        self.dec_specifier = dec_specifier

    def toCode(self):
        return self.storage_class_specifier.toCode() + self.dec_specifier.toCode()


class type_specifierp215(type_specifier):
    # type_specifier --> buildin_type_name
    def __init__(self, buildin_type_name):
        self.buildin_type_name = buildin_type_name

    def toCode(self):
        return self.buildin_type_name.toCode()


class type_specifierp216(type_specifier):
    # type_specifier --> typedef_name
    def __init__(self, typedef_name):
        self.typedef_name = typedef_name

    def toCode(self):
        return self.typedef_name.toCode()


class buildin_type_namep217(buildin_type_name):
    # buildin_type_name --> 'void'
    def __init__(self, void):
        pass

    def toCode(self):
        return 'void'


class buildin_type_namep218(buildin_type_name):
    # buildin_type_name --> 'char'
    def __init__(self, char):
        pass

    def toCode(self):
        return 'char'


class buildin_type_namep219(buildin_type_name):
    # buildin_type_name --> 'short'
    def __init__(self, short):
        pass

    def toCode(self):
        return 'short'


class buildin_type_namep220(buildin_type_name):
    # buildin_type_name --> 'int'
    def __init__(self, int):
        pass

    def toCode(self):
        return 'int'


class buildin_type_namep221(buildin_type_name):
    # buildin_type_name --> 'long'
    def __init__(self, long):
        pass

    def toCode(self):
        return 'long'


class buildin_type_namep222(buildin_type_name):
    # buildin_type_name --> 'fixed'
    def __init__(self, fixed):
        pass

    def toCode(self):
        return 'fixed'


class buildin_type_namep223(buildin_type_name):
    # buildin_type_name --> 'half'
    def __init__(self, half):
        pass

    def toCode(self):
        return 'half'


class buildin_type_namep224(buildin_type_name):
    # buildin_type_name --> 'float'
    def __init__(self, float):
        pass

    def toCode(self):
        return 'float'


class buildin_type_namep225(buildin_type_name):
    # buildin_type_name --> 'double'
    def __init__(self, double):
        pass

    def toCode(self):
        return 'double'


class buildin_type_namep226(buildin_type_name):
    # buildin_type_name --> 'sampler2D'
    def __init__(self, sampler2D):
        pass

    def toCode(self):
        return 'sampler2D'


class buildin_type_namep227(buildin_type_name):
    # buildin_type_name --> 'float2'
    def __init__(self, float2):
        pass

    def toCode(self):
        return 'float2'


class buildin_type_namep228(buildin_type_name):
    # buildin_type_name --> 'float3'
    def __init__(self, float3):
        pass

    def toCode(self):
        return 'float3'


class buildin_type_namep229(buildin_type_name):
    # buildin_type_name --> 'float4'
    def __init__(self, float4):
        pass

    def toCode(self):
        return 'float4'


class buildin_type_namep230(buildin_type_name):
    # buildin_type_name --> 'half2'
    def __init__(self, half2):
        pass

    def toCode(self):
        return 'half2'


class buildin_type_namep231(buildin_type_name):
    # buildin_type_name --> 'half3'
    def __init__(self, half3):
        pass

    def toCode(self):
        return 'half3'


class buildin_type_namep232(buildin_type_name):
    # buildin_type_name --> 'half4'
    def __init__(self, half4):
        pass

    def toCode(self):
        return 'half4'


class buildin_type_namep233(buildin_type_name):
    # buildin_type_name --> 'fixed2'
    def __init__(self, fixed2):
        pass

    def toCode(self):
        return 'fixed2'


class buildin_type_namep234(buildin_type_name):
    # buildin_type_name --> 'fixed3'
    def __init__(self, fixed3):
        pass

    def toCode(self):
        return 'fixed3'


class buildin_type_namep235(buildin_type_name):
    # buildin_type_name --> 'fixed4'
    def __init__(self, fixed4):
        pass

    def toCode(self):
        return 'fixed4'


class buildin_type_namep236(buildin_type_name):
    # buildin_type_name --> 'float3x3'
    def __init__(self, float3x3):
        pass

    def toCode(self):
        return 'float3x3'


class type_qualifierp237(type_qualifier):
    # type_qualifier --> 'uniform'
    def __init__(self, uniform):
        pass

    def toCode(self):
        return 'uniform'


class type_qualifierp238(type_qualifier):
    # type_qualifier --> 'inline'
    def __init__(self, inline):
        pass

    def toCode(self):
        return 'inline'


class type_qualifierp239(type_qualifier):
    # type_qualifier --> 'const'
    def __init__(self, const):
        pass

    def toCode(self):
        return 'const'


class storage_class_specifierp240(storage_class_specifier):
    # storage_class_specifier --> 'static'
    def __init__(self, static):
        pass

    def toCode(self):
        return 'static'


class typedef_namep241(typedef_name):
    # typedef_name --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class struct_specifierp242(struct_specifier):
    # struct_specifier --> 'struct' ID
    def __init__(self, struct, ID):
        self.ID = ID

    def toCode(self):
        return 'struct' + self.ID.toCode()


class struct_specifierp243(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list

    def toCode(self):
        return 'struct' + self.ID.toCode() + '{' + self.struct_dec_list.toCode() + '}'


class struct_dec_listp244(struct_dec_list):
    # struct_dec_list --> struct_dec
    def __init__(self, struct_dec):
        self.struct_dec = struct_dec

    def toCode(self):
        return self.struct_dec.toCode()


class struct_dec_listp245(struct_dec_list):
    # struct_dec_list --> struct_dec_list struct_dec
    def __init__(self, struct_dec_list, struct_dec):
        self.struct_dec_list = struct_dec_list
        self.struct_dec = struct_dec

    def toCode(self):
        return self.struct_dec_list.toCode() + self.struct_dec.toCode()


class struct_decp246(struct_dec):
    # struct_dec --> type_specifier struct_declarator_list ;
    def __init__(self, type_specifier, struct_declarator_list, Semicolon):
        self.type_specifier = type_specifier
        self.struct_declarator_list = struct_declarator_list

    def toCode(self):
        return self.type_specifier.toCode() + self.struct_declarator_list.toCode() + ';'


class struct_decp247(struct_dec):
    # struct_dec --> ID ;
    def __init__(self, ID, Semicolon):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode() + ';'


class struct_decp248(struct_dec):
    # struct_dec --> ID ( Number )
    def __init__(self, ID, LParen, Number, RParen):
        self.ID = ID
        self.Number = Number

    def toCode(self):
        return self.ID.toCode() + '(' + self.Number.toCode() + ')'


class struct_decp249(struct_dec):
    # struct_dec --> ID ( Number , Number )
    def __init__(self, ID, LParen, Number1, Comma, Number2, RParen):
        self.ID = ID
        self.Number1 = Number1
        self.Number2 = Number2

    def toCode(self):
        return self.ID.toCode() + '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ')'


class struct_decp250(struct_dec):
    # struct_dec --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class struct_decp251(struct_dec):
    # struct_dec --> 'INTERNAL_DATA'
    def __init__(self, INTERNAL_DATA):
        pass

    def toCode(self):
        return 'INTERNAL_DATA'


class struct_decp252(struct_dec):
    # struct_dec --> 'UNITY_VERTEX_INPUT_INSTANCE_ID'
    def __init__(self, UNITY_VERTEX_INPUT_INSTANCE_ID):
        pass

    def toCode(self):
        return 'UNITY_VERTEX_INPUT_INSTANCE_ID'


class struct_decp253(struct_dec):
    # struct_dec --> 'UNITY_VERTEX_OUTPUT_STEREO'
    def __init__(self, UNITY_VERTEX_OUTPUT_STEREO):
        pass

    def toCode(self):
        return 'UNITY_VERTEX_OUTPUT_STEREO'


class struct_declarator_listp254(struct_declarator_list):
    # struct_declarator_list --> struct_declarator
    def __init__(self, struct_declarator):
        self.struct_declarator = struct_declarator

    def toCode(self):
        return self.struct_declarator.toCode()


class struct_declarator_listp255(struct_declarator_list):
    # struct_declarator_list --> struct_declarator_list , struct_declarator
    def __init__(self, struct_declarator_list, Comma, struct_declarator):
        self.struct_declarator_list = struct_declarator_list
        self.struct_declarator = struct_declarator

    def toCode(self):
        return self.struct_declarator_list.toCode() + ',' + self.struct_declarator.toCode()


class struct_declaratorp256(struct_declarator):
    # struct_declarator --> declarator
    def __init__(self, declarator):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode()


class struct_declaratorp257(struct_declarator):
    # struct_declarator --> declarator : ID
    def __init__(self, declarator, Colon, ID):
        self.declarator = declarator
        self.ID = ID

    def toCode(self):
        return self.declarator.toCode() + ':' + self.ID.toCode()


class declaratorp258(declarator):
    # declarator --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class declaratorp259(declarator):
    # declarator --> declarator [ exp ]
    def __init__(self, declarator, LBrack, exp, RBrack):
        self.declarator = declarator
        self.exp = exp

    def toCode(self):
        return self.declarator.toCode() + '[' + self.exp.toCode() + ']'


class declaratorp260(declarator):
    # declarator --> declarator ( )
    def __init__(self, declarator, LParen, RParen):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode() + '(' + ')'


class declaratorp261(declarator):
    # declarator --> declarator ( parameter_list )
    def __init__(self, declarator, LParen, parameter_list, RParen):
        self.declarator = declarator
        self.parameter_list = parameter_list

    def toCode(self):
        return self.declarator.toCode() + '(' + self.parameter_list.toCode() + ')'


class parameter_listp262(parameter_list):
    # parameter_list --> parameter_dec
    def __init__(self, parameter_dec):
        self.parameter_dec = parameter_dec

    def toCode(self):
        return self.parameter_dec.toCode()


class parameter_listp263(parameter_list):
    # parameter_list --> parameter_list , parameter_dec
    def __init__(self, parameter_list, Comma, parameter_dec):
        self.parameter_list = parameter_list
        self.parameter_dec = parameter_dec

    def toCode(self):
        return self.parameter_list.toCode() + ',' + self.parameter_dec.toCode()


class parameter_decp264(parameter_dec):
    # parameter_dec --> parameter_dec_specifier declarator
    def __init__(self, parameter_dec_specifier, declarator):
        self.parameter_dec_specifier = parameter_dec_specifier
        self.declarator = declarator

    def toCode(self):
        return self.parameter_dec_specifier.toCode() + self.declarator.toCode()


class parameter_decp265(parameter_dec):
    # parameter_dec --> parameter_dec_specifier declarator : ID
    def __init__(self, parameter_dec_specifier, declarator, Colon, ID):
        self.parameter_dec_specifier = parameter_dec_specifier
        self.declarator = declarator
        self.ID = ID

    def toCode(self):
        return self.parameter_dec_specifier.toCode() + self.declarator.toCode() + ':' + self.ID.toCode()


class parameter_dec_specifierp266(parameter_dec_specifier):
    # parameter_dec_specifier --> dec_specifier
    def __init__(self, dec_specifier):
        self.dec_specifier = dec_specifier

    def toCode(self):
        return self.dec_specifier.toCode()


class parameter_dec_specifierp267(parameter_dec_specifier):
    # parameter_dec_specifier --> 'out' dec_specifier
    def __init__(self, out, dec_specifier):
        self.dec_specifier = dec_specifier

    def toCode(self):
        return 'out' + self.dec_specifier.toCode()


class parameter_dec_specifierp268(parameter_dec_specifier):
    # parameter_dec_specifier --> 'inout' dec_specifier
    def __init__(self, inout, dec_specifier):
        self.dec_specifier = dec_specifier

    def toCode(self):
        return 'inout' + self.dec_specifier.toCode()


class parameter_dec_specifierp269(parameter_dec_specifier):
    # parameter_dec_specifier --> 'triangle' dec_specifier
    def __init__(self, triangle, dec_specifier):
        self.dec_specifier = dec_specifier

    def toCode(self):
        return 'triangle' + self.dec_specifier.toCode()


class parameter_dec_specifierp270(parameter_dec_specifier):
    # parameter_dec_specifier --> 'inout' 'TriangleStream' < ID >
    def __init__(self, inout, TriangleStream, LT, ID, GT):
        self.ID = ID

    def toCode(self):
        return 'inout' + 'TriangleStream' + '<' + self.ID.toCode() + '>'


class init_dec_listp271(init_dec_list):
    # init_dec_list --> init_dec
    def __init__(self, init_dec):
        self.init_dec = init_dec

    def toCode(self):
        return self.init_dec.toCode()


class init_dec_listp272(init_dec_list):
    # init_dec_list --> init_dec_list , init_dec
    def __init__(self, init_dec_list, Comma, init_dec):
        self.init_dec_list = init_dec_list
        self.init_dec = init_dec

    def toCode(self):
        return self.init_dec_list.toCode() + ',' + self.init_dec.toCode()


class init_decp273(init_dec):
    # init_dec --> declarator
    def __init__(self, declarator):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode()


class init_decp274(init_dec):
    # init_dec --> declarator = initializer
    def __init__(self, declarator, Assign, initializer):
        self.declarator = declarator
        self.initializer = initializer

    def toCode(self):
        return self.declarator.toCode() + '=' + self.initializer.toCode()


class initializerp275(initializer):
    # initializer --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class initializerp276(initializer):
    # initializer --> { initializer_list }
    def __init__(self, LBrace, initializer_list, RBrace):
        self.initializer_list = initializer_list

    def toCode(self):
        return '{' + self.initializer_list.toCode() + '}'


class initializerp277(initializer):
    # initializer --> { initializer_list , }
    def __init__(self, LBrace, initializer_list, Comma, RBrace):
        self.initializer_list = initializer_list

    def toCode(self):
        return '{' + self.initializer_list.toCode() + ',' + '}'


class initializer_listp278(initializer_list):
    # initializer_list --> initializer
    def __init__(self, initializer):
        self.initializer = initializer

    def toCode(self):
        return self.initializer.toCode()


class initializer_listp279(initializer_list):
    # initializer_list --> initializer_list , initializer
    def __init__(self, initializer_list, Comma, initializer):
        self.initializer_list = initializer_list
        self.initializer = initializer

    def toCode(self):
        return self.initializer_list.toCode() + ',' + self.initializer.toCode()


class stmp280(stm):
    # stm --> exp_stm
    def __init__(self, exp_stm):
        self.exp_stm = exp_stm

    def toCode(self):
        return self.exp_stm.toCode()


class stmp281(stm):
    # stm --> compound_stm
    def __init__(self, compound_stm):
        self.compound_stm = compound_stm

    def toCode(self):
        return self.compound_stm.toCode()


class stmp282(stm):
    # stm --> selection_stm
    def __init__(self, selection_stm):
        self.selection_stm = selection_stm

    def toCode(self):
        return self.selection_stm.toCode()


class stmp283(stm):
    # stm --> iteration_stm
    def __init__(self, iteration_stm):
        self.iteration_stm = iteration_stm

    def toCode(self):
        return self.iteration_stm.toCode()


class stmp284(stm):
    # stm --> jump_stm
    def __init__(self, jump_stm):
        self.jump_stm = jump_stm

    def toCode(self):
        return self.jump_stm.toCode()


class stmp285(stm):
    # stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class stmp286(stm):
    # stm --> 'UNITY_BRANCH'
    def __init__(self, UNITY_BRANCH):
        pass

    def toCode(self):
        return 'UNITY_BRANCH'


class stmp287(stm):
    # stm --> 'UNITY_UNROLL'
    def __init__(self, UNITY_UNROLL):
        pass

    def toCode(self):
        return 'UNITY_UNROLL'


class stmp288(stm):
    # stm --> 'TRANSFER_SHADOW_CASTER_NORMALOFFSET' ( ID )
    def __init__(self, TRANSFER_SHADOW_CASTER_NORMALOFFSET, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return 'TRANSFER_SHADOW_CASTER_NORMALOFFSET' + '(' + self.ID.toCode() + ')'


class stmp289(stm):
    # stm --> 'SHADOW_CASTER_FRAGMENT' ( ID )
    def __init__(self, SHADOW_CASTER_FRAGMENT, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return 'SHADOW_CASTER_FRAGMENT' + '(' + self.ID.toCode() + ')'


class stmp290(stm):
    # stm --> 'SPEEDTREE_COPY_FRAG' ( ID , ID )
    def __init__(self, SPEEDTREE_COPY_FRAG, LParen, ID1, Comma, ID2, RParen):
        self.ID1 = ID1
        self.ID2 = ID2

    def toCode(self):
        return 'SPEEDTREE_COPY_FRAG' + '(' + self.ID1.toCode() + ',' + self.ID2.toCode() + ')'


class stmp291(stm):
    # stm --> 'UNITY_TRANSFER_DITHER_CROSSFADE_HPOS' ( argument_exp_list )
    def __init__(self, UNITY_TRANSFER_DITHER_CROSSFADE_HPOS, LParen, argument_exp_list, RParen):
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return 'UNITY_TRANSFER_DITHER_CROSSFADE_HPOS' + '(' + self.argument_exp_list.toCode() + ')'


class stmp292(stm):
    # stm --> 'UNITY_APPLY_DITHER_CROSSFADE' ( ID )
    def __init__(self, UNITY_APPLY_DITHER_CROSSFADE, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return 'UNITY_APPLY_DITHER_CROSSFADE' + '(' + self.ID.toCode() + ')'


class exp_stmp293(exp_stm):
    # exp_stm --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return self.exp.toCode() + ';'


class exp_stmp294(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass

    def toCode(self):
        return ';'


class compound_stmp295(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list

    def toCode(self):
        return '{' + self.block_item_list.toCode() + '}'


class compound_stmp296(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass

    def toCode(self):
        return '{' + '}'


class block_item_listp297(block_item_list):
    # block_item_list --> block_item
    def __init__(self, block_item):
        self.block_item = block_item

    def toCode(self):
        return self.block_item.toCode()


class block_item_listp298(block_item_list):
    # block_item_list --> block_item_list block_item
    def __init__(self, block_item_list, block_item):
        self.block_item_list = block_item_list
        self.block_item = block_item

    def toCode(self):
        return self.block_item_list.toCode() + self.block_item.toCode()


class block_itemp299(block_item):
    # block_item --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class block_itemp300(block_item):
    # block_item --> stm
    def __init__(self, stm):
        self.stm = stm

    def toCode(self):
        return self.stm.toCode()


class selection_stmp301(selection_stm):
    # selection_stm --> 'if' ( exp ) stm
    def __init__(self, _if, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm

    def toCode(self):
        return 'if' + '(' + self.exp.toCode() + ')' + self.stm.toCode()


class selection_stmp302(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, _if, LParen, exp, RParen, stm1, _else, stm2):
        self.exp = exp
        self.stm1 = stm1
        self.stm2 = stm2

    def toCode(self):
        return 'if' + '(' + self.exp.toCode() + ')' + self.stm1.toCode() + 'else' + self.stm2.toCode()


class iteration_stmp303(iteration_stm):
    # iteration_stm --> 'while' ( exp ) stm
    def __init__(self, _while, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm

    def toCode(self):
        return 'while' + '(' + self.exp.toCode() + ')' + self.stm.toCode()


class iteration_stmp304(iteration_stm):
    # iteration_stm --> 'do' stm 'while' ( exp ) ;
    def __init__(self, do, stm, _while, LParen, exp, RParen, Semicolon):
        self.stm = stm
        self.exp = exp

    def toCode(self):
        return 'do' + self.stm.toCode() + 'while' + '(' + self.exp.toCode() + ')' + ';'


class iteration_stmp305(iteration_stm):
    # iteration_stm --> 'for' ( exp ; exp ; exp ) stm
    def __init__(self, _for, LParen, exp1, Semicolon1, exp2, Semicolon2, exp3, RParen, stm):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.stm = stm

    def toCode(self):
        return 'for' + '(' + self.exp1.toCode() + ';' + self.exp2.toCode() + ';' + self.exp3.toCode() + ')' + self.stm.toCode()


class iteration_stmp306(iteration_stm):
    # iteration_stm --> 'for' ( dec_specifier init_dec_list ; exp ; exp ) stm
    def __init__(self, _for, LParen, dec_specifier, init_dec_list, Semicolon1, exp1, Semicolon2, exp2, RParen, stm):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list
        self.exp1 = exp1
        self.exp2 = exp2
        self.stm = stm

    def toCode(self):
        return 'for' + '(' + self.dec_specifier.toCode() + self.init_dec_list.toCode() + ';' + self.exp1.toCode() + ';' + self.exp2.toCode() + ')' + self.stm.toCode()


class jump_stmp307(jump_stm):
    # jump_stm --> 'goto' ID
    def __init__(self, goto, ID):
        self.ID = ID

    def toCode(self):
        return 'goto' + self.ID.toCode()


class jump_stmp308(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, _continue):
        pass

    def toCode(self):
        return 'continue'


class jump_stmp309(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, _break):
        pass

    def toCode(self):
        return 'break'


class jump_stmp310(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, _return, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return 'return' + self.exp.toCode() + ';'


class Test(unittest.TestCase):


    def test(self):
        pass
