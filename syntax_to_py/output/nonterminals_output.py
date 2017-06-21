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
    pragma_item_list = 'pragma_item_list'
    pragma_item = 'pragma_item'
    dec_list = 'dec_list'
    id_list = 'id_list'
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


class marco_unfold(Nonterminal):
    pass


class pragma_item_list(Nonterminal):
    pass


class pragma_item(Nonterminal):
    pass


class dec_list(Nonterminal):
    pass


class id_list(Nonterminal):
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
        return 'CGPROGRAM' + self.cg_prog.toCode() + 'ENDCG'


class progp2(prog):
    # prog --> 'CGINCLUDE' cg_prog 'ENDCG'
    def __init__(self, CGINCLUDE, cg_prog, ENDCG):
        self.cg_prog = cg_prog

    def toCode(self):
        return 'CGINCLUDE' + self.cg_prog.toCode() + 'ENDCG'


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
        return self.dec_specifier.toCode() + self.declarator.toCode() + self.compound_stm.toCode()


class function_definitionp11(function_definition):
    # function_definition --> dec_specifier declarator : ID compound_stm
    def __init__(self, dec_specifier, declarator, Colon, ID, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID = ID
        self.compound_stm = compound_stm

    def toCode(self):
        return self.dec_specifier.toCode() + self.declarator.toCode() + ':' + self.ID.toCode() + self.compound_stm.toCode()


class preprocessing_stmp12(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class preprocessing_stmp13(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd

    def toCode(self):
        return self.pp_cmd.toCode()


class preprocessing_stmp14(preprocessing_stm):
    # preprocessing_stm --> marco_unfold
    def __init__(self, marco_unfold):
        self.marco_unfold = marco_unfold

    def toCode(self):
        return self.marco_unfold.toCode()


class pp_if_stmp15(pp_if_stm):
    # pp_if_stm --> # 'if' binary_exp Enter
    def __init__(self, Pound, if, binary_exp, Enter):
        self.binary_exp = binary_exp
        self.Enter = Enter

    def toCode(self):
        return '#' + 'if' + self.binary_exp.toCode() + self.Enter.toCode()


class pp_if_stmp16(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'ifdef' + self.ID.toCode()


class pp_if_stmp17(pp_if_stm):
    # pp_if_stm --> # 'ifndef' ID
    def __init__(self, Pound, ifndef, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'ifndef' + self.ID.toCode()


class pp_if_stmp18(pp_if_stm):
    # pp_if_stm --> # 'elif' ID
    def __init__(self, Pound, elif, ID):
        self.ID = ID

    def toCode(self):
        return '#' + 'elif' + self.ID.toCode()


class pp_if_stmp19(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, else):
        pass

    def toCode(self):
        return '#' + 'else'


class pp_if_stmp20(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass

    def toCode(self):
        return '#' + 'endif'


class pp_cmdp21(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String

    def toCode(self):
        return '#' + 'include' + self.String.toCode()


class pp_cmdp22(pp_cmd):
    # pp_cmd --> # 'pragma' pragma_item_list Enter
    def __init__(self, Pound, pragma, pragma_item_list, Enter):
        self.pragma_item_list = pragma_item_list
        self.Enter = Enter

    def toCode(self):
        return '#' + 'pragma' + self.pragma_item_list.toCode() + self.Enter.toCode()


class pp_cmdp23(pp_cmd):
    # pp_cmd --> # 'define' exp exp Enter
    def __init__(self, Pound, define, exp1, exp2, Enter):
        self.exp1 = exp1
        self.exp2 = exp2
        self.Enter = Enter

    def toCode(self):
        return '#' + 'define' + self.exp1.toCode() + self.exp2.toCode() + self.Enter.toCode()


class marco_unfoldp24(marco_unfold):
    # marco_unfold --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return self.exp.toCode() + ';'


class pragma_item_listp25(pragma_item_list):
    # pragma_item_list --> pragma_item
    def __init__(self, pragma_item):
        self.pragma_item = pragma_item

    def toCode(self):
        return self.pragma_item.toCode()


class pragma_item_listp26(pragma_item_list):
    # pragma_item_list --> pragma_item_list pragma_item
    def __init__(self, pragma_item_list, pragma_item):
        self.pragma_item_list = pragma_item_list
        self.pragma_item = pragma_item

    def toCode(self):
        return self.pragma_item_list.toCode() + self.pragma_item.toCode()


class pragma_itemp27(pragma_item):
    # pragma_item --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class pragma_itemp28(pragma_item):
    # pragma_item --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class pragma_itemp29(pragma_item):
    # pragma_item --> ID : ID
    def __init__(self, ID1, Colon, ID2):
        self.ID1 = ID1
        self.ID2 = ID2

    def toCode(self):
        return self.ID1.toCode() + ':' + self.ID2.toCode()


class dec_listp30(dec_list):
    # dec_list --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class dec_listp31(dec_list):
    # dec_list --> dec_list dec
    def __init__(self, dec_list, dec):
        self.dec_list = dec_list
        self.dec = dec

    def toCode(self):
        return self.dec_list.toCode() + self.dec.toCode()


class id_listp32(id_list):
    # id_list --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class id_listp33(id_list):
    # id_list --> id_list ID
    def __init__(self, id_list, ID):
        self.id_list = id_list
        self.ID = ID

    def toCode(self):
        return self.id_list.toCode() + self.ID.toCode()


class primary_expp34(primary_exp):
    # primary_exp --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class primary_expp35(primary_exp):
    # primary_exp --> String
    def __init__(self, String):
        self.String = String

    def toCode(self):
        return self.String.toCode()


class primary_expp36(primary_exp):
    # primary_exp --> Number
    def __init__(self, Number):
        self.Number = Number

    def toCode(self):
        return self.Number.toCode()


class primary_expp37(primary_exp):
    # primary_exp --> ( exp )
    def __init__(self, LParen, exp, RParen):
        self.exp = exp

    def toCode(self):
        return '(' + self.exp.toCode() + ')'


class postfix_expp38(postfix_exp):
    # postfix_exp --> primary_exp
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def toCode(self):
        return self.primary_exp.toCode()


class postfix_expp39(postfix_exp):
    # postfix_exp --> postfix_exp [ exp ]
    def __init__(self, postfix_exp, LBrack, exp, RBrack):
        self.postfix_exp = postfix_exp
        self.exp = exp

    def toCode(self):
        return self.postfix_exp.toCode() + '[' + self.exp.toCode() + ']'


class postfix_expp40(postfix_exp):
    # postfix_exp --> postfix_exp ( )
    def __init__(self, postfix_exp, LParen, RParen):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '(' + ')'


class postfix_expp41(postfix_exp):
    # postfix_exp --> postfix_exp ( argument_exp_list )
    def __init__(self, postfix_exp, LParen, argument_exp_list, RParen):
        self.postfix_exp = postfix_exp
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return self.postfix_exp.toCode() + '(' + self.argument_exp_list.toCode() + ')'


class postfix_expp42(postfix_exp):
    # postfix_exp --> buildin_type_name ( argument_exp_list )
    def __init__(self, buildin_type_name, LParen, argument_exp_list, RParen):
        self.buildin_type_name = buildin_type_name
        self.argument_exp_list = argument_exp_list

    def toCode(self):
        return self.buildin_type_name.toCode() + '(' + self.argument_exp_list.toCode() + ')'


class postfix_expp43(postfix_exp):
    # postfix_exp --> postfix_exp . ID
    def __init__(self, postfix_exp, Dot, ID):
        self.postfix_exp = postfix_exp
        self.ID = ID

    def toCode(self):
        return self.postfix_exp.toCode() + '.' + self.ID.toCode()


class postfix_expp44(postfix_exp):
    # postfix_exp --> postfix_exp ++
    def __init__(self, postfix_exp, Increment):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '++'


class postfix_expp45(postfix_exp):
    # postfix_exp --> postfix_exp --
    def __init__(self, postfix_exp, Decrement):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode() + '--'


class argument_exp_listp46(argument_exp_list):
    # argument_exp_list --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class argument_exp_listp47(argument_exp_list):
    # argument_exp_list --> argument_exp_list , assignment_exp
    def __init__(self, argument_exp_list, Comma, assignment_exp):
        self.argument_exp_list = argument_exp_list
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.argument_exp_list.toCode() + ',' + self.assignment_exp.toCode()


class unary_expp48(unary_exp):
    # unary_exp --> postfix_exp
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def toCode(self):
        return self.postfix_exp.toCode()


class unary_expp49(unary_exp):
    # unary_exp --> ++ unary_exp
    def __init__(self, Increment, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return '++' + self.unary_exp.toCode()


class unary_expp50(unary_exp):
    # unary_exp --> -- unary_exp
    def __init__(self, Decrement, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return '--' + self.unary_exp.toCode()


class unary_expp51(unary_exp):
    # unary_exp --> unary_op unary_exp
    def __init__(self, unary_op, unary_exp):
        self.unary_op = unary_op
        self.unary_exp = unary_exp

    def toCode(self):
        return self.unary_op.toCode() + self.unary_exp.toCode()


class unary_opp52(unary_op):
    # unary_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class unary_opp53(unary_op):
    # unary_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class unary_opp54(unary_op):
    # unary_op --> !
    def __init__(self, NOT):
        pass

    def toCode(self):
        return '!'


class unary_opp55(unary_op):
    # unary_op --> ~
    def __init__(self, Tilde):
        pass

    def toCode(self):
        return '~'


class cast_expp56(cast_exp):
    # cast_exp --> unary_exp
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def toCode(self):
        return self.unary_exp.toCode()


class cast_expp57(cast_exp):
    # cast_exp --> ( type_specifier ) cast_exp
    def __init__(self, LParen, type_specifier, RParen, cast_exp):
        self.type_specifier = type_specifier
        self.cast_exp = cast_exp

    def toCode(self):
        return '(' + self.type_specifier.toCode() + ')' + self.cast_exp.toCode()


class binary_expp58(binary_exp):
    # binary_exp --> cast_exp
    def __init__(self, cast_exp):
        self.cast_exp = cast_exp

    def toCode(self):
        return self.cast_exp.toCode()


class binary_expp59(binary_exp):
    # binary_exp --> binary_exp binary_op unary_exp
    def __init__(self, binary_exp, binary_op, unary_exp):
        self.binary_exp = binary_exp
        self.binary_op = binary_op
        self.unary_exp = unary_exp

    def toCode(self):
        return self.binary_exp.toCode() + self.binary_op.toCode() + self.unary_exp.toCode()


class binary_opp60(binary_op):
    # binary_op --> *
    def __init__(self, Times):
        pass

    def toCode(self):
        return '*'


class binary_opp61(binary_op):
    # binary_op --> /
    def __init__(self, Divide):
        pass

    def toCode(self):
        return '/'


class binary_opp62(binary_op):
    # binary_op --> %
    def __init__(self, Percent):
        pass

    def toCode(self):
        return '%'


class binary_opp63(binary_op):
    # binary_op --> +
    def __init__(self, Plus):
        pass

    def toCode(self):
        return '+'


class binary_opp64(binary_op):
    # binary_op --> -
    def __init__(self, Minus):
        pass

    def toCode(self):
        return '-'


class binary_opp65(binary_op):
    # binary_op --> <<
    def __init__(self, LeftShift):
        pass

    def toCode(self):
        return '<<'


class binary_opp66(binary_op):
    # binary_op --> >>
    def __init__(self, RightShift):
        pass

    def toCode(self):
        return '>>'


class binary_opp67(binary_op):
    # binary_op --> <
    def __init__(self, LT):
        pass

    def toCode(self):
        return '<'


class binary_opp68(binary_op):
    # binary_op --> >
    def __init__(self, GT):
        pass

    def toCode(self):
        return '>'


class binary_opp69(binary_op):
    # binary_op --> <=
    def __init__(self, LE):
        pass

    def toCode(self):
        return '<='


class binary_opp70(binary_op):
    # binary_op --> >=
    def __init__(self, GE):
        pass

    def toCode(self):
        return '>='


class binary_opp71(binary_op):
    # binary_op --> ==
    def __init__(self, EQ):
        pass

    def toCode(self):
        return '=='


class binary_opp72(binary_op):
    # binary_op --> !=
    def __init__(self, NEQ):
        pass

    def toCode(self):
        return '!='


class binary_opp73(binary_op):
    # binary_op --> &
    def __init__(self, Ampersand):
        pass

    def toCode(self):
        return '&'


class binary_opp74(binary_op):
    # binary_op --> ^
    def __init__(self, Caret):
        pass

    def toCode(self):
        return '^'


class binary_opp75(binary_op):
    # binary_op --> |
    def __init__(self, VerticalBar):
        pass

    def toCode(self):
        return '|'


class binary_opp76(binary_op):
    # binary_op --> &&
    def __init__(self, AND):
        pass

    def toCode(self):
        return '&&'


class binary_opp77(binary_op):
    # binary_op --> ||
    def __init__(self, OR):
        pass

    def toCode(self):
        return '||'


class conditional_expp78(conditional_exp):
    # conditional_exp --> binary_exp
    def __init__(self, binary_exp):
        self.binary_exp = binary_exp

    def toCode(self):
        return self.binary_exp.toCode()


class conditional_expp79(conditional_exp):
    # conditional_exp --> binary_exp ? exp : conditional_exp
    def __init__(self, binary_exp, Question, exp, Colon, conditional_exp):
        self.binary_exp = binary_exp
        self.exp = exp
        self.conditional_exp = conditional_exp

    def toCode(self):
        return self.binary_exp.toCode() + '?' + self.exp.toCode() + ':' + self.conditional_exp.toCode()


class assignment_expp80(assignment_exp):
    # assignment_exp --> conditional_exp
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp

    def toCode(self):
        return self.conditional_exp.toCode()


class assignment_expp81(assignment_exp):
    # assignment_exp --> unary_exp assignment_op assignment_exp
    def __init__(self, unary_exp, assignment_op, assignment_exp):
        self.unary_exp = unary_exp
        self.assignment_op = assignment_op
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.unary_exp.toCode() + self.assignment_op.toCode() + self.assignment_exp.toCode()


class assignment_opp82(assignment_op):
    # assignment_op --> =
    def __init__(self, Assign):
        pass

    def toCode(self):
        return '='


class assignment_opp83(assignment_op):
    # assignment_op --> *=
    def __init__(self, AddAssign):
        pass

    def toCode(self):
        return '*='


class assignment_opp84(assignment_op):
    # assignment_op --> /=
    def __init__(self, SubAssign):
        pass

    def toCode(self):
        return '/='


class assignment_opp85(assignment_op):
    # assignment_op --> %=
    def __init__(self, MulAssign):
        pass

    def toCode(self):
        return '%='


class assignment_opp86(assignment_op):
    # assignment_op --> +=
    def __init__(self, DivAssign):
        pass

    def toCode(self):
        return '+='


class assignment_opp87(assignment_op):
    # assignment_op --> -=
    def __init__(self, ModAssign):
        pass

    def toCode(self):
        return '-='


class assignment_opp88(assignment_op):
    # assignment_op --> <<=
    def __init__(self, LeftShiftAssign):
        pass

    def toCode(self):
        return '<<='


class assignment_opp89(assignment_op):
    # assignment_op --> >>=
    def __init__(self, RightShiftAssign):
        pass

    def toCode(self):
        return '>>='


class assignment_opp90(assignment_op):
    # assignment_op --> &=
    def __init__(self, AndAssign):
        pass

    def toCode(self):
        return '&='


class assignment_opp91(assignment_op):
    # assignment_op --> ^=
    def __init__(self, XorAssign):
        pass

    def toCode(self):
        return '^='


class assignment_opp92(assignment_op):
    # assignment_op --> |=
    def __init__(self, OrAssign):
        pass

    def toCode(self):
        return '|='


class expp93(exp):
    # exp --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.assignment_exp.toCode()


class expp94(exp):
    # exp --> exp , assignment_exp
    def __init__(self, exp, Comma, assignment_exp):
        self.exp = exp
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.exp.toCode() + ',' + self.assignment_exp.toCode()


class decp95(dec):
    # dec --> struct_specifier ;
    def __init__(self, struct_specifier, Semicolon):
        self.struct_specifier = struct_specifier

    def toCode(self):
        return self.struct_specifier.toCode() + ';'


class decp96(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list

    def toCode(self):
        return self.dec_specifier.toCode() + self.init_dec_list.toCode() + ';'


class dec_specifierp97(dec_specifier):
    # dec_specifier --> type_specifier
    def __init__(self, type_specifier):
        self.type_specifier = type_specifier

    def toCode(self):
        return self.type_specifier.toCode()


class dec_specifierp98(dec_specifier):
    # dec_specifier --> type_qualifier type_specifier
    def __init__(self, type_qualifier, type_specifier):
        self.type_qualifier = type_qualifier
        self.type_specifier = type_specifier

    def toCode(self):
        return self.type_qualifier.toCode() + self.type_specifier.toCode()


class type_specifierp99(type_specifier):
    # type_specifier --> buildin_type_name
    def __init__(self, buildin_type_name):
        self.buildin_type_name = buildin_type_name

    def toCode(self):
        return self.buildin_type_name.toCode()


class type_specifierp100(type_specifier):
    # type_specifier --> typedef_name
    def __init__(self, typedef_name):
        self.typedef_name = typedef_name

    def toCode(self):
        return self.typedef_name.toCode()


class buildin_type_namep101(buildin_type_name):
    # buildin_type_name --> 'void'
    def __init__(self, void):
        pass

    def toCode(self):
        return 'void'


class buildin_type_namep102(buildin_type_name):
    # buildin_type_name --> 'char'
    def __init__(self, char):
        pass

    def toCode(self):
        return 'char'


class buildin_type_namep103(buildin_type_name):
    # buildin_type_name --> 'short'
    def __init__(self, short):
        pass

    def toCode(self):
        return 'short'


class buildin_type_namep104(buildin_type_name):
    # buildin_type_name --> 'int'
    def __init__(self, int):
        pass

    def toCode(self):
        return 'int'


class buildin_type_namep105(buildin_type_name):
    # buildin_type_name --> 'long'
    def __init__(self, long):
        pass

    def toCode(self):
        return 'long'


class buildin_type_namep106(buildin_type_name):
    # buildin_type_name --> 'float'
    def __init__(self, float):
        pass

    def toCode(self):
        return 'float'


class buildin_type_namep107(buildin_type_name):
    # buildin_type_name --> 'double'
    def __init__(self, double):
        pass

    def toCode(self):
        return 'double'


class buildin_type_namep108(buildin_type_name):
    # buildin_type_name --> 'sampler2D'
    def __init__(self, sampler2D):
        pass

    def toCode(self):
        return 'sampler2D'


class buildin_type_namep109(buildin_type_name):
    # buildin_type_name --> 'float2'
    def __init__(self, float2):
        pass

    def toCode(self):
        return 'float2'


class buildin_type_namep110(buildin_type_name):
    # buildin_type_name --> 'float3'
    def __init__(self, float3):
        pass

    def toCode(self):
        return 'float3'


class buildin_type_namep111(buildin_type_name):
    # buildin_type_name --> 'float4'
    def __init__(self, float4):
        pass

    def toCode(self):
        return 'float4'


class buildin_type_namep112(buildin_type_name):
    # buildin_type_name --> 'half2'
    def __init__(self, half2):
        pass

    def toCode(self):
        return 'half2'


class buildin_type_namep113(buildin_type_name):
    # buildin_type_name --> 'half3'
    def __init__(self, half3):
        pass

    def toCode(self):
        return 'half3'


class buildin_type_namep114(buildin_type_name):
    # buildin_type_name --> 'half4'
    def __init__(self, half4):
        pass

    def toCode(self):
        return 'half4'


class buildin_type_namep115(buildin_type_name):
    # buildin_type_name --> 'fixed2'
    def __init__(self, fixed2):
        pass

    def toCode(self):
        return 'fixed2'


class buildin_type_namep116(buildin_type_name):
    # buildin_type_name --> 'fixed3'
    def __init__(self, fixed3):
        pass

    def toCode(self):
        return 'fixed3'


class buildin_type_namep117(buildin_type_name):
    # buildin_type_name --> 'fixed4'
    def __init__(self, fixed4):
        pass

    def toCode(self):
        return 'fixed4'


class buildin_type_namep118(buildin_type_name):
    # buildin_type_name --> 'float3x3'
    def __init__(self, float3x3):
        pass

    def toCode(self):
        return 'float3x3'


class type_qualifierp119(type_qualifier):
    # type_qualifier --> 'uniform'
    def __init__(self, uniform):
        pass

    def toCode(self):
        return 'uniform'


class type_qualifierp120(type_qualifier):
    # type_qualifier --> 'inout'
    def __init__(self, inout):
        pass

    def toCode(self):
        return 'inout'


class type_qualifierp121(type_qualifier):
    # type_qualifier --> 'inline'
    def __init__(self, inline):
        pass

    def toCode(self):
        return 'inline'


class type_qualifierp122(type_qualifier):
    # type_qualifier --> 'const'
    def __init__(self, const):
        pass

    def toCode(self):
        return 'const'


class typedef_namep123(typedef_name):
    # typedef_name --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class struct_specifierp124(struct_specifier):
    # struct_specifier --> 'struct' ID
    def __init__(self, struct, ID):
        self.ID = ID

    def toCode(self):
        return 'struct' + self.ID.toCode()


class struct_specifierp125(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list

    def toCode(self):
        return 'struct' + self.ID.toCode() + '{' + self.struct_dec_list.toCode() + '}'


class struct_dec_listp126(struct_dec_list):
    # struct_dec_list --> struct_dec
    def __init__(self, struct_dec):
        self.struct_dec = struct_dec

    def toCode(self):
        return self.struct_dec.toCode()


class struct_dec_listp127(struct_dec_list):
    # struct_dec_list --> struct_dec_list struct_dec
    def __init__(self, struct_dec_list, struct_dec):
        self.struct_dec_list = struct_dec_list
        self.struct_dec = struct_dec

    def toCode(self):
        return self.struct_dec_list.toCode() + self.struct_dec.toCode()


class struct_decp128(struct_dec):
    # struct_dec --> type_specifier struct_declarator_list ;
    def __init__(self, type_specifier, struct_declarator_list, Semicolon):
        self.type_specifier = type_specifier
        self.struct_declarator_list = struct_declarator_list

    def toCode(self):
        return self.type_specifier.toCode() + self.struct_declarator_list.toCode() + ';'


class struct_decp129(struct_dec):
    # struct_dec --> ID ;
    def __init__(self, ID, Semicolon):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode() + ';'


class struct_decp130(struct_dec):
    # struct_dec --> ID ( Number )
    def __init__(self, ID, LParen, Number, RParen):
        self.ID = ID
        self.Number = Number

    def toCode(self):
        return self.ID.toCode() + '(' + self.Number.toCode() + ')'


class struct_decp131(struct_dec):
    # struct_dec --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class struct_decp132(struct_dec):
    # struct_dec --> 'INTERNAL_DATA'
    def __init__(self, INTERNAL_DATA):
        pass

    def toCode(self):
        return 'INTERNAL_DATA'


class struct_declarator_listp133(struct_declarator_list):
    # struct_declarator_list --> struct_declarator
    def __init__(self, struct_declarator):
        self.struct_declarator = struct_declarator

    def toCode(self):
        return self.struct_declarator.toCode()


class struct_declarator_listp134(struct_declarator_list):
    # struct_declarator_list --> struct_declarator_list , struct_declarator
    def __init__(self, struct_declarator_list, Comma, struct_declarator):
        self.struct_declarator_list = struct_declarator_list
        self.struct_declarator = struct_declarator

    def toCode(self):
        return self.struct_declarator_list.toCode() + ',' + self.struct_declarator.toCode()


class struct_declaratorp135(struct_declarator):
    # struct_declarator --> declarator
    def __init__(self, declarator):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode()


class struct_declaratorp136(struct_declarator):
    # struct_declarator --> declarator : ID
    def __init__(self, declarator, Colon, ID):
        self.declarator = declarator
        self.ID = ID

    def toCode(self):
        return self.declarator.toCode() + ':' + self.ID.toCode()


class declaratorp137(declarator):
    # declarator --> ID
    def __init__(self, ID):
        self.ID = ID

    def toCode(self):
        return self.ID.toCode()


class declaratorp138(declarator):
    # declarator --> declarator [ exp ]
    def __init__(self, declarator, LBrack, exp, RBrack):
        self.declarator = declarator
        self.exp = exp

    def toCode(self):
        return self.declarator.toCode() + '[' + self.exp.toCode() + ']'


class declaratorp139(declarator):
    # declarator --> declarator ( )
    def __init__(self, declarator, LParen, RParen):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode() + '(' + ')'


class declaratorp140(declarator):
    # declarator --> declarator ( parameter_list )
    def __init__(self, declarator, LParen, parameter_list, RParen):
        self.declarator = declarator
        self.parameter_list = parameter_list

    def toCode(self):
        return self.declarator.toCode() + '(' + self.parameter_list.toCode() + ')'


class parameter_listp141(parameter_list):
    # parameter_list --> parameter_dec
    def __init__(self, parameter_dec):
        self.parameter_dec = parameter_dec

    def toCode(self):
        return self.parameter_dec.toCode()


class parameter_listp142(parameter_list):
    # parameter_list --> parameter_list , parameter_dec
    def __init__(self, parameter_list, Comma, parameter_dec):
        self.parameter_list = parameter_list
        self.parameter_dec = parameter_dec

    def toCode(self):
        return self.parameter_list.toCode() + ',' + self.parameter_dec.toCode()


class parameter_decp143(parameter_dec):
    # parameter_dec --> dec_specifier declarator
    def __init__(self, dec_specifier, declarator):
        self.dec_specifier = dec_specifier
        self.declarator = declarator

    def toCode(self):
        return self.dec_specifier.toCode() + self.declarator.toCode()


class parameter_decp144(parameter_dec):
    # parameter_dec --> dec_specifier declarator : ID
    def __init__(self, dec_specifier, declarator, Colon, ID):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID = ID

    def toCode(self):
        return self.dec_specifier.toCode() + self.declarator.toCode() + ':' + self.ID.toCode()


class init_dec_listp145(init_dec_list):
    # init_dec_list --> init_dec
    def __init__(self, init_dec):
        self.init_dec = init_dec

    def toCode(self):
        return self.init_dec.toCode()


class init_dec_listp146(init_dec_list):
    # init_dec_list --> init_dec_list , init_dec
    def __init__(self, init_dec_list, Comma, init_dec):
        self.init_dec_list = init_dec_list
        self.init_dec = init_dec

    def toCode(self):
        return self.init_dec_list.toCode() + ',' + self.init_dec.toCode()


class init_decp147(init_dec):
    # init_dec --> declarator
    def __init__(self, declarator):
        self.declarator = declarator

    def toCode(self):
        return self.declarator.toCode()


class init_decp148(init_dec):
    # init_dec --> declarator = assignment_exp
    def __init__(self, declarator, Assign, assignment_exp):
        self.declarator = declarator
        self.assignment_exp = assignment_exp

    def toCode(self):
        return self.declarator.toCode() + '=' + self.assignment_exp.toCode()


class stmp149(stm):
    # stm --> exp_stm
    def __init__(self, exp_stm):
        self.exp_stm = exp_stm

    def toCode(self):
        return self.exp_stm.toCode()


class stmp150(stm):
    # stm --> compound_stm
    def __init__(self, compound_stm):
        self.compound_stm = compound_stm

    def toCode(self):
        return self.compound_stm.toCode()


class stmp151(stm):
    # stm --> selection_stm
    def __init__(self, selection_stm):
        self.selection_stm = selection_stm

    def toCode(self):
        return self.selection_stm.toCode()


class stmp152(stm):
    # stm --> iteration_stm
    def __init__(self, iteration_stm):
        self.iteration_stm = iteration_stm

    def toCode(self):
        return self.iteration_stm.toCode()


class stmp153(stm):
    # stm --> jump_stm
    def __init__(self, jump_stm):
        self.jump_stm = jump_stm

    def toCode(self):
        return self.jump_stm.toCode()


class stmp154(stm):
    # stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm

    def toCode(self):
        return self.pp_if_stm.toCode()


class stmp155(stm):
    # stm --> 'UNITY_BRANCH'
    def __init__(self, UNITY_BRANCH):
        pass

    def toCode(self):
        return 'UNITY_BRANCH'


class stmp156(stm):
    # stm --> 'UNITY_UNROLL'
    def __init__(self, UNITY_UNROLL):
        pass

    def toCode(self):
        return 'UNITY_UNROLL'


class stmp157(stm):
    # stm --> 'TRANSFER_SHADOW_CASTER_NORMALOFFSET' ( ID )
    def __init__(self, TRANSFER_SHADOW_CASTER_NORMALOFFSET, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return 'TRANSFER_SHADOW_CASTER_NORMALOFFSET' + '(' + self.ID.toCode() + ')'


class stmp158(stm):
    # stm --> 'SHADOW_CASTER_FRAGMENT' ( ID )
    def __init__(self, SHADOW_CASTER_FRAGMENT, LParen, ID, RParen):
        self.ID = ID

    def toCode(self):
        return 'SHADOW_CASTER_FRAGMENT' + '(' + self.ID.toCode() + ')'


class exp_stmp159(exp_stm):
    # exp_stm --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return self.exp.toCode() + ';'


class exp_stmp160(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass

    def toCode(self):
        return ';'


class compound_stmp161(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list

    def toCode(self):
        return '{' + self.block_item_list.toCode() + '}'


class compound_stmp162(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass

    def toCode(self):
        return '{' + '}'


class block_item_listp163(block_item_list):
    # block_item_list --> block_item
    def __init__(self, block_item):
        self.block_item = block_item

    def toCode(self):
        return self.block_item.toCode()


class block_item_listp164(block_item_list):
    # block_item_list --> block_item_list block_item
    def __init__(self, block_item_list, block_item):
        self.block_item_list = block_item_list
        self.block_item = block_item

    def toCode(self):
        return self.block_item_list.toCode() + self.block_item.toCode()


class block_itemp165(block_item):
    # block_item --> dec
    def __init__(self, dec):
        self.dec = dec

    def toCode(self):
        return self.dec.toCode()


class block_itemp166(block_item):
    # block_item --> stm
    def __init__(self, stm):
        self.stm = stm

    def toCode(self):
        return self.stm.toCode()


class selection_stmp167(selection_stm):
    # selection_stm --> 'if' ( exp ) stm
    def __init__(self, if, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm

    def toCode(self):
        return 'if' + '(' + self.exp.toCode() + ')' + self.stm.toCode()


class selection_stmp168(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, if, LParen, exp, RParen, stm1, else, stm2):
        self.exp = exp
        self.stm1 = stm1
        self.stm2 = stm2

    def toCode(self):
        return 'if' + '(' + self.exp.toCode() + ')' + self.stm1.toCode() + 'else' + self.stm2.toCode()


class iteration_stmp169(iteration_stm):
    # iteration_stm --> 'while' ( exp ) stm
    def __init__(self, while, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm

    def toCode(self):
        return 'while' + '(' + self.exp.toCode() + ')' + self.stm.toCode()


class iteration_stmp170(iteration_stm):
    # iteration_stm --> 'do' stm 'while' ( exp ) ;
    def __init__(self, do, stm, while, LParen, exp, RParen, Semicolon):
        self.stm = stm
        self.exp = exp

    def toCode(self):
        return 'do' + self.stm.toCode() + 'while' + '(' + self.exp.toCode() + ')' + ';'


class iteration_stmp171(iteration_stm):
    # iteration_stm --> 'for' ( exp ; exp ; exp ) stm
    def __init__(self, for, LParen, exp1, Semicolon1, exp2, Semicolon2, exp3, RParen, stm):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.stm = stm

    def toCode(self):
        return 'for' + '(' + self.exp1.toCode() + ';' + self.exp2.toCode() + ';' + self.exp3.toCode() + ')' + self.stm.toCode()


class iteration_stmp172(iteration_stm):
    # iteration_stm --> 'for' ( dec_specifier init_dec_list ; exp ; exp ) stm
    def __init__(self, for, LParen, dec_specifier, init_dec_list, Semicolon1, exp1, Semicolon2, exp2, RParen, stm):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list
        self.exp1 = exp1
        self.exp2 = exp2
        self.stm = stm

    def toCode(self):
        return 'for' + '(' + self.dec_specifier.toCode() + self.init_dec_list.toCode() + ';' + self.exp1.toCode() + ';' + self.exp2.toCode() + ')' + self.stm.toCode()


class jump_stmp173(jump_stm):
    # jump_stm --> 'goto' ID
    def __init__(self, goto, ID):
        self.ID = ID

    def toCode(self):
        return 'goto' + self.ID.toCode()


class jump_stmp174(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, continue):
        pass

    def toCode(self):
        return 'continue'


class jump_stmp175(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, break):
        pass

    def toCode(self):
        return 'break'


class jump_stmp176(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, return, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return 'return' + self.exp.toCode() + ';'


class Test(unittest.TestCase):


    def test(self):
        pass
