from ..syntax_production import Production
from .base_types import ObjectSet, Item
from .base_algorithms import calcClosure, goto, calcFirstDict
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
    beginningItemSet.add(Item(beginningProduction, 0, '*'))

    # 初始化symbolType
    from test.lr1_test.tokens import TokenType
    from test.lr1_test.nonterminals import NonterminalType
    SymbolType = [ty for ty in TokenType] + [ty for ty in NonterminalType]

    # 根据productionList获取firstDict和nullableDict
    firstDict, nullableDict = calcFirstDict(productionList, TokenType)

    # 初始化stateSet
    beginningState = calcClosure(productionList, firstDict, nullableDict, beginningItemSet)
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
                _addEdge(edges, stateIndex, st if isinstance(st, str) else st.name, 'r' + productionNo)

        # 放置Shift
        for ty in SymbolType:
            newState = goto(productionList, firstDict, nullableDict, state, ty)
            if len(newState) == 0:
                continue

            if not stateSet.has(newState):
                stateSet.add(newState)
                stateList.append(newState)

            _addEdge(edges, stateIndex, ty.name, 's%s' % stateSet.getSerialNumber(newState))

        stateIndex = stateIndex + 1

    for i, state in enumerate(stateList):
        print(i, state)

    print('---------------------------------')
    _printCell('')
    for ty in SymbolType:
        _printCell(ty.name)
    print('')

    for i, state in enumerate(stateList):
        _printCell(str(i))
        for ty in SymbolType:
            actionStr = str(edges[i][ty.name] if edges[i].get(ty.name) else '')
            _printCell(actionStr)
        print('')


def _addEdge(edges, key1, key2, action):
    oldValue = edges[key1].get(key2)
    if oldValue is None:
        edges[key1][key2] = action
    elif isinstance(oldValue, str) and oldValue != action:
        edges[key1][key2] = [oldValue, action]
    elif isinstance(oldValue, list) and not action in edges[key1][key2]:
        edges[key1][key2].append(action)
    else:
        print('should not go here!')


def _printCell(text):
    for i in range(len(text), 15):
        text = text + ' '
    print(text, end='')


class Test(unittest.TestCase):

    def test(self):
        from test.lr1_test.productions import productionList
        for p in productionList:
            print(p)
        print('--------------------------------')
        dfmEdges = construct(productionList)


    def DDtestFirstDict(self):        
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
        beginningItemSet.add(Item(beginningProduction, 0, endingTerminal))

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
