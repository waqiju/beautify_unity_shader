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
    ids = 'ids'
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


class ids(Nonterminal):
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
    # cg_stm --> function_definition
    def __init__(self, function_definition):
        self.function_definition = function_definition


class cg_stmp7(cg_stm):
    # cg_stm --> dec
    def __init__(self, dec):
        self.dec = dec


class function_definitionp8(function_definition):
    # function_definition --> dec_specifier declarator compound_stm
    def __init__(self, dec_specifier, declarator, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm


class preprocessing_stmp9(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class preprocessing_stmp10(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd


class pp_if_stmp11(pp_if_stm):
    # pp_if_stm --> # 'if' ID
    def __init__(self, Pound, _if, ID):
        self.ID = ID


class pp_if_stmp12(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID


class pp_if_stmp13(pp_if_stm):
    # pp_if_stm --> # 'ifndef' ID
    def __init__(self, Pound, ifndef, ID):
        self.ID = ID


class pp_if_stmp14(pp_if_stm):
    # pp_if_stm --> # 'elif' ID
    def __init__(self, Pound, _elif, ID):
        self.ID = ID


class pp_if_stmp15(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, _else):
        pass


class pp_if_stmp16(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass


class pp_cmdp17(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String


class pp_cmdp18(pp_cmd):
    # pp_cmd --> # 'pragma' ids Enter
    def __init__(self, Pound, pragma, ids, Enter):
        self.ids = ids


class idsp19(ids):
    # ids --> ID ids
    def __init__(self, ID, ids):
        self.ID = ID
        self.ids = ids


class idsp20(ids):
    # ids -->
    def __init__(self):
        pass


class primary_expp21(primary_exp):
    # primary_exp --> ID
    def __init__(self, ID):
        self.ID = ID


class primary_expp22(primary_exp):
    # primary_exp --> String
    def __init__(self, String):
        self.String = String


class primary_expp23(primary_exp):
    # primary_exp --> Number
    def __init__(self, Number):
        self.Number = Number


class primary_expp24(primary_exp):
    # primary_exp --> ( exp )
    def __init__(self, LParen, exp, RParen):
        self.exp = exp


class postfix_expp25(postfix_exp):
    # postfix_exp --> primary_exp
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp


class postfix_expp26(postfix_exp):
    # postfix_exp --> postfix_exp [ exp ]
    def __init__(self, postfix_exp, LBrack, exp, RBrack):
        self.postfix_exp = postfix_exp
        self.exp = exp


class postfix_expp27(postfix_exp):
    # postfix_exp --> postfix_exp ( )
    def __init__(self, postfix_exp, LParen, RParen):
        self.postfix_exp = postfix_exp


class postfix_expp28(postfix_exp):
    # postfix_exp --> postfix_exp ( argument_exp_list )
    def __init__(self, postfix_exp, LParen, argument_exp_list, RParen):
        self.postfix_exp = postfix_exp
        self.argument_exp_list = argument_exp_list


class postfix_expp29(postfix_exp):
    # postfix_exp --> postfix_exp . ID
    def __init__(self, postfix_exp, Dot, ID):
        self.postfix_exp = postfix_exp
        self.ID = ID


class postfix_expp30(postfix_exp):
    # postfix_exp --> postfix_exp ++
    def __init__(self, postfix_exp, Increment):
        self.postfix_exp = postfix_exp


class postfix_expp31(postfix_exp):
    # postfix_exp --> postfix_exp --
    def __init__(self, postfix_exp, Decrement):
        self.postfix_exp = postfix_exp


class argument_exp_listp32(argument_exp_list):
    # argument_exp_list --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp


class argument_exp_listp33(argument_exp_list):
    # argument_exp_list --> argument_exp_list , assignment_exp
    def __init__(self, argument_exp_list, Comma, assignment_exp):
        self.argument_exp_list = argument_exp_list
        self.assignment_exp = assignment_exp


class unary_expp34(unary_exp):
    # unary_exp --> postfix_exp
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp


class unary_expp35(unary_exp):
    # unary_exp --> ++ unary_exp
    def __init__(self, Increment, unary_exp):
        self.unary_exp = unary_exp


class unary_expp36(unary_exp):
    # unary_exp --> -- unary_exp
    def __init__(self, Decrement, unary_exp):
        self.unary_exp = unary_exp


class unary_expp37(unary_exp):
    # unary_exp --> unary_op unary_exp
    def __init__(self, unary_op, unary_exp):
        self.unary_op = unary_op
        self.unary_exp = unary_exp


class unary_opp38(unary_op):
    # unary_op --> +
    def __init__(self, Plus):
        pass


class unary_opp39(unary_op):
    # unary_op --> -
    def __init__(self, Minus):
        pass


class unary_opp40(unary_op):
    # unary_op --> !
    def __init__(self, NOT):
        pass


class unary_opp41(unary_op):
    # unary_op --> ~
    def __init__(self, Tilde):
        pass


class binary_expp42(binary_exp):
    # binary_exp --> unary_exp
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp


class binary_expp43(binary_exp):
    # binary_exp --> binary_exp binary_op unary_exp
    def __init__(self, binary_exp, binary_op, unary_exp):
        self.binary_exp = binary_exp
        self.binary_op = binary_op
        self.unary_exp = unary_exp


class binary_opp44(binary_op):
    # binary_op --> *
    def __init__(self, Times):
        pass


class binary_opp45(binary_op):
    # binary_op --> /
    def __init__(self, Divide):
        pass


class binary_opp46(binary_op):
    # binary_op --> %
    def __init__(self, Percent):
        pass


class binary_opp47(binary_op):
    # binary_op --> +
    def __init__(self, Plus):
        pass


class binary_opp48(binary_op):
    # binary_op --> -
    def __init__(self, Minus):
        pass


class binary_opp49(binary_op):
    # binary_op --> <<
    def __init__(self, LeftShift):
        pass


class binary_opp50(binary_op):
    # binary_op --> >>
    def __init__(self, RightShift):
        pass


class binary_opp51(binary_op):
    # binary_op --> <
    def __init__(self, LT):
        pass


class binary_opp52(binary_op):
    # binary_op --> >
    def __init__(self, GT):
        pass


class binary_opp53(binary_op):
    # binary_op --> <=
    def __init__(self, LE):
        pass


class binary_opp54(binary_op):
    # binary_op --> >=
    def __init__(self, GE):
        pass


class binary_opp55(binary_op):
    # binary_op --> ==
    def __init__(self, EQ):
        pass


class binary_opp56(binary_op):
    # binary_op --> !=
    def __init__(self, NEQ):
        pass


class binary_opp57(binary_op):
    # binary_op --> &
    def __init__(self, Ampersand):
        pass


class binary_opp58(binary_op):
    # binary_op --> ^
    def __init__(self, Caret):
        pass


class binary_opp59(binary_op):
    # binary_op --> |
    def __init__(self, VerticalBar):
        pass


class binary_opp60(binary_op):
    # binary_op --> &&
    def __init__(self, AND):
        pass


class binary_opp61(binary_op):
    # binary_op --> ||
    def __init__(self, OR):
        pass


class conditional_expp62(conditional_exp):
    # conditional_exp --> binary_exp
    def __init__(self, binary_exp):
        self.binary_exp = binary_exp


class conditional_expp63(conditional_exp):
    # conditional_exp --> binary_exp ? exp : conditional_exp
    def __init__(self, binary_exp, Question, exp, Colon, conditional_exp):
        self.binary_exp = binary_exp
        self.exp = exp
        self.conditional_exp = conditional_exp


class assignment_expp64(assignment_exp):
    # assignment_exp --> conditional_exp
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp


class assignment_expp65(assignment_exp):
    # assignment_exp --> unary_exp assignment_op assignment_exp
    def __init__(self, unary_exp, assignment_op, assignment_exp):
        self.unary_exp = unary_exp
        self.assignment_op = assignment_op
        self.assignment_exp = assignment_exp


class assignment_opp66(assignment_op):
    # assignment_op --> =
    def __init__(self, Assign):
        pass


class expp67(exp):
    # exp --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp


class expp68(exp):
    # exp --> exp , assignment_exp
    def __init__(self, exp, Comma, assignment_exp):
        self.exp = exp
        self.assignment_exp = assignment_exp


class decp69(dec):
    # dec --> struct_specifier ;
    def __init__(self, struct_specifier, Semicolon):
        self.struct_specifier = struct_specifier


class decp70(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list


class dec_specifierp71(dec_specifier):
    # dec_specifier --> type_specifier
    def __init__(self, type_specifier):
        self.type_specifier = type_specifier


class dec_specifierp72(dec_specifier):
    # dec_specifier --> type_qualifier type_specifier
    def __init__(self, type_qualifier, type_specifier):
        self.type_qualifier = type_qualifier
        self.type_specifier = type_specifier


class type_specifierp73(type_specifier):
    # type_specifier --> 'void'
    def __init__(self, void):
        pass


class type_specifierp74(type_specifier):
    # type_specifier --> 'char'
    def __init__(self, char):
        pass


class type_specifierp75(type_specifier):
    # type_specifier --> 'short'
    def __init__(self, short):
        pass


class type_specifierp76(type_specifier):
    # type_specifier --> 'int'
    def __init__(self, int):
        pass


class type_specifierp77(type_specifier):
    # type_specifier --> 'long'
    def __init__(self, long):
        pass


class type_specifierp78(type_specifier):
    # type_specifier --> 'float'
    def __init__(self, float):
        pass


class type_specifierp79(type_specifier):
    # type_specifier --> 'double'
    def __init__(self, double):
        pass


class type_specifierp80(type_specifier):
    # type_specifier --> 'sampler2D'
    def __init__(self, sampler2D):
        pass


class type_specifierp81(type_specifier):
    # type_specifier --> 'float2'
    def __init__(self, float2):
        pass


class type_specifierp82(type_specifier):
    # type_specifier --> 'float3'
    def __init__(self, float3):
        pass


class type_specifierp83(type_specifier):
    # type_specifier --> 'float4'
    def __init__(self, float4):
        pass


class type_specifierp84(type_specifier):
    # type_specifier --> 'half2'
    def __init__(self, half2):
        pass


class type_specifierp85(type_specifier):
    # type_specifier --> 'half3'
    def __init__(self, half3):
        pass


class type_specifierp86(type_specifier):
    # type_specifier --> 'half4'
    def __init__(self, half4):
        pass


class type_specifierp87(type_specifier):
    # type_specifier --> 'fixed2'
    def __init__(self, fixed2):
        pass


class type_specifierp88(type_specifier):
    # type_specifier --> 'fixed3'
    def __init__(self, fixed3):
        pass


class type_specifierp89(type_specifier):
    # type_specifier --> 'fixed4'
    def __init__(self, fixed4):
        pass


class type_specifierp90(type_specifier):
    # type_specifier --> typedef_name
    def __init__(self, typedef_name):
        self.typedef_name = typedef_name


class type_qualifierp91(type_qualifier):
    # type_qualifier --> 'uniform'
    def __init__(self, uniform):
        pass


class typedef_namep92(typedef_name):
    # typedef_name --> ID
    def __init__(self, ID):
        self.ID = ID


class struct_specifierp93(struct_specifier):
    # struct_specifier --> 'struct' ID
    def __init__(self, struct, ID):
        self.ID = ID


class struct_specifierp94(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list


class struct_dec_listp95(struct_dec_list):
    # struct_dec_list --> struct_dec
    def __init__(self, struct_dec):
        self.struct_dec = struct_dec


class struct_dec_listp96(struct_dec_list):
    # struct_dec_list --> struct_dec_list struct_dec
    def __init__(self, struct_dec_list, struct_dec):
        self.struct_dec_list = struct_dec_list
        self.struct_dec = struct_dec


class struct_decp97(struct_dec):
    # struct_dec --> type_specifier struct_declarator_list ;
    def __init__(self, type_specifier, struct_declarator_list, Semicolon):
        self.type_specifier = type_specifier
        self.struct_declarator_list = struct_declarator_list


class struct_declarator_listp98(struct_declarator_list):
    # struct_declarator_list --> struct_declarator
    def __init__(self, struct_declarator):
        self.struct_declarator = struct_declarator


class struct_declarator_listp99(struct_declarator_list):
    # struct_declarator_list --> struct_declarator_list , struct_declarator
    def __init__(self, struct_declarator_list, Comma, struct_declarator):
        self.struct_declarator_list = struct_declarator_list
        self.struct_declarator = struct_declarator


class struct_declaratorp100(struct_declarator):
    # struct_declarator --> declarator
    def __init__(self, declarator):
        self.declarator = declarator


class struct_declaratorp101(struct_declarator):
    # struct_declarator --> declarator : ID
    def __init__(self, declarator, Colon, ID):
        self.declarator = declarator
        self.ID = ID


class declaratorp102(declarator):
    # declarator --> ID
    def __init__(self, ID):
        self.ID = ID


class declaratorp103(declarator):
    # declarator --> ( declarator )
    def __init__(self, LParen, declarator, RParen):
        self.declarator = declarator


class declaratorp104(declarator):
    # declarator --> declarator ( parameter_list )
    def __init__(self, declarator, LParen, parameter_list, RParen):
        self.declarator = declarator
        self.parameter_list = parameter_list


class parameter_listp105(parameter_list):
    # parameter_list --> parameter_dec
    def __init__(self, parameter_dec):
        self.parameter_dec = parameter_dec


class parameter_listp106(parameter_list):
    # parameter_list --> parameter_list , parameter_dec
    def __init__(self, parameter_list, Comma, parameter_dec):
        self.parameter_list = parameter_list
        self.parameter_dec = parameter_dec


class parameter_decp107(parameter_dec):
    # parameter_dec --> type_specifier declarator
    def __init__(self, type_specifier, declarator):
        self.type_specifier = type_specifier
        self.declarator = declarator


class init_dec_listp108(init_dec_list):
    # init_dec_list --> ID
    def __init__(self, ID):
        self.ID = ID


class stmp109(stm):
    # stm --> exp_stm
    def __init__(self, exp_stm):
        self.exp_stm = exp_stm


class stmp110(stm):
    # stm --> compound_stm
    def __init__(self, compound_stm):
        self.compound_stm = compound_stm


class stmp111(stm):
    # stm --> selection_stm
    def __init__(self, selection_stm):
        self.selection_stm = selection_stm


class stmp112(stm):
    # stm --> iteration_stm
    def __init__(self, iteration_stm):
        self.iteration_stm = iteration_stm


class stmp113(stm):
    # stm --> jump_stm
    def __init__(self, jump_stm):
        self.jump_stm = jump_stm


class exp_stmp114(exp_stm):
    # exp_stm --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp


class exp_stmp115(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass


class compound_stmp116(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list


class compound_stmp117(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass


class block_item_listp118(block_item_list):
    # block_item_list --> block_item
    def __init__(self, block_item):
        self.block_item = block_item


class block_item_listp119(block_item_list):
    # block_item_list --> block_item_list block_item
    def __init__(self, block_item_list, block_item):
        self.block_item_list = block_item_list
        self.block_item = block_item


class block_itemp120(block_item):
    # block_item --> dec
    def __init__(self, dec):
        self.dec = dec


class block_itemp121(block_item):
    # block_item --> stm
    def __init__(self, stm):
        self.stm = stm


class selection_stmp122(selection_stm):
    # selection_stm --> 'if' ( exp ) stm
    def __init__(self, _if, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm


class selection_stmp123(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, _if, LParen, exp, RParen, stm1, _else, stm2):
        self.exp = exp
        self.stm1 = stm1
        self.stm2 = stm2


class iteration_stmp124(iteration_stm):
    # iteration_stm --> 'while' ( exp ) stm
    def __init__(self, _while, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm


class iteration_stmp125(iteration_stm):
    # iteration_stm --> 'do' stm 'while' ( exp ) ;
    def __init__(self, do, stm, _while, LParen, exp, RParen, Semicolon):
        self.stm = stm
        self.exp = exp


class iteration_stmp126(iteration_stm):
    # iteration_stm --> 'for' ( exp ; exp ; exp ) stm
    def __init__(self, _for, LParen, exp1, Semicolon1, exp2, Semicolon2, exp3, RParen, stm):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.stm = stm


class jump_stmp127(jump_stm):
    # jump_stm --> 'goto' ID
    def __init__(self, goto, ID):
        self.ID = ID


class jump_stmp128(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, _continue):
        pass


class jump_stmp129(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, _break):
        pass


class jump_stmp130(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, _return, exp, Semicolon):
        self.exp = exp


class Test(unittest.TestCase):


    def test(self):
        pass
