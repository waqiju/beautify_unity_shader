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
        return GB() + I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + '\n' + self.compound_stm.toCode() + GA()


class function_definitionp131(function_definition):
    # function_definition --> dec_specifier declarator : ID compound_stm
    def __init__(self, dec_specifier, declarator, Colon, ID, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID = ID
        self.compound_stm = compound_stm

    def toCode(self):
        return GB() + I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + ' : ' + self.ID.toCode() + '\n' + self.compound_stm.toCode() + GA()


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
        return self.argument_exp_list.toCode() + ', ' + self.assignment_exp.toCode()


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
        return self.binary_exp.toCode() + ' ' + self.binary_op.toCode() + ' ' + self.unary_exp.toCode()


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
        return self.unary_exp.toCode() + ' ' + self.assignment_op.toCode() + ' ' + self.assignment_exp.toCode()


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
        return GB() + I() + self.struct_specifier.toCode() + ';\n' + GA()


class decp211(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list

    def toCode(self):
        return I() + self.dec_specifier.toCode() + ' ' + self.init_dec_list.toCode() + ';\n'


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
        return 'struct ' + self.ID.toCode()


class struct_specifierp243(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list

    def toCode(self):
        return 'struct ' + self.ID.toCode() + '\n' + IAA() + '{' + '\n' + self.struct_dec_list.toCode() + SSI() + '}'


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
        return I() + self.type_specifier.toCode() + ' ' + self.struct_declarator_list.toCode() + ';\n'


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
        return self.declarator.toCode() + ' : ' + self.ID.toCode()


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
        return self.parameter_list.toCode() + ', ' + self.parameter_dec.toCode()


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
        return I() + self.exp.toCode() + ';\n'


class exp_stmp294(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass

    def toCode(self):
        return I() + ';\n'


class compound_stmp295(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list

    def toCode(self):
        return IAA() + '{' + '\n'+ self.block_item_list.toCode() + SSI() + '}' + '\n'


class compound_stmp296(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass

    def toCode(self):
        return I() + '{\n' +I() + '}\n'


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
        return I() + 'if ' + '(' + self.exp.toCode() + ')\n' + self.stm.toCode()


class selection_stmp302(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, _if, LParen, exp, RParen, stm1, _else, stm2):
        self.exp = exp
        self.stm1 = stm1
        self.stm2 = stm2

    def toCode(self):
        return I() + 'if ' + '(' + self.exp.toCode() + ')\n' + self.stm1.toCode() + I() + 'else' + self.stm2.toCode()


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
        return 'for' + '(' + self.exp.toCode() + ';' + self.exp.toCode() + ';' + self.exp.toCode() + ')' + self.stm.toCode()


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
        return I() + 'goto' + self.ID.toCode() + '\n'


class jump_stmp308(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, _continue):
        pass

    def toCode(self):
        return I() + 'continue' + '\n'


class jump_stmp309(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, _break):
        pass

    def toCode(self):
        return I() + 'break' + '\n'


class jump_stmp310(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, _return, exp, Semicolon):
        self.exp = exp

    def toCode(self):
        return I() + 'return ' + self.exp.toCode() + ';\n'


class Test(unittest.TestCase):


    def test(self):
        pass