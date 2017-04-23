from ..syntax_production import Production
from ..symbol_type import SymbolType
from .base_types import ObjectSet, Item
from .base_algorithms import calcClosure, goto, calcFirstDict
import unittest


BeginningNonterminal = '__Begin'
EndingTerminal = '__End'


def construct(productionList, isDebug=False):
    # 初始化symbolType
    TokenType = SymbolType.TokenType
    NonterminalType = SymbolType.NonterminalType

    # 加入S -> XX $
    NonterminalType.add(BeginningNonterminal)
    TokenType.add(EndingTerminal)

    firstNonterminalType = productionList[0].left
    beginningProduction = Production(
        '%s -> %s %s' % (BeginningNonterminal,
                         firstNonterminalType, EndingTerminal),
        'p0',
        BeginningNonterminal,
        (firstNonterminalType, EndingTerminal),
    )
    productionList.insert(0, beginningProduction)

    # 根据productionList获取firstDict和nullableDict
    firstDict, nullableDict = calcFirstDict(productionList, TokenType)

    # 初始的ItemSet
    beginningItemSet = ObjectSet()
    beginningItemSet.add(Item(beginningProduction, 0, '*'))
    beginningState = calcClosure(productionList, firstDict, nullableDict, beginningItemSet)

    # 初始的StateSet
    stateSet = ObjectSet()
    stateSet.add(beginningState)
    stateList = []
    stateList.append(beginningState)

    # 初始化edges
    edges = {}

    stateIndex = 0
    while (stateIndex < len(stateList)):
        state = stateList[stateIndex]
        edges[stateIndex] = {}

        # 放置Reduce
        for item in state:
            if item.getNextSymbolType() is None:
                productionNo = item.production.name[1:]
                st = item.getLookAheadST()
                _addEdge(edges, stateIndex, st, 'r' + productionNo)

        # 放置Shift
        for ty in SymbolType:
            newState = goto(productionList, firstDict, nullableDict, state, ty)
            if len(newState) == 0:
                continue

            # 放置Accept
            if ty == EndingTerminal:
                _addEdge(edges, stateIndex, ty, 'a')
                continue

            if not stateSet.has(newState):
                stateSet.add(newState)
                stateList.append(newState)

            _addEdge(edges, stateIndex, ty, 's%s' % stateSet.getSerialNumber(newState))

        stateIndex = stateIndex + 1

    if isDebug:
        _printStateList(stateList)
        _printEdges(edges)

    return edges


def _addEdge(edges, key1, key2, action):
    oldValue = edges[key1].get(key2)
    if oldValue is None:
        edges[key1][key2] = action
    elif isinstance(oldValue, str):
        if oldValue != action:
            edges[key1][key2] = [oldValue, action]
    elif isinstance(oldValue, list) and action not in edges[key1][key2]:
        edges[key1][key2].append(action)
    else:
        print('should not go here!')


def _printCell(text):
    for i in range(len(text), 15):
        text = text + ' '
    print(text, end='')


def _printProductionList(productionList):
    print('-------ProductionList-----------')
    for p in productionList:
        print(p)
    print('--------------------------------')


def _printStateList(stateList):
    print('-----------StateList------------')
    for i, state in enumerate(stateList):
        print(i, state)
    print('--------------------------------')


def _printEdges(edges):
    print('------------Edges---------------')
    _printCell('')
    for ty in SymbolType:
        _printCell(ty)
    print('')

    for i, _ in enumerate(edges):
        _printCell(str(i))
        for ty in SymbolType:
            actionStr = str(edges[i][ty] if edges[i].get(ty) else '')
            _printCell(actionStr)
        print('')
    print('--------------------------------')



class Test(unittest.TestCase):

    def test(self):
        from test.lr1_test.productions import productionList
        _printProductionList(productionList)
        edges = construct(productionList)
        _printEdges(edges)



    def DDtestFirstDict(self):        
        # 加入S -> XX $
        firstNonterminalType = productionList[0].left
        beginningProduction = Production(
            '%s -> %s %s' % (BeginningNonterminal,
                             firstNonterminalType, EndingTerminal),
            'p0',
            BeginningNonterminal,
            (firstNonterminalType, EndingTerminal),
        )
        productionList.insert(0, beginningProduction)
        beginningItemSet = ObjectSet()
        beginningItemSet.add(Item(beginningProduction, 0, EndingTerminal))

        # 初始化symbolType
        from test.lr1_test.tokens import TokenType
        from test.lr1_test.nonterminals import NonterminalType
        SymbolType = [ty for ty in TokenType] + [ty for ty in NonterminalType]

        # 根据productionList获取firstDict和nullableDict
        firstDict, nullableDict = calcFirstDict(productionList, TokenType)
        for st in firstDict:
            print(st)
            for st2 in firstDict[st]:
                print('\t', st2)

        print(nullableDict)
