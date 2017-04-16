from ..syntax_production import Production
from .base_types import ObjectSet, Item
from .base_algorithms import calcClosure, goto
import unittest


beginningNonterminal = '__Begin'
endingTerminal = '__End'


def construct(productionList):
    # 加入S -> XX $
    firstNonterminalType = productionList[0].left
    beginningProduction = Production(
        '%s -> %s %s' % (beginningNonterminal,
                         firstNonterminalType.name, endingTerminal),
        'p0',
        beginningNonterminal,
        (firstNonterminalType, endingTerminal),
    )
    productionList.insert(0, beginningProduction)
    beginningItemSet = ObjectSet()
    beginningItemSet.add(Item(beginningProduction))

    # 初始化stateSet
    beginningState = calcClosure(productionList, beginningItemSet)
    stateSet = ObjectSet()
    stateSet.add(beginningState)
    stateList = []
    stateList.append(beginningState)
    # 初始化edges
    edges = {}
    # 初始化symbolType
    from test.lr_test.tokens import TokenType
    from test.lr_test.nonterminals import NonterminalType
    SymbolType = [ty for ty in TokenType] + [ty for ty in NonterminalType]

    stateIndex = 0
    while (stateIndex < len(stateList)):
        state = stateList[stateIndex]
        edges[stateIndex] = {}

        # 放置Reduce
        for item in state:
            if item.getNextSymbolType() is None:
                productionNo = item.production.name[1:]
                for ty in TokenType:
                    edges[stateIndex][ty.name] = 'r' + productionNo

        # 放置Shift
        for ty in SymbolType:
            newState = goto(productionList, state, ty)
            if len(newState) == 0:
                continue

            if not stateSet.has(newState):
                stateSet.add(newState)
                stateList.append(newState)

            edges[stateIndex][
                ty.name] = 's%s' % stateSet.getSerialNumber(newState)

        stateIndex = stateIndex + 1

    for i, state in enumerate(stateList):
        print(i, state)

    print('---------------------------')
    for ty in SymbolType:
        print(ty.name + '\t', end='')
    print('')

    for i, state in enumerate(stateList):
        for ty in SymbolType:
            print((edges[i][ty.name] if edges[i].get(
                ty.name) else '\t') + '\t', end='')
        print('')


class Test(unittest.TestCase):

    def test(self):
        from test.lr_test.productions import productionList
        dfmEdges = construct(productionList)

    # 测试s0和s1
    def DDtest2(self):
        from test.lr_test.productions import productionList
        # 加入S -> XX $
        firstNonterminalType = productionList[0].left
        beginningProduction = Production(
            '%s -> %s %s' % (beginningNonterminal,
                             firstNonterminalType.name, endingTerminal),
            'p0',
            beginningNonterminal,
            (firstNonterminalType, endingTerminal),
        )
        productionList.insert(0, beginningProduction)
        beginningItemSet = ObjectSet()
        beginningItemSet.add(Item(beginningProduction))

        stateSet = ObjectSet()
        s = calcClosure(productionList, beginningItemSet)
        print(s)

        from ..lex_tokens import TokenType
        s1 = goto(productionList, s, TokenType.ID)
        print(s1)
