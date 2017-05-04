from app.symbol_type import SymbolType
from app.syntax_nonterminal import Nonterminal
from .lex_tokens import TokenType
import unittest


class NonterminalType(SymbolType):

    prog = 'prog'
    shader_body = 'shader_body'
    props = 'props'
    props_body = 'props_body'
    prop_stm = 'prop_stm'
    prop_init = 'prop_init'
    subshr = 'subshr'
    subshr_body = 'subshr_body'
    tags = 'tags'
    tags_body = 'tags_body'
    tag_smt = 'tag_smt'
    cmds = 'cmds'
    cmd_stm = 'cmd_stm'
    ids = 'ids'
    passes = 'passes'
    shr_pass = 'shr_pass'
    pass_body = 'pass_body'
    cg_prog = 'cg_prog'
    cg_stms = 'cg_stms'
    cg_stm = 'cg_stm'
    function_definition = 'function_definition'
    preprocessing_stm = 'preprocessing_stm'
    pp_if_stm = 'pp_if_stm'
    pp_cmd = 'pp_cmd'
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
    struct_specifier = 'struct_specifier'
    struct_dec_list = 'struct_dec_list'
    struct_dec = 'struct_dec'
    declarator_list = 'declarator_list'
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


class shader_body(Nonterminal):
    pass


class props(Nonterminal):
    pass


class props_body(Nonterminal):
    pass


class prop_stm(Nonterminal):
    pass


class prop_init(Nonterminal):
    pass


class subshr(Nonterminal):
    pass


class subshr_body(Nonterminal):
    pass


class tags(Nonterminal):
    pass


class tags_body(Nonterminal):
    pass


class tag_smt(Nonterminal):
    pass


class cmds(Nonterminal):
    pass


class cmd_stm(Nonterminal):
    pass


class ids(Nonterminal):
    pass


class passes(Nonterminal):
    pass


class shr_pass(Nonterminal):
    pass


class pass_body(Nonterminal):
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


class struct_specifier(Nonterminal):
    pass


class struct_dec_list(Nonterminal):
    pass


class struct_dec(Nonterminal):
    pass


class declarator_list(Nonterminal):
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
    # prog --> 'Shader' String { shader_body }
    def __init__(self, Shader, String, LBrace, shader_body, RBrace):
        self.String = String
        self.shader_body = shader_body


class shader_bodyp2(shader_body):
    # shader_body --> props subshr
    def __init__(self, props, subshr):
        self.props = props
        self.subshr = subshr


class propsp3(props):
    # props --> 'Properties' { props_body }
    def __init__(self, Properties, LBrace, props_body, RBrace):
        self.props_body = props_body


class propsp4(props):
    # props -->
    def __init__(self):
        pass


class props_bodyp5(props_body):
    # props_body --> prop_stm props_body
    def __init__(self, prop_stm, props_body):
        self.prop_stm = prop_stm
        self.props_body = props_body


class props_bodyp6(props_body):
    # props_body -->
    def __init__(self):
        pass


class prop_stmp7(prop_stm):
    # prop_stm --> ID ( String , ReservedWord ) = prop_init
    def __init__(self, ID, LParen, String, Comma, ReservedWord, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.ReservedWord = ReservedWord
        self.prop_init = prop_init


class prop_initp8(prop_init):
    # prop_init --> Number
    def __init__(self, Number):
        self.Number = Number


class prop_initp9(prop_init):
    # prop_init --> String { }
    def __init__(self, String, LBrace, RBrace):
        self.String = String


class prop_initp10(prop_init):
    # prop_init --> ( Number , Number , Number , Number )
    def __init__(self, LParen, Number, Comma, Number, Comma, Number, Comma, Number, RParen):
        self.Number = Number
        self.Number = Number
        self.Number = Number
        self.Number = Number


class subshrp11(subshr):
    # subshr --> 'SubShader' { subshr_body }
    def __init__(self, SubShader, LBrace, subshr_body, RBrace):
        self.subshr_body = subshr_body


class subshr_bodyp12(subshr_body):
    # subshr_body --> tags cmds passes
    def __init__(self, tags, cmds, passes):
        self.tags = tags
        self.cmds = cmds
        self.passes = passes


class tagsp13(tags):
    # tags --> 'Tags' { tags_body }
    def __init__(self, Tags, LBrace, tags_body, RBrace):
        self.tags_body = tags_body


class tags_bodyp14(tags_body):
    # tags_body --> tag_smt tags_body
    def __init__(self, tag_smt, tags_body):
        self.tag_smt = tag_smt
        self.tags_body = tags_body


class tags_bodyp15(tags_body):
    # tags_body -->
    def __init__(self):
        pass


class tag_smtp16(tag_smt):
    # tag_smt --> String = String
    def __init__(self, String, Assign, String):
        self.String = String
        self.String = String


class cmdsp17(cmds):
    # cmds --> cmd_stm cmds
    def __init__(self, cmd_stm, cmds):
        self.cmd_stm = cmd_stm
        self.cmds = cmds


class cmdsp18(cmds):
    # cmds -->
    def __init__(self):
        pass


class cmd_stmp19(cmd_stm):
    # cmd_stm --> ReservedWord ids
    def __init__(self, ReservedWord, ids):
        self.ReservedWord = ReservedWord
        self.ids = ids


class idsp20(ids):
    # ids --> ID ids
    def __init__(self, ID, ids):
        self.ID = ID
        self.ids = ids


class idsp21(ids):
    # ids -->
    def __init__(self):
        pass


class passesp22(passes):
    # passes --> shr_pass passes
    def __init__(self, shr_pass, passes):
        self.shr_pass = shr_pass
        self.passes = passes


class passesp23(passes):
    # passes -->
    def __init__(self):
        pass


class shr_passp24(shr_pass):
    # shr_pass --> 'Pass' { pass_body }
    def __init__(self, Pass, LBrace, pass_body, RBrace):
        self.pass_body = pass_body


class pass_bodyp25(pass_body):
    # pass_body --> 'CGPROGRAM' cg_prog 'ENDCG'
    def __init__(self, CGPROGRAM, cg_prog, ENDCG):
        self.cg_prog = cg_prog


class cg_progp26(cg_prog):
    # cg_prog --> cg_stms
    def __init__(self, cg_stms):
        self.cg_stms = cg_stms


class cg_stmsp27(cg_stms):
    # cg_stms --> cg_stm cg_stms
    def __init__(self, cg_stm, cg_stms):
        self.cg_stm = cg_stm
        self.cg_stms = cg_stms


class cg_stmsp28(cg_stms):
    # cg_stms -->
    def __init__(self):
        pass


class cg_stmp29(cg_stm):
    # cg_stm --> preprocessing_stm
    def __init__(self, preprocessing_stm):
        self.preprocessing_stm = preprocessing_stm


class cg_stmp30(cg_stm):
    # cg_stm --> function_definition
    def __init__(self, function_definition):
        self.function_definition = function_definition


class cg_stmp31(cg_stm):
    # cg_stm --> dec
    def __init__(self, dec):
        self.dec = dec


class function_definitionp32(function_definition):
    # function_definition --> dec_specifier declarator compound_stm
    def __init__(self, dec_specifier, declarator, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm


class preprocessing_stmp33(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class preprocessing_stmp34(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd


class pp_if_stmp35(pp_if_stm):
    # pp_if_stm --> # 'if' ID
    def __init__(self, Pound, if, ID):
        self.ID = ID


class pp_if_stmp36(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID


class pp_if_stmp37(pp_if_stm):
    # pp_if_stm --> # 'idndef' ID
    def __init__(self, Pound, idndef, ID):
        self.ID = ID


class pp_if_stmp38(pp_if_stm):
    # pp_if_stm --> # 'elif' ID
    def __init__(self, Pound, elif, ID):
        self.ID = ID


class pp_if_stmp39(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, else):
        pass


class pp_if_stmp40(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass


class pp_cmdp41(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String


class pp_cmdp42(pp_cmd):
    # pp_cmd --> # 'pragma' ids
    def __init__(self, Pound, pragma, ids):
        self.ids = ids


class primary_expp43(primary_exp):
    # primary_exp --> ID
    def __init__(self, ID):
        self.ID = ID


class primary_expp44(primary_exp):
    # primary_exp --> String
    def __init__(self, String):
        self.String = String


class primary_expp45(primary_exp):
    # primary_exp --> Number
    def __init__(self, Number):
        self.Number = Number


class primary_expp46(primary_exp):
    # primary_exp --> ( exp )
    def __init__(self, LParen, exp, RParen):
        self.exp = exp


class postfix_expp47(postfix_exp):
    # postfix_exp --> primary_exp
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp


class postfix_expp48(postfix_exp):
    # postfix_exp --> postfix_exp [ exp ]
    def __init__(self, postfix_exp, LBrack, exp, RBrack):
        self.postfix_exp = postfix_exp
        self.exp = exp


class postfix_expp49(postfix_exp):
    # postfix_exp --> postfix_exp ( argument_exp_list )
    def __init__(self, postfix_exp, LParen, argument_exp_list, RParen):
        self.postfix_exp = postfix_exp
        self.argument_exp_list = argument_exp_list


class postfix_expp50(postfix_exp):
    # postfix_exp --> postfix_exp . ID
    def __init__(self, postfix_exp, Dot, ID):
        self.postfix_exp = postfix_exp
        self.ID = ID


class postfix_expp51(postfix_exp):
    # postfix_exp --> postfix_exp + +
    def __init__(self, postfix_exp, Plus, Plus):
        self.postfix_exp = postfix_exp


class postfix_expp52(postfix_exp):
    # postfix_exp --> postfix_exp - -
    def __init__(self, postfix_exp, Minus, Minus):
        self.postfix_exp = postfix_exp


class argument_exp_listp53(argument_exp_list):
    # argument_exp_list --> assignment_exp argument_exp_list
    def __init__(self, assignment_exp, argument_exp_list):
        self.assignment_exp = assignment_exp
        self.argument_exp_list = argument_exp_list


class argument_exp_listp54(argument_exp_list):
    # argument_exp_list -->
    def __init__(self):
        pass


class unary_expp55(unary_exp):
    # unary_exp --> postfix_exp
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp


class unary_expp56(unary_exp):
    # unary_exp --> + + unary_exp
    def __init__(self, Plus, Plus, unary_exp):
        self.unary_exp = unary_exp


class unary_expp57(unary_exp):
    # unary_exp --> - - unary_exp
    def __init__(self, Minus, Minus, unary_exp):
        self.unary_exp = unary_exp


class unary_expp58(unary_exp):
    # unary_exp --> unary_op unary_exp
    def __init__(self, unary_op, unary_exp):
        self.unary_op = unary_op
        self.unary_exp = unary_exp


class unary_opp59(unary_op):
    # unary_op --> +
    def __init__(self, Plus):
        pass


class unary_opp60(unary_op):
    # unary_op --> -
    def __init__(self, Minus):
        pass


class unary_opp61(unary_op):
    # unary_op --> !
    def __init__(self, NOT):
        pass


class unary_opp62(unary_op):
    # unary_op --> ~
    def __init__(self, Tilde):
        pass


class binary_expp63(binary_exp):
    # binary_exp --> unary_exp
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp


class binary_expp64(binary_exp):
    # binary_exp --> binary_exp binary_op unary_exp
    def __init__(self, binary_exp, binary_op, unary_exp):
        self.binary_exp = binary_exp
        self.binary_op = binary_op
        self.unary_exp = unary_exp


class binary_opp65(binary_op):
    # binary_op --> *
    def __init__(self, Times):
        pass


class binary_opp66(binary_op):
    # binary_op --> /
    def __init__(self, Divide):
        pass


class binary_opp67(binary_op):
    # binary_op --> %
    def __init__(self, Percent):
        pass


class binary_opp68(binary_op):
    # binary_op --> +
    def __init__(self, Plus):
        pass


class binary_opp69(binary_op):
    # binary_op --> -
    def __init__(self, Minus):
        pass


class binary_opp70(binary_op):
    # binary_op --> < <
    def __init__(self, LT, LT):
        pass


class binary_opp71(binary_op):
    # binary_op --> > >
    def __init__(self, GT, GT):
        pass


class binary_opp72(binary_op):
    # binary_op --> <
    def __init__(self, LT):
        pass


class binary_opp73(binary_op):
    # binary_op --> >
    def __init__(self, GT):
        pass


class binary_opp74(binary_op):
    # binary_op --> < =
    def __init__(self, LT, Assign):
        pass


class binary_opp75(binary_op):
    # binary_op --> > =
    def __init__(self, GT, Assign):
        pass


class binary_opp76(binary_op):
    # binary_op --> ==
    def __init__(self, EQ):
        pass


class binary_opp77(binary_op):
    # binary_op --> !=
    def __init__(self, NEQ):
        pass


class binary_opp78(binary_op):
    # binary_op --> &
    def __init__(self, Ampersand):
        pass


class binary_opp79(binary_op):
    # binary_op --> ^
    def __init__(self, Caret):
        pass


class binary_opp80(binary_op):
    # binary_op --> |
    def __init__(self, VerticalBar):
        pass


class binary_opp81(binary_op):
    # binary_op --> & &
    def __init__(self, Ampersand, Ampersand):
        pass


class binary_opp82(binary_op):
    # binary_op --> | |
    def __init__(self, VerticalBar, VerticalBar):
        pass


class conditional_expp83(conditional_exp):
    # conditional_exp --> binary_exp
    def __init__(self, binary_exp):
        self.binary_exp = binary_exp


class conditional_expp84(conditional_exp):
    # conditional_exp --> binary_exp ? exp : conditional_exp
    def __init__(self, binary_exp, Question, exp, Colon, conditional_exp):
        self.binary_exp = binary_exp
        self.exp = exp
        self.conditional_exp = conditional_exp


class assignment_expp85(assignment_exp):
    # assignment_exp --> conditional_exp
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp


class assignment_expp86(assignment_exp):
    # assignment_exp --> unary_exp assignment_op assignment_exp
    def __init__(self, unary_exp, assignment_op, assignment_exp):
        self.unary_exp = unary_exp
        self.assignment_op = assignment_op
        self.assignment_exp = assignment_exp


class assignment_opp87(assignment_op):
    # assignment_op --> =
    def __init__(self, Assign):
        pass


class assignment_opp88(assignment_op):
    # assignment_op --> * =
    def __init__(self, Times, Assign):
        pass


class assignment_opp89(assignment_op):
    # assignment_op --> / =
    def __init__(self, Divide, Assign):
        pass


class assignment_opp90(assignment_op):
    # assignment_op --> %=
    def __init__(self, ModAssign):
        pass


class assignment_opp91(assignment_op):
    # assignment_op --> + =
    def __init__(self, Plus, Assign):
        pass


class assignment_opp92(assignment_op):
    # assignment_op --> - =
    def __init__(self, Minus, Assign):
        pass


class assignment_opp93(assignment_op):
    # assignment_op --> < < =
    def __init__(self, LT, LT, Assign):
        pass


class assignment_opp94(assignment_op):
    # assignment_op --> > > =
    def __init__(self, GT, GT, Assign):
        pass


class assignment_opp95(assignment_op):
    # assignment_op --> &=
    def __init__(self, AndAssign):
        pass


class assignment_opp96(assignment_op):
    # assignment_op --> ^=
    def __init__(self, XorAssign):
        pass


class assignment_opp97(assignment_op):
    # assignment_op --> |=
    def __init__(self, OrAssign):
        pass


class expp98(exp):
    # exp --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp


class expp99(exp):
    # exp --> exp , assignment_exp
    def __init__(self, exp, Comma, assignment_exp):
        self.exp = exp
        self.assignment_exp = assignment_exp


class decp100(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list


class dec_specifierp101(dec_specifier):
    # dec_specifier --> 'void'
    def __init__(self, void):
        pass


class dec_specifierp102(dec_specifier):
    # dec_specifier --> 'char'
    def __init__(self, char):
        pass


class dec_specifierp103(dec_specifier):
    # dec_specifier --> 'short'
    def __init__(self, short):
        pass


class dec_specifierp104(dec_specifier):
    # dec_specifier --> 'int'
    def __init__(self, int):
        pass


class dec_specifierp105(dec_specifier):
    # dec_specifier --> 'long'
    def __init__(self, long):
        pass


class dec_specifierp106(dec_specifier):
    # dec_specifier --> 'float'
    def __init__(self, float):
        pass


class dec_specifierp107(dec_specifier):
    # dec_specifier --> 'double'
    def __init__(self, double):
        pass


class dec_specifierp108(dec_specifier):
    # dec_specifier --> struct_specifier
    def __init__(self, struct_specifier):
        self.struct_specifier = struct_specifier


class struct_specifierp109(struct_specifier):
    # struct_specifier --> 'struct' ID
    def __init__(self, struct, ID):
        self.ID = ID


class struct_specifierp110(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list


class struct_dec_listp111(struct_dec_list):
    # struct_dec_list --> struct_dec
    def __init__(self, struct_dec):
        self.struct_dec = struct_dec


class struct_dec_listp112(struct_dec_list):
    # struct_dec_list --> struct_dec_list struct_dec
    def __init__(self, struct_dec_list, struct_dec):
        self.struct_dec_list = struct_dec_list
        self.struct_dec = struct_dec


class struct_decp113(struct_dec):
    # struct_dec --> dec_specifier declarator_list
    def __init__(self, dec_specifier, declarator_list):
        self.dec_specifier = dec_specifier
        self.declarator_list = declarator_list


class declarator_listp114(declarator_list):
    # declarator_list --> declarator
    def __init__(self, declarator):
        self.declarator = declarator


class declarator_listp115(declarator_list):
    # declarator_list --> declarator_list , declarator
    def __init__(self, declarator_list, Comma, declarator):
        self.declarator_list = declarator_list
        self.declarator = declarator


class declaratorp116(declarator):
    # declarator --> ID
    def __init__(self, ID):
        self.ID = ID


class declaratorp117(declarator):
    # declarator --> ( declarator )
    def __init__(self, LParen, declarator, RParen):
        self.declarator = declarator


class declaratorp118(declarator):
    # declarator --> declarator [ exp ]
    def __init__(self, declarator, LBrack, exp, RBrack):
        self.declarator = declarator
        self.exp = exp


class declaratorp119(declarator):
    # declarator --> declarator ( parameter_list )
    def __init__(self, declarator, LParen, parameter_list, RParen):
        self.declarator = declarator
        self.parameter_list = parameter_list


class parameter_listp120(parameter_list):
    # parameter_list --> parameter_dec
    def __init__(self, parameter_dec):
        self.parameter_dec = parameter_dec


class parameter_listp121(parameter_list):
    # parameter_list --> parameter_list , parameter_dec
    def __init__(self, parameter_list, Comma, parameter_dec):
        self.parameter_list = parameter_list
        self.parameter_dec = parameter_dec


class parameter_decp122(parameter_dec):
    # parameter_dec --> dec_specifier declarator
    def __init__(self, dec_specifier, declarator):
        self.dec_specifier = dec_specifier
        self.declarator = declarator


class init_dec_listp123(init_dec_list):
    # init_dec_list --> init_dec
    def __init__(self, init_dec):
        self.init_dec = init_dec


class init_dec_listp124(init_dec_list):
    # init_dec_list --> init_dec_list , init_dec
    def __init__(self, init_dec_list, Comma, init_dec):
        self.init_dec_list = init_dec_list
        self.init_dec = init_dec


class init_decp125(init_dec):
    # init_dec --> declarator
    def __init__(self, declarator):
        self.declarator = declarator


class init_decp126(init_dec):
    # init_dec --> declarator = exp
    def __init__(self, declarator, Assign, exp):
        self.declarator = declarator
        self.exp = exp


class stmp127(stm):
    # stm --> exp_stm
    def __init__(self, exp_stm):
        self.exp_stm = exp_stm


class stmp128(stm):
    # stm --> compound_stm
    def __init__(self, compound_stm):
        self.compound_stm = compound_stm


class stmp129(stm):
    # stm --> selection_stm
    def __init__(self, selection_stm):
        self.selection_stm = selection_stm


class stmp130(stm):
    # stm --> iteration_stm
    def __init__(self, iteration_stm):
        self.iteration_stm = iteration_stm


class stmp131(stm):
    # stm --> jump_stm
    def __init__(self, jump_stm):
        self.jump_stm = jump_stm


class exp_stmp132(exp_stm):
    # exp_stm --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp


class exp_stmp133(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass


class compound_stmp134(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list


class compound_stmp135(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass


class block_item_listp136(block_item_list):
    # block_item_list --> block_item
    def __init__(self, block_item):
        self.block_item = block_item


class block_item_listp137(block_item_list):
    # block_item_list --> block_item_list block_item
    def __init__(self, block_item_list, block_item):
        self.block_item_list = block_item_list
        self.block_item = block_item


class block_itemp138(block_item):
    # block_item --> dec
    def __init__(self, dec):
        self.dec = dec


class block_itemp139(block_item):
    # block_item --> stm
    def __init__(self, stm):
        self.stm = stm


class selection_stmp140(selection_stm):
    # selection_stm --> 'if' ( exp ) stm
    def __init__(self, if, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm


class selection_stmp141(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, if, LParen, exp, RParen, stm, else, stm):
        self.exp = exp
        self.stm = stm
        self.stm = stm


class iteration_stmp142(iteration_stm):
    # iteration_stm --> 'while' ( exp ) stm
    def __init__(self, while, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm


class iteration_stmp143(iteration_stm):
    # iteration_stm --> 'do' stm 'while' ( exp ) ;
    def __init__(self, do, stm, while, LParen, exp, RParen, Semicolon):
        self.stm = stm
        self.exp = exp


class iteration_stmp144(iteration_stm):
    # iteration_stm --> 'for' ( exp ; exp ; exp ) stm
    def __init__(self, for, LParen, exp, Semicolon, exp, Semicolon, exp, RParen, stm):
        self.exp = exp
        self.exp = exp
        self.exp = exp
        self.stm = stm


class jump_stmp145(jump_stm):
    # jump_stm --> 'goto' ID
    def __init__(self, goto, ID):
        self.ID = ID


class jump_stmp146(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, continue):
        pass


class jump_stmp147(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, break):
        pass


class jump_stmp148(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, return, exp, Semicolon):
        self.exp = exp


class Test(unittest.TestCase):


    def test(self):
        pass
