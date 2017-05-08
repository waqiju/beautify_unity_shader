from app.symbol_type import SymbolType
from app.syntax_nonterminal import Nonterminal
import unittest


class NonterminalType(SymbolType):

    prog = 'prog'
    cg_prog = 'cg_prog'
    cg_stms = 'cg_stms'
    cg_stm = 'cg_stm'
    function_definition = 'function_definition'
    preprocessing_stm = 'preprocessing_stm'
    pp_if_stm = 'pp_if_stm'
    pp_cmd = 'pp_cmd'
    ids_or_numbers = 'ids_or_numbers'
    primary_exp = 'primary_exp'
    postfix_exp = 'postfix_exp'
    argument_exp_list = 'argument_exp_list'
    unary_exp = 'unary_exp'
    unary_op = 'unary_op'
    binary_exp = 'binary_exp'
    binary_op = 'binary_op'
    conditional_exp = 'conditional_exp'
    assignment_exp = 'assignment_exp'
    assignment_op = 'assignment_op'
    exp = 'exp'
    dec = 'dec'
    dec_specifier = 'dec_specifier'
    type_specifier = 'type_specifier'
    type_qualifier = 'type_qualifier'
    typedef_name = 'typedef_name'
    struct_specifier = 'struct_specifier'
    struct_dec_list = 'struct_dec_list'
    struct_dec = 'struct_dec'
    struct_declarator_list = 'struct_declarator_list'
    struct_declarator = 'struct_declarator'
    declarator = 'declarator'
    parameter_list = 'parameter_list'
    parameter_dec = 'parameter_dec'
    init_dec_list = 'init_dec_list'
    init_dec = 'init_dec'
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


class cg_prog(Nonterminal):
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


class ids_or_numbers(Nonterminal):
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


class type_qualifier(Nonterminal):
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


class init_dec_list(Nonterminal):
    pass


class init_dec(Nonterminal):
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
    # prog --> 'CGPROGRAM' cg_prog 'ENDCG'
    def __init__(self, CGPROGRAM, cg_prog, ENDCG):
        self.cg_prog = cg_prog


class progp2(prog):
    # prog --> 'CGINCLUDE' cg_prog 'ENDCG'
    def __init__(self, CGINCLUDE, cg_prog, ENDCG):
        self.cg_prog = cg_prog


class cg_progp3(cg_prog):
    # cg_prog --> cg_stms
    def __init__(self, cg_stms):
        self.cg_stms = cg_stms


class cg_stmsp4(cg_stms):
    # cg_stms --> cg_stm cg_stms
    def __init__(self, cg_stm, cg_stms):
        self.cg_stm = cg_stm
        self.cg_stms = cg_stms


class cg_stmsp5(cg_stms):
    # cg_stms -->
    def __init__(self):
        pass


class cg_stmp6(cg_stm):
    # cg_stm --> preprocessing_stm
    def __init__(self, preprocessing_stm):
        self.preprocessing_stm = preprocessing_stm


class cg_stmp7(cg_stm):
    # cg_stm --> function_definition
    def __init__(self, function_definition):
        self.function_definition = function_definition


class cg_stmp8(cg_stm):
    # cg_stm --> dec
    def __init__(self, dec):
        self.dec = dec


class function_definitionp9(function_definition):
    # function_definition --> dec_specifier declarator compound_stm
    def __init__(self, dec_specifier, declarator, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm


class function_definitionp10(function_definition):
    # function_definition --> dec_specifier declarator : ID compound_stm
    def __init__(self, dec_specifier, declarator, Colon, ID, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID = ID
        self.compound_stm = compound_stm


class preprocessing_stmp11(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class preprocessing_stmp12(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd


class pp_if_stmp13(pp_if_stm):
    # pp_if_stm --> # 'if' ID
    def __init__(self, Pound, if, ID):
        self.ID = ID


class pp_if_stmp14(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID


class pp_if_stmp15(pp_if_stm):
    # pp_if_stm --> # 'ifndef' ID
    def __init__(self, Pound, ifndef, ID):
        self.ID = ID


class pp_if_stmp16(pp_if_stm):
    # pp_if_stm --> # 'elif' ID
    def __init__(self, Pound, elif, ID):
        self.ID = ID


class pp_if_stmp17(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, else):
        pass


class pp_if_stmp18(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass


class pp_cmdp19(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String


class pp_cmdp20(pp_cmd):
    # pp_cmd --> # 'pragma' ids_or_numbers Enter
    def __init__(self, Pound, pragma, ids_or_numbers, Enter):
        self.ids_or_numbers = ids_or_numbers
        self.Enter = Enter


class ids_or_numbersp21(ids_or_numbers):
    # ids_or_numbers --> ID ids_or_numbers
    def __init__(self, ID, ids_or_numbers):
        self.ID = ID
        self.ids_or_numbers = ids_or_numbers


class ids_or_numbersp22(ids_or_numbers):
    # ids_or_numbers --> Number ids_or_numbers
    def __init__(self, Number, ids_or_numbers):
        self.Number = Number
        self.ids_or_numbers = ids_or_numbers


class ids_or_numbersp23(ids_or_numbers):
    # ids_or_numbers -->
    def __init__(self):
        pass


class primary_expp24(primary_exp):
    # primary_exp --> ID
    def __init__(self, ID):
        self.ID = ID


class primary_expp25(primary_exp):
    # primary_exp --> String
    def __init__(self, String):
        self.String = String


class primary_expp26(primary_exp):
    # primary_exp --> Number
    def __init__(self, Number):
        self.Number = Number


class primary_expp27(primary_exp):
    # primary_exp --> ( exp )
    def __init__(self, LParen, exp, RParen):
        self.exp = exp


class postfix_expp28(postfix_exp):
    # postfix_exp --> primary_exp
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp


class postfix_expp29(postfix_exp):
    # postfix_exp --> postfix_exp [ exp ]
    def __init__(self, postfix_exp, LBrack, exp, RBrack):
        self.postfix_exp = postfix_exp
        self.exp = exp


class postfix_expp30(postfix_exp):
    # postfix_exp --> postfix_exp ( )
    def __init__(self, postfix_exp, LParen, RParen):
        self.postfix_exp = postfix_exp


class postfix_expp31(postfix_exp):
    # postfix_exp --> postfix_exp ( argument_exp_list )
    def __init__(self, postfix_exp, LParen, argument_exp_list, RParen):
        self.postfix_exp = postfix_exp
        self.argument_exp_list = argument_exp_list


class postfix_expp32(postfix_exp):
    # postfix_exp --> postfix_exp . ID
    def __init__(self, postfix_exp, Dot, ID):
        self.postfix_exp = postfix_exp
        self.ID = ID


class postfix_expp33(postfix_exp):
    # postfix_exp --> postfix_exp ++
    def __init__(self, postfix_exp, Increment):
        self.postfix_exp = postfix_exp


class postfix_expp34(postfix_exp):
    # postfix_exp --> postfix_exp --
    def __init__(self, postfix_exp, Decrement):
        self.postfix_exp = postfix_exp


class argument_exp_listp35(argument_exp_list):
    # argument_exp_list --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp


class argument_exp_listp36(argument_exp_list):
    # argument_exp_list --> argument_exp_list , assignment_exp
    def __init__(self, argument_exp_list, Comma, assignment_exp):
        self.argument_exp_list = argument_exp_list
        self.assignment_exp = assignment_exp


class unary_expp37(unary_exp):
    # unary_exp --> postfix_exp
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp


class unary_expp38(unary_exp):
    # unary_exp --> ++ unary_exp
    def __init__(self, Increment, unary_exp):
        self.unary_exp = unary_exp


class unary_expp39(unary_exp):
    # unary_exp --> -- unary_exp
    def __init__(self, Decrement, unary_exp):
        self.unary_exp = unary_exp


class unary_expp40(unary_exp):
    # unary_exp --> unary_op unary_exp
    def __init__(self, unary_op, unary_exp):
        self.unary_op = unary_op
        self.unary_exp = unary_exp


class unary_opp41(unary_op):
    # unary_op --> +
    def __init__(self, Plus):
        pass


class unary_opp42(unary_op):
    # unary_op --> -
    def __init__(self, Minus):
        pass


class unary_opp43(unary_op):
    # unary_op --> !
    def __init__(self, NOT):
        pass


class unary_opp44(unary_op):
    # unary_op --> ~
    def __init__(self, Tilde):
        pass


class binary_expp45(binary_exp):
    # binary_exp --> unary_exp
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp


class binary_expp46(binary_exp):
    # binary_exp --> binary_exp binary_op unary_exp
    def __init__(self, binary_exp, binary_op, unary_exp):
        self.binary_exp = binary_exp
        self.binary_op = binary_op
        self.unary_exp = unary_exp


class binary_opp47(binary_op):
    # binary_op --> *
    def __init__(self, Times):
        pass


class binary_opp48(binary_op):
    # binary_op --> /
    def __init__(self, Divide):
        pass


class binary_opp49(binary_op):
    # binary_op --> %
    def __init__(self, Percent):
        pass


class binary_opp50(binary_op):
    # binary_op --> +
    def __init__(self, Plus):
        pass


class binary_opp51(binary_op):
    # binary_op --> -
    def __init__(self, Minus):
        pass


class binary_opp52(binary_op):
    # binary_op --> <<
    def __init__(self, LeftShift):
        pass


class binary_opp53(binary_op):
    # binary_op --> >>
    def __init__(self, RightShift):
        pass


class binary_opp54(binary_op):
    # binary_op --> <
    def __init__(self, LT):
        pass


class binary_opp55(binary_op):
    # binary_op --> >
    def __init__(self, GT):
        pass


class binary_opp56(binary_op):
    # binary_op --> <=
    def __init__(self, LE):
        pass


class binary_opp57(binary_op):
    # binary_op --> >=
    def __init__(self, GE):
        pass


class binary_opp58(binary_op):
    # binary_op --> ==
    def __init__(self, EQ):
        pass


class binary_opp59(binary_op):
    # binary_op --> !=
    def __init__(self, NEQ):
        pass


class binary_opp60(binary_op):
    # binary_op --> &
    def __init__(self, Ampersand):
        pass


class binary_opp61(binary_op):
    # binary_op --> ^
    def __init__(self, Caret):
        pass


class binary_opp62(binary_op):
    # binary_op --> |
    def __init__(self, VerticalBar):
        pass


class binary_opp63(binary_op):
    # binary_op --> &&
    def __init__(self, AND):
        pass


class binary_opp64(binary_op):
    # binary_op --> ||
    def __init__(self, OR):
        pass


class conditional_expp65(conditional_exp):
    # conditional_exp --> binary_exp
    def __init__(self, binary_exp):
        self.binary_exp = binary_exp


class conditional_expp66(conditional_exp):
    # conditional_exp --> binary_exp ? exp : conditional_exp
    def __init__(self, binary_exp, Question, exp, Colon, conditional_exp):
        self.binary_exp = binary_exp
        self.exp = exp
        self.conditional_exp = conditional_exp


class assignment_expp67(assignment_exp):
    # assignment_exp --> conditional_exp
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp


class assignment_expp68(assignment_exp):
    # assignment_exp --> unary_exp assignment_op assignment_exp
    def __init__(self, unary_exp, assignment_op, assignment_exp):
        self.unary_exp = unary_exp
        self.assignment_op = assignment_op
        self.assignment_exp = assignment_exp


class assignment_opp69(assignment_op):
    # assignment_op --> =
    def __init__(self, Assign):
        pass


class assignment_opp70(assignment_op):
    # assignment_op --> *=
    def __init__(self, AddAssign):
        pass


class assignment_opp71(assignment_op):
    # assignment_op --> /=
    def __init__(self, SubAssign):
        pass


class assignment_opp72(assignment_op):
    # assignment_op --> %=
    def __init__(self, MulAssign):
        pass


class assignment_opp73(assignment_op):
    # assignment_op --> +=
    def __init__(self, DivAssign):
        pass


class assignment_opp74(assignment_op):
    # assignment_op --> -=
    def __init__(self, ModAssign):
        pass


class assignment_opp75(assignment_op):
    # assignment_op --> <<=
    def __init__(self, LeftShiftAssign):
        pass


class assignment_opp76(assignment_op):
    # assignment_op --> >>=
    def __init__(self, RightShiftAssign):
        pass


class assignment_opp77(assignment_op):
    # assignment_op --> &=
    def __init__(self, AndAssign):
        pass


class assignment_opp78(assignment_op):
    # assignment_op --> ^=
    def __init__(self, XorAssign):
        pass


class assignment_opp79(assignment_op):
    # assignment_op --> |=
    def __init__(self, OrAssign):
        pass


class expp80(exp):
    # exp --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp


class expp81(exp):
    # exp --> exp , assignment_exp
    def __init__(self, exp, Comma, assignment_exp):
        self.exp = exp
        self.assignment_exp = assignment_exp


class decp82(dec):
    # dec --> struct_specifier ;
    def __init__(self, struct_specifier, Semicolon):
        self.struct_specifier = struct_specifier


class decp83(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list


class dec_specifierp84(dec_specifier):
    # dec_specifier --> type_specifier
    def __init__(self, type_specifier):
        self.type_specifier = type_specifier


class dec_specifierp85(dec_specifier):
    # dec_specifier --> type_qualifier type_specifier
    def __init__(self, type_qualifier, type_specifier):
        self.type_qualifier = type_qualifier
        self.type_specifier = type_specifier


class type_specifierp86(type_specifier):
    # type_specifier --> 'void'
    def __init__(self, void):
        pass


class type_specifierp87(type_specifier):
    # type_specifier --> 'char'
    def __init__(self, char):
        pass


class type_specifierp88(type_specifier):
    # type_specifier --> 'short'
    def __init__(self, short):
        pass


class type_specifierp89(type_specifier):
    # type_specifier --> 'int'
    def __init__(self, int):
        pass


class type_specifierp90(type_specifier):
    # type_specifier --> 'long'
    def __init__(self, long):
        pass


class type_specifierp91(type_specifier):
    # type_specifier --> 'float'
    def __init__(self, float):
        pass


class type_specifierp92(type_specifier):
    # type_specifier --> 'double'
    def __init__(self, double):
        pass


class type_specifierp93(type_specifier):
    # type_specifier --> 'sampler2D'
    def __init__(self, sampler2D):
        pass


class type_specifierp94(type_specifier):
    # type_specifier --> 'float2'
    def __init__(self, float2):
        pass


class type_specifierp95(type_specifier):
    # type_specifier --> 'float3'
    def __init__(self, float3):
        pass


class type_specifierp96(type_specifier):
    # type_specifier --> 'float4'
    def __init__(self, float4):
        pass


class type_specifierp97(type_specifier):
    # type_specifier --> 'half2'
    def __init__(self, half2):
        pass


class type_specifierp98(type_specifier):
    # type_specifier --> 'half3'
    def __init__(self, half3):
        pass


class type_specifierp99(type_specifier):
    # type_specifier --> 'half4'
    def __init__(self, half4):
        pass


class type_specifierp100(type_specifier):
    # type_specifier --> 'fixed2'
    def __init__(self, fixed2):
        pass


class type_specifierp101(type_specifier):
    # type_specifier --> 'fixed3'
    def __init__(self, fixed3):
        pass


class type_specifierp102(type_specifier):
    # type_specifier --> 'fixed4'
    def __init__(self, fixed4):
        pass


class type_specifierp103(type_specifier):
    # type_specifier --> typedef_name
    def __init__(self, typedef_name):
        self.typedef_name = typedef_name


class type_qualifierp104(type_qualifier):
    # type_qualifier --> 'uniform'
    def __init__(self, uniform):
        pass


class typedef_namep105(typedef_name):
    # typedef_name --> ID
    def __init__(self, ID):
        self.ID = ID


class struct_specifierp106(struct_specifier):
    # struct_specifier --> 'struct' ID
    def __init__(self, struct, ID):
        self.ID = ID


class struct_specifierp107(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list


class struct_dec_listp108(struct_dec_list):
    # struct_dec_list --> struct_dec
    def __init__(self, struct_dec):
        self.struct_dec = struct_dec


class struct_dec_listp109(struct_dec_list):
    # struct_dec_list --> struct_dec_list struct_dec
    def __init__(self, struct_dec_list, struct_dec):
        self.struct_dec_list = struct_dec_list
        self.struct_dec = struct_dec


class struct_decp110(struct_dec):
    # struct_dec --> type_specifier struct_declarator_list ;
    def __init__(self, type_specifier, struct_declarator_list, Semicolon):
        self.type_specifier = type_specifier
        self.struct_declarator_list = struct_declarator_list


class struct_declarator_listp111(struct_declarator_list):
    # struct_declarator_list --> struct_declarator
    def __init__(self, struct_declarator):
        self.struct_declarator = struct_declarator


class struct_declarator_listp112(struct_declarator_list):
    # struct_declarator_list --> struct_declarator_list , struct_declarator
    def __init__(self, struct_declarator_list, Comma, struct_declarator):
        self.struct_declarator_list = struct_declarator_list
        self.struct_declarator = struct_declarator


class struct_declaratorp113(struct_declarator):
    # struct_declarator --> declarator
    def __init__(self, declarator):
        self.declarator = declarator


class struct_declaratorp114(struct_declarator):
    # struct_declarator --> declarator : ID
    def __init__(self, declarator, Colon, ID):
        self.declarator = declarator
        self.ID = ID


class declaratorp115(declarator):
    # declarator --> ID
    def __init__(self, ID):
        self.ID = ID


class declaratorp116(declarator):
    # declarator --> declarator [ exp ]
    def __init__(self, declarator, LBrack, exp, RBrack):
        self.declarator = declarator
        self.exp = exp


class declaratorp117(declarator):
    # declarator --> declarator ( parameter_list )
    def __init__(self, declarator, LParen, parameter_list, RParen):
        self.declarator = declarator
        self.parameter_list = parameter_list


class parameter_listp118(parameter_list):
    # parameter_list --> parameter_dec
    def __init__(self, parameter_dec):
        self.parameter_dec = parameter_dec


class parameter_listp119(parameter_list):
    # parameter_list --> parameter_list , parameter_dec
    def __init__(self, parameter_list, Comma, parameter_dec):
        self.parameter_list = parameter_list
        self.parameter_dec = parameter_dec


class parameter_decp120(parameter_dec):
    # parameter_dec --> type_specifier declarator
    def __init__(self, type_specifier, declarator):
        self.type_specifier = type_specifier
        self.declarator = declarator


class init_dec_listp121(init_dec_list):
    # init_dec_list --> init_dec
    def __init__(self, init_dec):
        self.init_dec = init_dec


class init_dec_listp122(init_dec_list):
    # init_dec_list --> init_dec_list , init_dec
    def __init__(self, init_dec_list, Comma, init_dec):
        self.init_dec_list = init_dec_list
        self.init_dec = init_dec


class init_decp123(init_dec):
    # init_dec --> declarator
    def __init__(self, declarator):
        self.declarator = declarator


class init_decp124(init_dec):
    # init_dec --> declarator = assignment_exp
    def __init__(self, declarator, Assign, assignment_exp):
        self.declarator = declarator
        self.assignment_exp = assignment_exp


class stmp125(stm):
    # stm --> exp_stm
    def __init__(self, exp_stm):
        self.exp_stm = exp_stm


class stmp126(stm):
    # stm --> compound_stm
    def __init__(self, compound_stm):
        self.compound_stm = compound_stm


class stmp127(stm):
    # stm --> selection_stm
    def __init__(self, selection_stm):
        self.selection_stm = selection_stm


class stmp128(stm):
    # stm --> iteration_stm
    def __init__(self, iteration_stm):
        self.iteration_stm = iteration_stm


class stmp129(stm):
    # stm --> jump_stm
    def __init__(self, jump_stm):
        self.jump_stm = jump_stm


class exp_stmp130(exp_stm):
    # exp_stm --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp


class exp_stmp131(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass


class compound_stmp132(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list


class compound_stmp133(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass


class block_item_listp134(block_item_list):
    # block_item_list --> block_item
    def __init__(self, block_item):
        self.block_item = block_item


class block_item_listp135(block_item_list):
    # block_item_list --> block_item_list block_item
    def __init__(self, block_item_list, block_item):
        self.block_item_list = block_item_list
        self.block_item = block_item


class block_itemp136(block_item):
    # block_item --> dec
    def __init__(self, dec):
        self.dec = dec


class block_itemp137(block_item):
    # block_item --> stm
    def __init__(self, stm):
        self.stm = stm


class selection_stmp138(selection_stm):
    # selection_stm --> 'if' ( exp ) stm
    def __init__(self, if, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm


class selection_stmp139(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, if, LParen, exp, RParen, stm, else, stm):
        self.exp = exp
        self.stm = stm
        self.stm = stm


class iteration_stmp140(iteration_stm):
    # iteration_stm --> 'while' ( exp ) stm
    def __init__(self, while, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm


class iteration_stmp141(iteration_stm):
    # iteration_stm --> 'do' stm 'while' ( exp ) ;
    def __init__(self, do, stm, while, LParen, exp, RParen, Semicolon):
        self.stm = stm
        self.exp = exp


class iteration_stmp142(iteration_stm):
    # iteration_stm --> 'for' ( exp ; exp ; exp ) stm
    def __init__(self, for, LParen, exp, Semicolon, exp, Semicolon, exp, RParen, stm):
        self.exp = exp
        self.exp = exp
        self.exp = exp
        self.stm = stm


class jump_stmp143(jump_stm):
    # jump_stm --> 'goto' ID
    def __init__(self, goto, ID):
        self.ID = ID


class jump_stmp144(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, continue):
        pass


class jump_stmp145(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, break):
        pass


class jump_stmp146(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, return, exp, Semicolon):
        self.exp = exp


class Test(unittest.TestCase):


    def test(self):
        pass
