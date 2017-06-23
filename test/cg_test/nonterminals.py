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


class cg_stmp9(cg_stm):
    # cg_stm --> 'CBUFFER_START' ( ID ) dec_list 'CBUFFER_END'
    def __init__(self, CBUFFER_START, LParen, ID, RParen, dec_list, CBUFFER_END):
        self.ID = ID
        self.dec_list = dec_list

    def toCode(self):
        return 'CBUFFER_START' + '(' + self.ID.toCode() + ')' + self.dec_list.toCode() + 'CBUFFER_END'


class function_definitionp10(function_definition):
    # function_definition --> dec_specifier declarator compound_stm
    def __init__(self, dec_specifier, declarator, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm

    def toCode(self):
        return GB() + I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + '\n' + self.compound_stm.toCode() + GA()


class function_definitionp11(function_definition):
    # function_definition --> dec_specifier declarator : ID compound_stm
    def __init__(self, dec_specifier, declarator, Colon, ID, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID = ID
        self.compound_stm = compound_stm

    def toCode(self):
        return GB() + I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + ' : ' + self.ID.toCode() + '\n' + self.compound_stm.toCode() + GA()


class function_definitionp12(function_definition):
    # function_definition --> [ ID ( Number ) ] dec_specifier declarator compound_stm
    def __init__(self, LBrack, ID, LParen, Number, RParen, RBrack, dec_specifier, declarator, compound_stm):
        self.ID = ID
        self.Number = Number
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm

    def toCode(self):
        return '[' + self.ID.toCode() + '(' + self.Number.toCode() + ')' + ']' + self.dec_specifier.toCode() + self.declarator.toCode() + self.compound_stm.toCode()


class function_definitionp13(function_definition):
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


class preprocessing_stmp14(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class preprocessing_stmp15(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd

    def toCode(self):
        return self.pp_cmd.toCode()


class preprocessing_stmp16(preprocessing_stm):
    # preprocessing_stm --> marco_unfold
    def __init__(self, marco_unfold):
        self.marco_unfold = marco_unfold

    def toCode(self):
        return self.marco_unfold.toCode()


class pp_if_stmp17(pp_if_stm):
    # pp_if_stm --> # 'if' PPTokens
    def __init__(self, Pound, _if, PPTokens):
        self.PPTokens = PPTokens

    def toCode(self):
        return '#' + 'if' + self.PPTokens.toCode()


class pp_if_stmp18(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'ifdef' + self.ID.toCode()


class pp_if_stmp19(pp_if_stm):
    # pp_if_stm --> # 'ifndef' ID
    def __init__(self, Pound, ifndef, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'ifndef' + self.ID.toCode()


class pp_if_stmp20(pp_if_stm):
    # pp_if_stm --> # 'elif' PPTokens
    def __init__(self, Pound, _elif, PPTokens):
        self.PPTokens = PPTokens

    def toCode(self):
        return '#' + 'elif' + self.PPTokens.toCode()


class pp_if_stmp21(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, _else):
        pass

    def toCode(self):
        return '#' + 'else'


class pp_if_stmp22(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass

    def toCode(self):
        return '#' + 'endif'


class pp_cmdp23(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String

    def toCode(self):
        return '#' + 'include' + self.String.toCode()


class pp_cmdp24(pp_cmd):
    # pp_cmd --> # 'pragma' PPTokens
    def __init__(self, Pound, pragma, PPTokens):
        self.PPTokens = PPTokens

    def toCode(self):
        return '#' + 'pragma' + self.PPTokens.toCode()


class pp_cmdp25(pp_cmd):
    # pp_cmd --> # 'define' PPTokens
    def __init__(self, Pound, define, PPTokens):
        self.PPTokens = PPTokens

    def toCode(self):
        return '#' + 'define' + self.PPTokens.toCode()


class marco_unfoldp26(marco_unfold):
    # marco_unfold --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return self.exp.toCode() + ';'


class dec_listp27(dec_list):
    # dec_list --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class dec_listp28(dec_list):
    # dec_list --> dec_list dec
    def __init__(self, dec_list, dec):
        self.dec_list = dec_list
        self.dec = dec

    def toCode(self):
        return self.dec_list.toCode() + self.dec.toCode()


class primary_expp29(primary_exp):
    # primary_exp --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class primary_expp30(primary_exp):
    # primary_exp --> String
    def __init__(self, String):
        self.String = String

    def toCode(self):
        return self.String.toCode()


class primary_expp31(primary_exp):
    # primary_exp --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class primary_expp32(primary_exp):
    # primary_exp --> ( exp )
    def __init__(self, LParen, exp, RParen):
        self.exp = exp

    def toCode(self):
        return '(' + self.exp.toCode() + ')'


class postfix_expp33(postfix_exp):
    # postfix_exp --> primary_exp
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def toCode(self):
        return self.primary_exp.toCode()


class postfix_expp34(postfix_exp):
    # postfix_exp --> postfix_exp [ exp ]
    def __init__(self, postfix_exp, LBrack, exp, RBrack):
        self.postfix_exp = postfix_exp
        self.exp = exp

    def toCode(self):
        return self.postfix_exp.toCode() + '[' + self.exp.toCode() + ']'


class postfix_expp35(postfix_exp):
    # postfix_exp --> postfix_exp ( )
    def __init__(self, postfix_exp, LParen, RParen):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '(' + ')'


class postfix_expp36(postfix_exp):
    # postfix_exp --> postfix_exp ( argument_exp_list )
    def __init__(self, postfix_exp, LParen, argument_exp_list, RParen):
        self.postfix_exp = postfix_exp
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return self.postfix_exp.toCode() + '(' + self.argument_exp_list.toCode() + ')'


class postfix_expp37(postfix_exp):
    # postfix_exp --> buildin_type_name ( argument_exp_list )
    def __init__(self, buildin_type_name, LParen, argument_exp_list, RParen):
        self.buildin_type_name = buildin_type_name
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return self.buildin_type_name.toCode() + '(' + self.argument_exp_list.toCode() + ')'


class postfix_expp38(postfix_exp):
    # postfix_exp --> postfix_exp . ID
    def __init__(self, postfix_exp, Dot, ID):
        self.postfix_exp = postfix_exp
        self.ID = ID

    def toCode(self):
        return self.postfix_exp.toCode() + '.' + self.ID.toCode()


class postfix_expp39(postfix_exp):
    # postfix_exp --> postfix_exp ++
    def __init__(self, postfix_exp, Increment):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '++'


class postfix_expp40(postfix_exp):
    # postfix_exp --> postfix_exp --
    def __init__(self, postfix_exp, Decrement):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '--'


class argument_exp_listp41(argument_exp_list):
    # argument_exp_list --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class argument_exp_listp42(argument_exp_list):
    # argument_exp_list --> argument_exp_list , assignment_exp
    def __init__(self, argument_exp_list, Comma, assignment_exp):
        self.argument_exp_list = argument_exp_list
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.argument_exp_list.toCode() + ', ' + self.assignment_exp.toCode()


class unary_expp43(unary_exp):
    # unary_exp --> postfix_exp
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode()


class unary_expp44(unary_exp):
    # unary_exp --> ++ unary_exp
    def __init__(self, Increment, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return '++' + self.unary_exp.toCode()


class unary_expp45(unary_exp):
    # unary_exp --> -- unary_exp
    def __init__(self, Decrement, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return '--' + self.unary_exp.toCode()


class unary_expp46(unary_exp):
    # unary_exp --> unary_op unary_exp
    def __init__(self, unary_op, unary_exp):
        self.unary_op = unary_op
        self.unary_exp = unary_exp

    def toCode(self):
        return self.unary_op.toCode() + self.unary_exp.toCode()


class unary_opp47(unary_op):
    # unary_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class unary_opp48(unary_op):
    # unary_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class unary_opp49(unary_op):
    # unary_op --> !
    def __init__(self, NOT):
        pass

    def toCode(self):
        return '!'


class unary_opp50(unary_op):
    # unary_op --> ~
    def __init__(self, Tilde):
        pass

    def toCode(self):
        return '~'


class cast_expp51(cast_exp):
    # cast_exp --> unary_exp
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return self.unary_exp.toCode()


class cast_expp52(cast_exp):
    # cast_exp --> ( buildin_type_name ) cast_exp
    def __init__(self, LParen, buildin_type_name, RParen, cast_exp):
        self.buildin_type_name = buildin_type_name
        self.cast_exp = cast_exp

    def toCode(self):
        return '(' + self.buildin_type_name.toCode() + ')' + self.cast_exp.toCode()


class binary_expp53(binary_exp):
    # binary_exp --> cast_exp
    def __init__(self, cast_exp):
        self.cast_exp = cast_exp

    def toCode(self):
        return self.cast_exp.toCode()


class binary_expp54(binary_exp):
    # binary_exp --> binary_exp binary_op unary_exp
    def __init__(self, binary_exp, binary_op, unary_exp):
        self.binary_exp = binary_exp
        self.binary_op = binary_op
        self.unary_exp = unary_exp

    def toCode(self):
        return self.binary_exp.toCode() + ' ' + self.binary_op.toCode() + ' ' + self.unary_exp.toCode()


class binary_opp55(binary_op):
    # binary_op --> *
    def __init__(self, Times):
        pass

    def toCode(self):
        return '*'


class binary_opp56(binary_op):
    # binary_op --> /
    def __init__(self, Divide):
        pass

    def toCode(self):
        return '/'


class binary_opp57(binary_op):
    # binary_op --> %
    def __init__(self, Percent):
        pass

    def toCode(self):
        return '%'


class binary_opp58(binary_op):
    # binary_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class binary_opp59(binary_op):
    # binary_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class binary_opp60(binary_op):
    # binary_op --> <<
    def __init__(self, LeftShift):
        pass

    def toCode(self):
        return '<<'


class binary_opp61(binary_op):
    # binary_op --> >>
    def __init__(self, RightShift):
        pass

    def toCode(self):
        return '>>'


class binary_opp62(binary_op):
    # binary_op --> <
    def __init__(self, LT):
        pass

    def toCode(self):
        return '<'


class binary_opp63(binary_op):
    # binary_op --> >
    def __init__(self, GT):
        pass

    def toCode(self):
        return '>'


class binary_opp64(binary_op):
    # binary_op --> <=
    def __init__(self, LE):
        pass

    def toCode(self):
        return '<='


class binary_opp65(binary_op):
    # binary_op --> >=
    def __init__(self, GE):
        pass

    def toCode(self):
        return '>='


class binary_opp66(binary_op):
    # binary_op --> ==
    def __init__(self, EQ):
        pass

    def toCode(self):
        return '=='


class binary_opp67(binary_op):
    # binary_op --> !=
    def __init__(self, NEQ):
        pass

    def toCode(self):
        return '!='


class binary_opp68(binary_op):
    # binary_op --> &
    def __init__(self, Ampersand):
        pass

    def toCode(self):
        return '&'


class binary_opp69(binary_op):
    # binary_op --> ^
    def __init__(self, Caret):
        pass

    def toCode(self):
        return '^'


class binary_opp70(binary_op):
    # binary_op --> |
    def __init__(self, VerticalBar):
        pass

    def toCode(self):
        return '|'


class binary_opp71(binary_op):
    # binary_op --> &&
    def __init__(self, AND):
        pass

    def toCode(self):
        return '&&'


class binary_opp72(binary_op):
    # binary_op --> ||
    def __init__(self, OR):
        pass

    def toCode(self):
        return '||'


class conditional_expp73(conditional_exp):
    # conditional_exp --> binary_exp
    def __init__(self, binary_exp):
        self.binary_exp = binary_exp

    def toCode(self):
        return self.binary_exp.toCode()


class conditional_expp74(conditional_exp):
    # conditional_exp --> binary_exp ? exp : conditional_exp
    def __init__(self, binary_exp, Question, exp, Colon, conditional_exp):
        self.binary_exp = binary_exp
        self.exp = exp
        self.conditional_exp = conditional_exp

    def toCode(self):
        return self.binary_exp.toCode() + '?' + self.exp.toCode() + ':' + self.conditional_exp.toCode()


class assignment_expp75(assignment_exp):
    # assignment_exp --> conditional_exp
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp

    def toCode(self):
        return self.conditional_exp.toCode()


class assignment_expp76(assignment_exp):
    # assignment_exp --> unary_exp assignment_op assignment_exp
    def __init__(self, unary_exp, assignment_op, assignment_exp):
        self.unary_exp = unary_exp
        self.assignment_op = assignment_op
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.unary_exp.toCode() + ' ' + self.assignment_op.toCode() + ' ' + self.assignment_exp.toCode()


class assignment_opp77(assignment_op):
    # assignment_op --> =
    def __init__(self, Assign):
        pass

    def toCode(self):
        return '='


class assignment_opp78(assignment_op):
    # assignment_op --> *=
    def __init__(self, AddAssign):
        pass

    def toCode(self):
        return '*='


class assignment_opp79(assignment_op):
    # assignment_op --> /=
    def __init__(self, SubAssign):
        pass

    def toCode(self):
        return '/='


class assignment_opp80(assignment_op):
    # assignment_op --> %=
    def __init__(self, MulAssign):
        pass

    def toCode(self):
        return '%='


class assignment_opp81(assignment_op):
    # assignment_op --> +=
    def __init__(self, DivAssign):
        pass

    def toCode(self):
        return '+='


class assignment_opp82(assignment_op):
    # assignment_op --> -=
    def __init__(self, ModAssign):
        pass

    def toCode(self):
        return '-='


class assignment_opp83(assignment_op):
    # assignment_op --> <<=
    def __init__(self, LeftShiftAssign):
        pass

    def toCode(self):
        return '<<='


class assignment_opp84(assignment_op):
    # assignment_op --> >>=
    def __init__(self, RightShiftAssign):
        pass

    def toCode(self):
        return '>>='


class assignment_opp85(assignment_op):
    # assignment_op --> &=
    def __init__(self, AndAssign):
        pass

    def toCode(self):
        return '&='


class assignment_opp86(assignment_op):
    # assignment_op --> ^=
    def __init__(self, XorAssign):
        pass

    def toCode(self):
        return '^='


class assignment_opp87(assignment_op):
    # assignment_op --> |=
    def __init__(self, OrAssign):
        pass

    def toCode(self):
        return '|='


class expp88(exp):
    # exp --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class expp89(exp):
    # exp --> exp , assignment_exp
    def __init__(self, exp, Comma, assignment_exp):
        self.exp = exp
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.exp.toCode() + ',' + self.assignment_exp.toCode()


class decp90(dec):
    # dec --> struct_specifier ;
    def __init__(self, struct_specifier, Semicolon):
        self.struct_specifier = struct_specifier

    def toCode(self):
        return GB() + I() + self.struct_specifier.toCode() + ';\n' + GA()


class decp91(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list

    def toCode(self):
        return I() + self.dec_specifier.toCode() + ' ' + self.init_dec_list.toCode() + ';\n'


class dec_specifierp92(dec_specifier):
    # dec_specifier --> type_specifier
    def __init__(self, type_specifier):
        self.type_specifier = type_specifier

    def toCode(self):
        return self.type_specifier.toCode()


class dec_specifierp93(dec_specifier):
    # dec_specifier --> type_qualifier dec_specifier
    def __init__(self, type_qualifier, dec_specifier):
        self.type_qualifier = type_qualifier
        self.dec_specifier = dec_specifier

    def toCode(self):
        return self.type_qualifier.toCode() + self.dec_specifier.toCode()


class dec_specifierp94(dec_specifier):
    # dec_specifier --> storage_class_specifier dec_specifier
    def __init__(self, storage_class_specifier, dec_specifier):
        self.storage_class_specifier = storage_class_specifier
        self.dec_specifier = dec_specifier

    def toCode(self):
        return self.storage_class_specifier.toCode() + self.dec_specifier.toCode()


class type_specifierp95(type_specifier):
    # type_specifier --> buildin_type_name
    def __init__(self, buildin_type_name):
        self.buildin_type_name = buildin_type_name

    def toCode(self):
        return self.buildin_type_name.toCode()


class type_specifierp96(type_specifier):
    # type_specifier --> typedef_name
    def __init__(self, typedef_name):
        self.typedef_name = typedef_name

    def toCode(self):
        return self.typedef_name.toCode()


class buildin_type_namep97(buildin_type_name):
    # buildin_type_name --> 'void'
    def __init__(self, void):
        pass

    def toCode(self):
        return 'void'


class buildin_type_namep98(buildin_type_name):
    # buildin_type_name --> 'char'
    def __init__(self, char):
        pass

    def toCode(self):
        return 'char'


class buildin_type_namep99(buildin_type_name):
    # buildin_type_name --> 'short'
    def __init__(self, short):
        pass

    def toCode(self):
        return 'short'


class buildin_type_namep100(buildin_type_name):
    # buildin_type_name --> 'int'
    def __init__(self, int):
        pass

    def toCode(self):
        return 'int'


class buildin_type_namep101(buildin_type_name):
    # buildin_type_name --> 'long'
    def __init__(self, long):
        pass

    def toCode(self):
        return 'long'


class buildin_type_namep102(buildin_type_name):
    # buildin_type_name --> 'fixed'
    def __init__(self, fixed):
        pass

    def toCode(self):
        return 'fixed'


class buildin_type_namep103(buildin_type_name):
    # buildin_type_name --> 'half'
    def __init__(self, half):
        pass

    def toCode(self):
        return 'half'


class buildin_type_namep104(buildin_type_name):
    # buildin_type_name --> 'float'
    def __init__(self, float):
        pass

    def toCode(self):
        return 'float'


class buildin_type_namep105(buildin_type_name):
    # buildin_type_name --> 'double'
    def __init__(self, double):
        pass

    def toCode(self):
        return 'double'


class buildin_type_namep106(buildin_type_name):
    # buildin_type_name --> 'sampler2D'
    def __init__(self, sampler2D):
        pass

    def toCode(self):
        return 'sampler2D'


class buildin_type_namep107(buildin_type_name):
    # buildin_type_name --> 'float2'
    def __init__(self, float2):
        pass

    def toCode(self):
        return 'float2'


class buildin_type_namep108(buildin_type_name):
    # buildin_type_name --> 'float3'
    def __init__(self, float3):
        pass

    def toCode(self):
        return 'float3'


class buildin_type_namep109(buildin_type_name):
    # buildin_type_name --> 'float4'
    def __init__(self, float4):
        pass

    def toCode(self):
        return 'float4'


class buildin_type_namep110(buildin_type_name):
    # buildin_type_name --> 'half2'
    def __init__(self, half2):
        pass

    def toCode(self):
        return 'half2'


class buildin_type_namep111(buildin_type_name):
    # buildin_type_name --> 'half3'
    def __init__(self, half3):
        pass

    def toCode(self):
        return 'half3'


class buildin_type_namep112(buildin_type_name):
    # buildin_type_name --> 'half4'
    def __init__(self, half4):
        pass

    def toCode(self):
        return 'half4'


class buildin_type_namep113(buildin_type_name):
    # buildin_type_name --> 'fixed2'
    def __init__(self, fixed2):
        pass

    def toCode(self):
        return 'fixed2'


class buildin_type_namep114(buildin_type_name):
    # buildin_type_name --> 'fixed3'
    def __init__(self, fixed3):
        pass

    def toCode(self):
        return 'fixed3'


class buildin_type_namep115(buildin_type_name):
    # buildin_type_name --> 'fixed4'
    def __init__(self, fixed4):
        pass

    def toCode(self):
        return 'fixed4'


class buildin_type_namep116(buildin_type_name):
    # buildin_type_name --> 'float3x3'
    def __init__(self, float3x3):
        pass

    def toCode(self):
        return 'float3x3'


class type_qualifierp117(type_qualifier):
    # type_qualifier --> 'uniform'
    def __init__(self, uniform):
        pass

    def toCode(self):
        return 'uniform'


class type_qualifierp118(type_qualifier):
    # type_qualifier --> 'inline'
    def __init__(self, inline):
        pass

    def toCode(self):
        return 'inline'


class type_qualifierp119(type_qualifier):
    # type_qualifier --> 'const'
    def __init__(self, const):
        pass

    def toCode(self):
        return 'const'


class storage_class_specifierp120(storage_class_specifier):
    # storage_class_specifier --> 'static'
    def __init__(self, static):
        pass

    def toCode(self):
        return 'static'


class typedef_namep121(typedef_name):
    # typedef_name --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class struct_specifierp122(struct_specifier):
    # struct_specifier --> 'struct' ID
    def __init__(self, struct, ID):
        self.ID = ID

    def toCode(self):
        return 'struct ' + self.ID.toCode()


class struct_specifierp123(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list

    def toCode(self):
        return 'struct ' + self.ID.toCode() + '\n' + IAA() + '{' + '\n' + self.struct_dec_list.toCode() + SSI() + '}'


class struct_dec_listp124(struct_dec_list):
    # struct_dec_list --> struct_dec
    def __init__(self, struct_dec):
        self.struct_dec = struct_dec

    def toCode(self):
        return self.struct_dec.toCode()


class struct_dec_listp125(struct_dec_list):
    # struct_dec_list --> struct_dec_list struct_dec
    def __init__(self, struct_dec_list, struct_dec):
        self.struct_dec_list = struct_dec_list
        self.struct_dec = struct_dec

    def toCode(self):
        return self.struct_dec_list.toCode() + self.struct_dec.toCode()


class struct_decp126(struct_dec):
    # struct_dec --> type_specifier struct_declarator_list ;
    def __init__(self, type_specifier, struct_declarator_list, Semicolon):
        self.type_specifier = type_specifier
        self.struct_declarator_list = struct_declarator_list

    def toCode(self):
        return I() + self.type_specifier.toCode() + ' ' + self.struct_declarator_list.toCode() + ';\n'


class struct_decp127(struct_dec):
    # struct_dec --> ID ;
    def __init__(self, ID, Semicolon):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode() + ';'


class struct_decp128(struct_dec):
    # struct_dec --> ID ( Number )
    def __init__(self, ID, LParen, Number, RParen):
        self.ID = ID
        self.Number = Number

    def toCode(self):
        return self.ID.toCode() + '(' + self.Number.toCode() + ')'


class struct_decp129(struct_dec):
    # struct_dec --> ID ( Number , Number )
    def __init__(self, ID, LParen, Number1, Comma, Number2, RParen):
        self.ID = ID
        self.Number1 = Number1
        self.Number2 = Number2

    def toCode(self):
        return self.ID.toCode() + '(' + self.Number1.toCode() + ',' + self.Number2.toCode() + ')'


class struct_decp130(struct_dec):
    # struct_dec --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class struct_decp131(struct_dec):
    # struct_dec --> 'INTERNAL_DATA'
    def __init__(self, INTERNAL_DATA):
        pass

    def toCode(self):
        return 'INTERNAL_DATA'


class struct_decp132(struct_dec):
    # struct_dec --> 'UNITY_VERTEX_INPUT_INSTANCE_ID'
    def __init__(self, UNITY_VERTEX_INPUT_INSTANCE_ID):
        pass

    def toCode(self):
        return 'UNITY_VERTEX_INPUT_INSTANCE_ID'


class struct_decp133(struct_dec):
    # struct_dec --> 'UNITY_VERTEX_OUTPUT_STEREO'
    def __init__(self, UNITY_VERTEX_OUTPUT_STEREO):
        pass

    def toCode(self):
        return 'UNITY_VERTEX_OUTPUT_STEREO'


class struct_declarator_listp134(struct_declarator_list):
    # struct_declarator_list --> struct_declarator
    def __init__(self, struct_declarator):
        self.struct_declarator = struct_declarator

    def toCode(self):
        return self.struct_declarator.toCode()


class struct_declarator_listp135(struct_declarator_list):
    # struct_declarator_list --> struct_declarator_list , struct_declarator
    def __init__(self, struct_declarator_list, Comma, struct_declarator):
        self.struct_declarator_list = struct_declarator_list
        self.struct_declarator = struct_declarator

    def toCode(self):
        return self.struct_declarator_list.toCode() + ',' + self.struct_declarator.toCode()


class struct_declaratorp136(struct_declarator):
    # struct_declarator --> declarator
    def __init__(self, declarator):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode()


class struct_declaratorp137(struct_declarator):
    # struct_declarator --> declarator : ID
    def __init__(self, declarator, Colon, ID):
        self.declarator = declarator
        self.ID = ID

    def toCode(self):
        return self.declarator.toCode() + ' : ' + self.ID.toCode()


class declaratorp138(declarator):
    # declarator --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class declaratorp139(declarator):
    # declarator --> declarator [ exp ]
    def __init__(self, declarator, LBrack, exp, RBrack):
        self.declarator = declarator
        self.exp = exp

    def toCode(self):
        return self.declarator.toCode() + '[' + self.exp.toCode() + ']'


class declaratorp140(declarator):
    # declarator --> declarator ( )
    def __init__(self, declarator, LParen, RParen):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode() + '(' + ')'


class declaratorp141(declarator):
    # declarator --> declarator ( parameter_list )
    def __init__(self, declarator, LParen, parameter_list, RParen):
        self.declarator = declarator
        self.parameter_list = parameter_list

    def toCode(self):
        return self.declarator.toCode() + '(' + self.parameter_list.toCode() + ')'


class parameter_listp142(parameter_list):
    # parameter_list --> parameter_dec
    def __init__(self, parameter_dec):
        self.parameter_dec = parameter_dec

    def toCode(self):
        return self.parameter_dec.toCode()


class parameter_listp143(parameter_list):
    # parameter_list --> parameter_list , parameter_dec
    def __init__(self, parameter_list, Comma, parameter_dec):
        self.parameter_list = parameter_list
        self.parameter_dec = parameter_dec

    def toCode(self):
        return self.parameter_list.toCode() + ', ' + self.parameter_dec.toCode()


class parameter_decp144(parameter_dec):
    # parameter_dec --> parameter_dec_specifier declarator
    def __init__(self, parameter_dec_specifier, declarator):
        self.parameter_dec_specifier = parameter_dec_specifier
        self.declarator = declarator

    def toCode(self):
        return self.parameter_dec_specifier.toCode() + self.declarator.toCode()


class parameter_decp145(parameter_dec):
    # parameter_dec --> parameter_dec_specifier declarator : ID
    def __init__(self, parameter_dec_specifier, declarator, Colon, ID):
        self.parameter_dec_specifier = parameter_dec_specifier
        self.declarator = declarator
        self.ID = ID

    def toCode(self):
        return self.parameter_dec_specifier.toCode() + self.declarator.toCode() + ':' + self.ID.toCode()


class parameter_dec_specifierp146(parameter_dec_specifier):
    # parameter_dec_specifier --> dec_specifier
    def __init__(self, dec_specifier):
        self.dec_specifier = dec_specifier

    def toCode(self):
        return self.dec_specifier.toCode()


class parameter_dec_specifierp147(parameter_dec_specifier):
    # parameter_dec_specifier --> 'out' dec_specifier
    def __init__(self, out, dec_specifier):
        self.dec_specifier = dec_specifier

    def toCode(self):
        return 'out' + self.dec_specifier.toCode()


class parameter_dec_specifierp148(parameter_dec_specifier):
    # parameter_dec_specifier --> 'inout' dec_specifier
    def __init__(self, inout, dec_specifier):
        self.dec_specifier = dec_specifier

    def toCode(self):
        return 'inout' + self.dec_specifier.toCode()


class parameter_dec_specifierp149(parameter_dec_specifier):
    # parameter_dec_specifier --> 'triangle' dec_specifier
    def __init__(self, triangle, dec_specifier):
        self.dec_specifier = dec_specifier

    def toCode(self):
        return 'triangle' + self.dec_specifier.toCode()


class parameter_dec_specifierp150(parameter_dec_specifier):
    # parameter_dec_specifier --> 'inout' 'TriangleStream' < ID >
    def __init__(self, inout, TriangleStream, LT, ID, GT):
        self.ID = ID

    def toCode(self):
        return 'inout' + 'TriangleStream' + '<' + self.ID.toCode() + '>'


class init_dec_listp151(init_dec_list):
    # init_dec_list --> init_dec
    def __init__(self, init_dec):
        self.init_dec = init_dec

    def toCode(self):
        return self.init_dec.toCode()


class init_dec_listp152(init_dec_list):
    # init_dec_list --> init_dec_list , init_dec
    def __init__(self, init_dec_list, Comma, init_dec):
        self.init_dec_list = init_dec_list
        self.init_dec = init_dec

    def toCode(self):
        return self.init_dec_list.toCode() + ',' + self.init_dec.toCode()


class init_decp153(init_dec):
    # init_dec --> declarator
    def __init__(self, declarator):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode()


class init_decp154(init_dec):
    # init_dec --> declarator = initializer
    def __init__(self, declarator, Assign, initializer):
        self.declarator = declarator
        self.initializer = initializer

    def toCode(self):
        return self.declarator.toCode() + '=' + self.initializer.toCode()


class initializerp155(initializer):
    # initializer --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class initializerp156(initializer):
    # initializer --> { initializer_list }
    def __init__(self, LBrace, initializer_list, RBrace):
        self.initializer_list = initializer_list

    def toCode(self):
        return '{' + self.initializer_list.toCode() + '}'


class initializerp157(initializer):
    # initializer --> { initializer_list , }
    def __init__(self, LBrace, initializer_list, Comma, RBrace):
        self.initializer_list = initializer_list

    def toCode(self):
        return '{' + self.initializer_list.toCode() + ',' + '}'


class initializer_listp158(initializer_list):
    # initializer_list --> initializer
    def __init__(self, initializer):
        self.initializer = initializer

    def toCode(self):
        return self.initializer.toCode()


class initializer_listp159(initializer_list):
    # initializer_list --> initializer_list , initializer
    def __init__(self, initializer_list, Comma, initializer):
        self.initializer_list = initializer_list
        self.initializer = initializer

    def toCode(self):
        return self.initializer_list.toCode() + ',' + self.initializer.toCode()


class stmp160(stm):
    # stm --> exp_stm
    def __init__(self, exp_stm):
        self.exp_stm = exp_stm

    def toCode(self):
        return self.exp_stm.toCode()


class stmp161(stm):
    # stm --> compound_stm
    def __init__(self, compound_stm):
        self.compound_stm = compound_stm

    def toCode(self):
        return self.compound_stm.toCode()


class stmp162(stm):
    # stm --> selection_stm
    def __init__(self, selection_stm):
        self.selection_stm = selection_stm

    def toCode(self):
        return self.selection_stm.toCode()


class stmp163(stm):
    # stm --> iteration_stm
    def __init__(self, iteration_stm):
        self.iteration_stm = iteration_stm

    def toCode(self):
        return self.iteration_stm.toCode()


class stmp164(stm):
    # stm --> jump_stm
    def __init__(self, jump_stm):
        self.jump_stm = jump_stm

    def toCode(self):
        return self.jump_stm.toCode()


class stmp165(stm):
    # stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class stmp166(stm):
    # stm --> 'UNITY_BRANCH'
    def __init__(self, UNITY_BRANCH):
        pass

    def toCode(self):
        return 'UNITY_BRANCH'


class stmp167(stm):
    # stm --> 'UNITY_UNROLL'
    def __init__(self, UNITY_UNROLL):
        pass

    def toCode(self):
        return 'UNITY_UNROLL'


class stmp168(stm):
    # stm --> 'TRANSFER_SHADOW_CASTER_NORMALOFFSET' ( ID )
    def __init__(self, TRANSFER_SHADOW_CASTER_NORMALOFFSET, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return 'TRANSFER_SHADOW_CASTER_NORMALOFFSET' + '(' + self.ID.toCode() + ')'


class stmp169(stm):
    # stm --> 'SHADOW_CASTER_FRAGMENT' ( ID )
    def __init__(self, SHADOW_CASTER_FRAGMENT, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return 'SHADOW_CASTER_FRAGMENT' + '(' + self.ID.toCode() + ')'


class stmp170(stm):
    # stm --> 'SPEEDTREE_COPY_FRAG' ( ID , ID )
    def __init__(self, SPEEDTREE_COPY_FRAG, LParen, ID1, Comma, ID2, RParen):
        self.ID1 = ID1
        self.ID2 = ID2

    def toCode(self):
        return 'SPEEDTREE_COPY_FRAG' + '(' + self.ID1.toCode() + ',' + self.ID2.toCode() + ')'


class stmp171(stm):
    # stm --> 'UNITY_TRANSFER_DITHER_CROSSFADE_HPOS' ( argument_exp_list )
    def __init__(self, UNITY_TRANSFER_DITHER_CROSSFADE_HPOS, LParen, argument_exp_list, RParen):
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return 'UNITY_TRANSFER_DITHER_CROSSFADE_HPOS' + '(' + self.argument_exp_list.toCode() + ')'


class stmp172(stm):
    # stm --> 'UNITY_APPLY_DITHER_CROSSFADE' ( ID )
    def __init__(self, UNITY_APPLY_DITHER_CROSSFADE, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return 'UNITY_APPLY_DITHER_CROSSFADE' + '(' + self.ID.toCode() + ')'


class exp_stmp173(exp_stm):
    # exp_stm --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return I() + self.exp.toCode() + ';\n'


class exp_stmp174(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass

    def toCode(self):
        return I() + ';\n'


class compound_stmp175(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list

    def toCode(self):
        return IAA() + '{' + '\n'+ self.block_item_list.toCode() + SSI() + '}' + '\n'


class compound_stmp176(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass

    def toCode(self):
        return I() + '{\n' +I() + '}\n'


class block_item_listp177(block_item_list):
    # block_item_list --> block_item
    def __init__(self, block_item):
        self.block_item = block_item

    def toCode(self):
        return self.block_item.toCode()


class block_item_listp178(block_item_list):
    # block_item_list --> block_item_list block_item
    def __init__(self, block_item_list, block_item):
        self.block_item_list = block_item_list
        self.block_item = block_item

    def toCode(self):
        return self.block_item_list.toCode() + self.block_item.toCode()


class block_itemp179(block_item):
    # block_item --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class block_itemp180(block_item):
    # block_item --> stm
    def __init__(self, stm):
        self.stm = stm

    def toCode(self):
        return self.stm.toCode()


class selection_stmp181(selection_stm):
    # selection_stm --> 'if' ( exp ) stm
    def __init__(self, _if, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm

    def toCode(self):
        return I() + 'if ' + '(' + self.exp.toCode() + ')\n' + self.stm.toCode()


class selection_stmp182(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, _if, LParen, exp, RParen, stm1, _else, stm2):
        self.exp = exp
        self.stm1 = stm1
        self.stm2 = stm2

    def toCode(self):
        return I() + 'if ' + '(' + self.exp.toCode() + ')\n' + self.stm1.toCode() + I() + 'else' + self.stm2.toCode()


class iteration_stmp183(iteration_stm):
    # iteration_stm --> 'while' ( exp ) stm
    def __init__(self, _while, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm

    def toCode(self):
        return 'while' + '(' + self.exp.toCode() + ')' + self.stm.toCode()


class iteration_stmp184(iteration_stm):
    # iteration_stm --> 'do' stm 'while' ( exp ) ;
    def __init__(self, do, stm, _while, LParen, exp, RParen, Semicolon):
        self.stm = stm
        self.exp = exp

    def toCode(self):
        return 'do' + self.stm.toCode() + 'while' + '(' + self.exp.toCode() + ')' + ';'


class iteration_stmp185(iteration_stm):
    # iteration_stm --> 'for' ( exp ; exp ; exp ) stm
    def __init__(self, _for, LParen, exp1, Semicolon1, exp2, Semicolon2, exp3, RParen, stm):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.stm = stm

    def toCode(self):
        return 'for' + '(' + self.exp.toCode() + ';' + self.exp.toCode() + ';' + self.exp.toCode() + ')' + self.stm.toCode()


class iteration_stmp186(iteration_stm):
    # iteration_stm --> 'for' ( dec_specifier init_dec_list ; exp ; exp ) stm
    def __init__(self, _for, LParen, dec_specifier, init_dec_list, Semicolon1, exp1, Semicolon2, exp2, RParen, stm):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list
        self.exp1 = exp1
        self.exp2 = exp2
        self.stm = stm

    def toCode(self):
        return 'for' + '(' + self.dec_specifier.toCode() + self.init_dec_list.toCode() + ';' + self.exp1.toCode() + ';' + self.exp2.toCode() + ')' + self.stm.toCode()


class jump_stmp187(jump_stm):
    # jump_stm --> 'goto' ID
    def __init__(self, goto, ID):
        self.ID = ID

    def toCode(self):
        return I() + 'goto' + self.ID.toCode() + '\n'


class jump_stmp188(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, _continue):
        pass

    def toCode(self):
        return I() + 'continue' + '\n'


class jump_stmp189(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, _break):
        pass

    def toCode(self):
        return I() + 'break' + '\n'


class jump_stmp190(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, _return, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return I() + 'return ' + self.exp.toCode() + ';\n'


class Test(unittest.TestCase):


    def test(self):
        pass