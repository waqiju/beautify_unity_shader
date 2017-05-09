from app.symbol_type import SymbolType
from app.syntax_nonterminal import Nonterminal
from app.formatter import I, AAI, IAA, SSI, ISS, GB, GA, RestoreComment
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

    def toCode(self):
        return I() + 'CGPROGRAM\n' + self.cg_prog.toCode() + I() + 'ENDCG\n'


class progp2(prog):
    # prog --> 'CGINCLUDE' cg_prog 'ENDCG'
    def __init__(self, CGINCLUDE, cg_prog, ENDCG):
        self.cg_prog = cg_prog

    def toCode(self):
        return I() + 'CGINCLUDE\n' + self.cg_prog.toCode() + 'ENDCG\n'


class cg_progp3(cg_prog):
    # cg_prog --> cg_stms
    def __init__(self, cg_stms):
        self.cg_stms = cg_stms

    def toCode(self):
        return self.cg_stms.toCode()


class cg_stmsp4(cg_stms):
    # cg_stms --> cg_stm cg_stms
    def __init__(self, cg_stm, cg_stms):
        self.cg_stm = cg_stm
        self.cg_stms = cg_stms

    def toCode(self):
        return self.cg_stm.toCode() + self.cg_stms.toCode()


class cg_stmsp5(cg_stms):
    # cg_stms -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class cg_stmp6(cg_stm):
    # cg_stm --> preprocessing_stm
    def __init__(self, preprocessing_stm):
        self.preprocessing_stm = preprocessing_stm

    def toCode(self):
        return self.preprocessing_stm.toCode()


class cg_stmp7(cg_stm):
    # cg_stm --> function_definition
    def __init__(self, function_definition):
        self.function_definition = function_definition

    def toCode(self):
        return self.function_definition.toCode()


class cg_stmp8(cg_stm):
    # cg_stm --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class function_definitionp9(function_definition):
    # function_definition --> dec_specifier declarator compound_stm
    def __init__(self, dec_specifier, declarator, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm

    def toCode(self):
        return GB() + I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + '\n' + self.compound_stm.toCode() + GA()


class function_definitionp10(function_definition):
    # function_definition --> dec_specifier declarator : ID compound_stm
    def __init__(self, dec_specifier, declarator, Colon, ID, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID = ID
        self.compound_stm = compound_stm

    def toCode(self):
        return GB() + I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + ' : ' + self.ID.toCode() + '\n' + self.compound_stm.toCode() + GA()


class preprocessing_stmp11(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class preprocessing_stmp12(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd

    def toCode(self):
        return self.pp_cmd.toCode()


class pp_if_stmp13(pp_if_stm):
    # pp_if_stm --> # 'if' ID
    def __init__(self, Pound, _if, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'if' + self.ID.toCode()


class pp_if_stmp14(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'ifdef' + self.ID.toCode()


class pp_if_stmp15(pp_if_stm):
    # pp_if_stm --> # 'ifndef' ID
    def __init__(self, Pound, ifndef, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'ifndef' + self.ID.toCode()


class pp_if_stmp16(pp_if_stm):
    # pp_if_stm --> # 'elif' ID
    def __init__(self, Pound, _elif, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'elif' + self.ID.toCode()


class pp_if_stmp17(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, _else):
        pass

    def toCode(self):
        return '#' + 'else'


class pp_if_stmp18(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass

    def toCode(self):
        return '#' + 'endif'


class pp_cmdp19(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String

    def toCode(self):
        return '#' + 'include' + self.String.toCode()


class pp_cmdp20(pp_cmd):
    # pp_cmd --> # 'pragma' ids_or_numbers Enter
    def __init__(self, Pound, pragma, ids_or_numbers, Enter):
        self.ids_or_numbers = ids_or_numbers

    def toCode(self):
        return I() + '#' + 'pragma' + self.ids_or_numbers.toCode() + '\n'


class ids_or_numbersp21(ids_or_numbers):
    # ids_or_numbers --> ID ids_or_numbers
    def __init__(self, ID, ids_or_numbers):
        self.ID = ID
        self.ids_or_numbers = ids_or_numbers

    def toCode(self):
        return ' ' + self.ID.toCode() + self.ids_or_numbers.toCode()


class ids_or_numbersp22(ids_or_numbers):
    # ids_or_numbers --> Number ids_or_numbers
    def __init__(self, Number, ids_or_numbers):
        self.Number = Number
        self.ids_or_numbers = ids_or_numbers

    def toCode(self):
        return self.Number.toCode() + self.ids_or_numbers.toCode()


class ids_or_numbersp23(ids_or_numbers):
    # ids_or_numbers -->
    def __init__(self):
        pass

    def toCode(self):
        return ''


class primary_expp24(primary_exp):
    # primary_exp --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class primary_expp25(primary_exp):
    # primary_exp --> String
    def __init__(self, String):
        self.String = String

    def toCode(self):
        return self.String.toCode()


class primary_expp26(primary_exp):
    # primary_exp --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class primary_expp27(primary_exp):
    # primary_exp --> ( exp )
    def __init__(self, LParen, exp, RParen):
        self.exp = exp

    def toCode(self):
        return '(' + self.exp.toCode() + ')'


class postfix_expp28(postfix_exp):
    # postfix_exp --> primary_exp
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def toCode(self):
        return self.primary_exp.toCode()


class postfix_expp29(postfix_exp):
    # postfix_exp --> postfix_exp [ exp ]
    def __init__(self, postfix_exp, LBrack, exp, RBrack):
        self.postfix_exp = postfix_exp
        self.exp = exp

    def toCode(self):
        return self.postfix_exp.toCode() + '[' + self.exp.toCode() + ']'


class postfix_expp30(postfix_exp):
    # postfix_exp --> postfix_exp ( )
    def __init__(self, postfix_exp, LParen, RParen):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '(' + ')'


class postfix_expp31(postfix_exp):
    # postfix_exp --> postfix_exp ( argument_exp_list )
    def __init__(self, postfix_exp, LParen, argument_exp_list, RParen):
        self.postfix_exp = postfix_exp
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return self.postfix_exp.toCode() + '(' + self.argument_exp_list.toCode() + ')'


class postfix_expp32(postfix_exp):
    # postfix_exp --> postfix_exp . ID
    def __init__(self, postfix_exp, Dot, ID):
        self.postfix_exp = postfix_exp
        self.ID = ID

    def toCode(self):
        return self.postfix_exp.toCode() + '.' + self.ID.toCode()


class postfix_expp33(postfix_exp):
    # postfix_exp --> postfix_exp ++
    def __init__(self, postfix_exp, Increment):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '++'


class postfix_expp34(postfix_exp):
    # postfix_exp --> postfix_exp --
    def __init__(self, postfix_exp, Decrement):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '--'


class argument_exp_listp35(argument_exp_list):
    # argument_exp_list --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class argument_exp_listp36(argument_exp_list):
    # argument_exp_list --> argument_exp_list , assignment_exp
    def __init__(self, argument_exp_list, Comma, assignment_exp):
        self.argument_exp_list = argument_exp_list
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.argument_exp_list.toCode() + ', ' + self.assignment_exp.toCode()


class unary_expp37(unary_exp):
    # unary_exp --> postfix_exp
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode()


class unary_expp38(unary_exp):
    # unary_exp --> ++ unary_exp
    def __init__(self, Increment, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return '++' + self.unary_exp.toCode()


class unary_expp39(unary_exp):
    # unary_exp --> -- unary_exp
    def __init__(self, Decrement, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return '--' + self.unary_exp.toCode()


class unary_expp40(unary_exp):
    # unary_exp --> unary_op unary_exp
    def __init__(self, unary_op, unary_exp):
        self.unary_op = unary_op
        self.unary_exp = unary_exp

    def toCode(self):
        return self.unary_op.toCode() + self.unary_exp.toCode()


class unary_opp41(unary_op):
    # unary_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class unary_opp42(unary_op):
    # unary_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class unary_opp43(unary_op):
    # unary_op --> !
    def __init__(self, NOT):
        pass

    def toCode(self):
        return '!'


class unary_opp44(unary_op):
    # unary_op --> ~
    def __init__(self, Tilde):
        pass

    def toCode(self):
        return '~'


class binary_expp45(binary_exp):
    # binary_exp --> unary_exp
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return self.unary_exp.toCode()


class binary_expp46(binary_exp):
    # binary_exp --> binary_exp binary_op unary_exp
    def __init__(self, binary_exp, binary_op, unary_exp):
        self.binary_exp = binary_exp
        self.binary_op = binary_op
        self.unary_exp = unary_exp

    def toCode(self):
        return self.binary_exp.toCode() + ' ' + self.binary_op.toCode() + ' ' + self.unary_exp.toCode()


class binary_opp47(binary_op):
    # binary_op --> *
    def __init__(self, Times):
        pass

    def toCode(self):
        return '*'


class binary_opp48(binary_op):
    # binary_op --> /
    def __init__(self, Divide):
        pass

    def toCode(self):
        return '/'


class binary_opp49(binary_op):
    # binary_op --> %
    def __init__(self, Percent):
        pass

    def toCode(self):
        return '%'


class binary_opp50(binary_op):
    # binary_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class binary_opp51(binary_op):
    # binary_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class binary_opp52(binary_op):
    # binary_op --> <<
    def __init__(self, LeftShift):
        pass

    def toCode(self):
        return '<<'


class binary_opp53(binary_op):
    # binary_op --> >>
    def __init__(self, RightShift):
        pass

    def toCode(self):
        return '>>'


class binary_opp54(binary_op):
    # binary_op --> <
    def __init__(self, LT):
        pass

    def toCode(self):
        return '<'


class binary_opp55(binary_op):
    # binary_op --> >
    def __init__(self, GT):
        pass

    def toCode(self):
        return '>'


class binary_opp56(binary_op):
    # binary_op --> <=
    def __init__(self, LE):
        pass

    def toCode(self):
        return '<='


class binary_opp57(binary_op):
    # binary_op --> >=
    def __init__(self, GE):
        pass

    def toCode(self):
        return '>='


class binary_opp58(binary_op):
    # binary_op --> ==
    def __init__(self, EQ):
        pass

    def toCode(self):
        return '=='


class binary_opp59(binary_op):
    # binary_op --> !=
    def __init__(self, NEQ):
        pass

    def toCode(self):
        return '!='


class binary_opp60(binary_op):
    # binary_op --> &
    def __init__(self, Ampersand):
        pass

    def toCode(self):
        return '&'


class binary_opp61(binary_op):
    # binary_op --> ^
    def __init__(self, Caret):
        pass

    def toCode(self):
        return '^'


class binary_opp62(binary_op):
    # binary_op --> |
    def __init__(self, VerticalBar):
        pass

    def toCode(self):
        return '|'


class binary_opp63(binary_op):
    # binary_op --> &&
    def __init__(self, AND):
        pass

    def toCode(self):
        return '&&'


class binary_opp64(binary_op):
    # binary_op --> ||
    def __init__(self, OR):
        pass

    def toCode(self):
        return '||'


class conditional_expp65(conditional_exp):
    # conditional_exp --> binary_exp
    def __init__(self, binary_exp):
        self.binary_exp = binary_exp

    def toCode(self):
        return self.binary_exp.toCode()


class conditional_expp66(conditional_exp):
    # conditional_exp --> binary_exp ? exp : conditional_exp
    def __init__(self, binary_exp, Question, exp, Colon, conditional_exp):
        self.binary_exp = binary_exp
        self.exp = exp
        self.conditional_exp = conditional_exp

    def toCode(self):
        return self.binary_exp.toCode() + '?' + self.exp.toCode() + ':' + self.conditional_exp.toCode()


class assignment_expp67(assignment_exp):
    # assignment_exp --> conditional_exp
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp

    def toCode(self):
        return self.conditional_exp.toCode()


class assignment_expp68(assignment_exp):
    # assignment_exp --> unary_exp assignment_op assignment_exp
    def __init__(self, unary_exp, assignment_op, assignment_exp):
        self.unary_exp = unary_exp
        self.assignment_op = assignment_op
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.unary_exp.toCode() + ' ' + self.assignment_op.toCode() + ' ' + self.assignment_exp.toCode()


class assignment_opp69(assignment_op):
    # assignment_op --> =
    def __init__(self, Assign):
        pass

    def toCode(self):
        return '='


class assignment_opp70(assignment_op):
    # assignment_op --> *=
    def __init__(self, AddAssign):
        pass

    def toCode(self):
        return '*='


class assignment_opp71(assignment_op):
    # assignment_op --> /=
    def __init__(self, SubAssign):
        pass

    def toCode(self):
        return '/='


class assignment_opp72(assignment_op):
    # assignment_op --> %=
    def __init__(self, MulAssign):
        pass

    def toCode(self):
        return '%='


class assignment_opp73(assignment_op):
    # assignment_op --> +=
    def __init__(self, DivAssign):
        pass

    def toCode(self):
        return '+='


class assignment_opp74(assignment_op):
    # assignment_op --> -=
    def __init__(self, ModAssign):
        pass

    def toCode(self):
        return '-='


class assignment_opp75(assignment_op):
    # assignment_op --> <<=
    def __init__(self, LeftShiftAssign):
        pass

    def toCode(self):
        return '<<='


class assignment_opp76(assignment_op):
    # assignment_op --> >>=
    def __init__(self, RightShiftAssign):
        pass

    def toCode(self):
        return '>>='


class assignment_opp77(assignment_op):
    # assignment_op --> &=
    def __init__(self, AndAssign):
        pass

    def toCode(self):
        return '&='


class assignment_opp78(assignment_op):
    # assignment_op --> ^=
    def __init__(self, XorAssign):
        pass

    def toCode(self):
        return '^='


class assignment_opp79(assignment_op):
    # assignment_op --> |=
    def __init__(self, OrAssign):
        pass

    def toCode(self):
        return '|='


class expp80(exp):
    # exp --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class expp81(exp):
    # exp --> exp , assignment_exp
    def __init__(self, exp, Comma, assignment_exp):
        self.exp = exp
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.exp.toCode() + ',' + self.assignment_exp.toCode()


class decp82(dec):
    # dec --> struct_specifier ;
    def __init__(self, struct_specifier, Semicolon):
        self.struct_specifier = struct_specifier

    def toCode(self):
        return GB() + I() + self.struct_specifier.toCode() + ';\n' + GA()


class decp83(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list

    def toCode(self):
        return I() + self.dec_specifier.toCode() + ' ' + self.init_dec_list.toCode() + ';\n'


class dec_specifierp84(dec_specifier):
    # dec_specifier --> type_specifier
    def __init__(self, type_specifier):
        self.type_specifier = type_specifier

    def toCode(self):
        return self.type_specifier.toCode()


class dec_specifierp85(dec_specifier):
    # dec_specifier --> type_qualifier type_specifier
    def __init__(self, type_qualifier, type_specifier):
        self.type_qualifier = type_qualifier
        self.type_specifier = type_specifier

    def toCode(self):
        return self.type_qualifier.toCode() + ' ' + self.type_specifier.toCode()


class type_specifierp86(type_specifier):
    # type_specifier --> 'void'
    def __init__(self, void):
        pass

    def toCode(self):
        return 'void'


class type_specifierp87(type_specifier):
    # type_specifier --> 'char'
    def __init__(self, char):
        pass

    def toCode(self):
        return 'char'


class type_specifierp88(type_specifier):
    # type_specifier --> 'short'
    def __init__(self, short):
        pass

    def toCode(self):
        return 'short'


class type_specifierp89(type_specifier):
    # type_specifier --> 'int'
    def __init__(self, int):
        pass

    def toCode(self):
        return 'int'


class type_specifierp90(type_specifier):
    # type_specifier --> 'long'
    def __init__(self, long):
        pass

    def toCode(self):
        return 'long'


class type_specifierp91(type_specifier):
    # type_specifier --> 'float'
    def __init__(self, float):
        pass

    def toCode(self):
        return 'float'


class type_specifierp92(type_specifier):
    # type_specifier --> 'double'
    def __init__(self, double):
        pass

    def toCode(self):
        return 'double'


class type_specifierp93(type_specifier):
    # type_specifier --> 'sampler2D'
    def __init__(self, sampler2D):
        pass

    def toCode(self):
        return 'sampler2D'


class type_specifierp94(type_specifier):
    # type_specifier --> 'float2'
    def __init__(self, float2):
        pass

    def toCode(self):
        return 'float2'


class type_specifierp95(type_specifier):
    # type_specifier --> 'float3'
    def __init__(self, float3):
        pass

    def toCode(self):
        return 'float3'


class type_specifierp96(type_specifier):
    # type_specifier --> 'float4'
    def __init__(self, float4):
        pass

    def toCode(self):
        return 'float4'


class type_specifierp97(type_specifier):
    # type_specifier --> 'half2'
    def __init__(self, half2):
        pass

    def toCode(self):
        return 'half2'


class type_specifierp98(type_specifier):
    # type_specifier --> 'half3'
    def __init__(self, half3):
        pass

    def toCode(self):
        return 'half3'


class type_specifierp99(type_specifier):
    # type_specifier --> 'half4'
    def __init__(self, half4):
        pass

    def toCode(self):
        return 'half4'


class type_specifierp100(type_specifier):
    # type_specifier --> 'fixed2'
    def __init__(self, fixed2):
        pass

    def toCode(self):
        return 'fixed2'


class type_specifierp101(type_specifier):
    # type_specifier --> 'fixed3'
    def __init__(self, fixed3):
        pass

    def toCode(self):
        return 'fixed3'


class type_specifierp102(type_specifier):
    # type_specifier --> 'fixed4'
    def __init__(self, fixed4):
        pass

    def toCode(self):
        return 'fixed4'


class type_specifierp103(type_specifier):
    # type_specifier --> typedef_name
    def __init__(self, typedef_name):
        self.typedef_name = typedef_name

    def toCode(self):
        return self.typedef_name.toCode()


class type_qualifierp104(type_qualifier):
    # type_qualifier --> 'uniform'
    def __init__(self, uniform):
        pass

    def toCode(self):
        return 'uniform'


class type_qualifierp105(type_qualifier):
    # type_qualifier --> 'inout'
    def __init__(self, inout):
        pass

    def toCode(self):
        return 'inout'


class typedef_namep106(typedef_name):
    # typedef_name --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class struct_specifierp107(struct_specifier):
    # struct_specifier --> 'struct' ID
    def __init__(self, struct, ID):
        self.ID = ID

    def toCode(self):
        return 'struct ' + self.ID.toCode()


class struct_specifierp108(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list

    def toCode(self):
        return 'struct ' + self.ID.toCode() + '\n' + IAA() + '{' + '\n' + self.struct_dec_list.toCode() + SSI() + '}'


class struct_dec_listp109(struct_dec_list):
    # struct_dec_list --> struct_dec
    def __init__(self, struct_dec):
        self.struct_dec = struct_dec

    def toCode(self):
        return self.struct_dec.toCode()


class struct_dec_listp110(struct_dec_list):
    # struct_dec_list --> struct_dec_list struct_dec
    def __init__(self, struct_dec_list, struct_dec):
        self.struct_dec_list = struct_dec_list
        self.struct_dec = struct_dec

    def toCode(self):
        return self.struct_dec_list.toCode() + self.struct_dec.toCode()


class struct_decp111(struct_dec):
    # struct_dec --> type_specifier struct_declarator_list ;
    def __init__(self, type_specifier, struct_declarator_list, Semicolon):
        self.type_specifier = type_specifier
        self.struct_declarator_list = struct_declarator_list

    def toCode(self):
        return I() + self.type_specifier.toCode() + ' ' + self.struct_declarator_list.toCode() + ';\n'


class struct_declarator_listp112(struct_declarator_list):
    # struct_declarator_list --> struct_declarator
    def __init__(self, struct_declarator):
        self.struct_declarator = struct_declarator

    def toCode(self):
        return self.struct_declarator.toCode()


class struct_declarator_listp113(struct_declarator_list):
    # struct_declarator_list --> struct_declarator_list , struct_declarator
    def __init__(self, struct_declarator_list, Comma, struct_declarator):
        self.struct_declarator_list = struct_declarator_list
        self.struct_declarator = struct_declarator

    def toCode(self):
        return self.struct_declarator_list.toCode() + ',' + self.struct_declarator.toCode()


class struct_declaratorp114(struct_declarator):
    # struct_declarator --> declarator
    def __init__(self, declarator):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode()


class struct_declaratorp115(struct_declarator):
    # struct_declarator --> declarator : ID
    def __init__(self, declarator, Colon, ID):
        self.declarator = declarator
        self.ID = ID

    def toCode(self):
        return self.declarator.toCode() + ' : ' + self.ID.toCode()


class declaratorp116(declarator):
    # declarator --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class declaratorp117(declarator):
    # declarator --> declarator [ exp ]
    def __init__(self, declarator, LBrack, exp, RBrack):
        self.declarator = declarator
        self.exp = exp

    def toCode(self):
        return self.declarator.toCode() + '[' + self.exp.toCode() + ']'


class declaratorp118(declarator):
    # declarator --> declarator ( parameter_list )
    def __init__(self, declarator, LParen, parameter_list, RParen):
        self.declarator = declarator
        self.parameter_list = parameter_list

    def toCode(self):
        return self.declarator.toCode() + '(' + self.parameter_list.toCode() + ')'


class parameter_listp119(parameter_list):
    # parameter_list --> parameter_dec
    def __init__(self, parameter_dec):
        self.parameter_dec = parameter_dec

    def toCode(self):
        return self.parameter_dec.toCode()


class parameter_listp120(parameter_list):
    # parameter_list --> parameter_list , parameter_dec
    def __init__(self, parameter_list, Comma, parameter_dec):
        self.parameter_list = parameter_list
        self.parameter_dec = parameter_dec

    def toCode(self):
        return self.parameter_list.toCode() + ', ' + self.parameter_dec.toCode()


class parameter_decp121(parameter_dec):
    # parameter_dec --> dec_specifier declarator
    def __init__(self, dec_specifier, declarator):
        self.dec_specifier = dec_specifier
        self.declarator = declarator

    def toCode(self):
        return self.dec_specifier.toCode() + ' ' + self.declarator.toCode()


class init_dec_listp122(init_dec_list):
    # init_dec_list --> init_dec
    def __init__(self, init_dec):
        self.init_dec = init_dec

    def toCode(self):
        return self.init_dec.toCode()


class init_dec_listp123(init_dec_list):
    # init_dec_list --> init_dec_list , init_dec
    def __init__(self, init_dec_list, Comma, init_dec):
        self.init_dec_list = init_dec_list
        self.init_dec = init_dec

    def toCode(self):
        return self.init_dec_list.toCode() + ',' + self.init_dec.toCode()


class init_decp124(init_dec):
    # init_dec --> declarator
    def __init__(self, declarator):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode()


class init_decp125(init_dec):
    # init_dec --> declarator = assignment_exp
    def __init__(self, declarator, Assign, assignment_exp):
        self.declarator = declarator
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.declarator.toCode() + ' = ' + self.assignment_exp.toCode()


class stmp126(stm):
    # stm --> exp_stm
    def __init__(self, exp_stm):
        self.exp_stm = exp_stm

    def toCode(self):
        return self.exp_stm.toCode()


class stmp127(stm):
    # stm --> compound_stm
    def __init__(self, compound_stm):
        self.compound_stm = compound_stm

    def toCode(self):
        return self.compound_stm.toCode()


class stmp128(stm):
    # stm --> selection_stm
    def __init__(self, selection_stm):
        self.selection_stm = selection_stm

    def toCode(self):
        return self.selection_stm.toCode()


class stmp129(stm):
    # stm --> iteration_stm
    def __init__(self, iteration_stm):
        self.iteration_stm = iteration_stm

    def toCode(self):
        return self.iteration_stm.toCode()


class stmp130(stm):
    # stm --> jump_stm
    def __init__(self, jump_stm):
        self.jump_stm = jump_stm

    def toCode(self):
        return self.jump_stm.toCode()


class exp_stmp131(exp_stm):
    # exp_stm --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return I() + self.exp.toCode() + ';\n'


class exp_stmp132(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass

    def toCode(self):
        return I() + ';\n'


class compound_stmp133(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list

    def toCode(self):
        return IAA() + '{' + '\n'+ self.block_item_list.toCode() + SSI() + '}' + '\n'


class compound_stmp134(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass

    def toCode(self):
        return I() + '{\n' +I() + '}\n'


class block_item_listp135(block_item_list):
    # block_item_list --> block_item
    def __init__(self, block_item):
        self.block_item = block_item

    def toCode(self):
        return self.block_item.toCode()


class block_item_listp136(block_item_list):
    # block_item_list --> block_item_list block_item
    def __init__(self, block_item_list, block_item):
        self.block_item_list = block_item_list
        self.block_item = block_item

    def toCode(self):
        return self.block_item_list.toCode() + self.block_item.toCode()


class block_itemp137(block_item):
    # block_item --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class block_itemp138(block_item):
    # block_item --> stm
    def __init__(self, stm):
        self.stm = stm

    def toCode(self):
        return self.stm.toCode()


class selection_stmp139(selection_stm):
    # selection_stm --> 'if' ( exp ) stm
    def __init__(self, _if, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm

    def toCode(self):
        return I() + 'if ' + '(' + self.exp.toCode() + ')\n' + self.stm.toCode()


class selection_stmp140(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, _if, LParen, exp, RParen, stm1, _else, stm2):
        self.exp = exp
        self.stm1 = stm1
        self.stm2 = stm2

    def toCode(self):
        return I() + 'if ' + '(' + self.exp.toCode() + ')\n' + self.stm.toCode() + I() + 'else' + self.stm.toCode()


class iteration_stmp141(iteration_stm):
    # iteration_stm --> 'while' ( exp ) stm
    def __init__(self, _while, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm

    def toCode(self):
        return 'while' + '(' + self.exp.toCode() + ')' + self.stm.toCode()


class iteration_stmp142(iteration_stm):
    # iteration_stm --> 'do' stm 'while' ( exp ) ;
    def __init__(self, do, stm, _while, LParen, exp, RParen, Semicolon):
        self.stm = stm
        self.exp = exp

    def toCode(self):
        return 'do' + self.stm.toCode() + 'while' + '(' + self.exp.toCode() + ')' + ';'


class iteration_stmp143(iteration_stm):
    # iteration_stm --> 'for' ( exp ; exp ; exp ) stm
    def __init__(self, _for, LParen, exp1, Semicolon1, exp2, Semicolon2, exp3, RParen, stm):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.stm = stm

    def toCode(self):
        return 'for' + '(' + self.exp.toCode() + ';' + self.exp.toCode() + ';' + self.exp.toCode() + ')' + self.stm.toCode()


class jump_stmp144(jump_stm):
    # jump_stm --> 'goto' ID
    def __init__(self, goto, ID):
        self.ID = ID

    def toCode(self):
        return I() + 'goto' + self.ID.toCode() + '\n'


class jump_stmp145(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, _continue):
        pass

    def toCode(self):
        return I() + 'continue' + '\n'


class jump_stmp146(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, _break):
        pass

    def toCode(self):
        return I() + 'break' + '\n'


class jump_stmp147(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, _return, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return I() + 'return ' + self.exp.toCode() + ';\n'


class Test(unittest.TestCase):


    def test(self):
        pass