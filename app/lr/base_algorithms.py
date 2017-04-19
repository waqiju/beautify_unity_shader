import unittest
from .base_types import ObjectSet, ItemLR0, Item
from ..syntax_nonterminal import Nonterminal

# below is algorithm for LR0
def calcClosureLR0(productionList, itemSet):
    isDirty = True
    closure = ObjectSet(itemSet)

    while(isDirty > 0):
        isDirty = False

        for item in closure:
            symbolType = item.getNextSymbolType()
            # arrive the endding of product
            if symbolType is None or isinstance(symbolType, str):
                continue

            Symbol = Nonterminal.getClass(symbolType.name)
            if Symbol:
                closure, isTmpDirty = ObjectSet.unionReportDirty(closure, _productions2ItemSetLR0(Symbol.leadingProductions))
                isDirty = isDirty + isTmpDirty

    return closure


def gotoLR0(productionList, itemSet, tokenType):
    newState = ObjectSet()

    for item in itemSet:
        if item.getNextSymbolType() == tokenType:
            newState.add(item.moveNext())

    return calcClosureLR0(productionList, newState)


def _productions2ItemSetLR0(productions):
    itemSet = ObjectSet()
    for p in productions:
        itemSet.add(ItemLR0(p))

    return itemSet


# below is algorithm for LR1
def calcClosure(productionList, firstDict, nullableDict, itemSet):
    dirtyCount = True
    closure = ObjectSet(itemSet)
    # print(closure)

    while dirtyCount > 0:
        dirtyCount = False

        for item in closure:
            x = item.getNextSymbolType()
            if x is None or isinstance(x, str) or not x.isNonterminal(): # todo refactor
                continue

            # print(x.name)
            XClass = Nonterminal.getClass(x.name)
            for production in XClass.leadingProductions:
                tail = item.getTailSTList()
                # print('----', production, tail, calcSTListFirst(firstDict, nullableDict, tail))
                for lookAheadST in calcSTListFirst(firstDict, nullableDict, tail): # todo
                    closure, isDirty = ObjectSet.unionReportDirty(closure, _production2ItemSet(production, lookAheadST))
                    dirtyCount += isDirty

        # print(closure)

    return closure


def _production2ItemSet(production, lookAheadST):
    item = Item(production, 0, lookAheadST)
    itemSet = ObjectSet()
    itemSet.add(item)

    return itemSet


def calcFirstDict(productionList, TokenType):
    r''' 
      firstDict, ST -> ObjectSet { ST ... } . Not **STList** ->  
      nullableDict, ST -> True/False
    '''

    # init
    # todo deal with things like 'if'
    firstDict = {}
    for production in productionList:
        x = production.left
        if not firstDict.get(x):
            firstDict[x] = ObjectSet()

        for y in production.right:
            if not firstDict.get(y):
                firstDict[y] = ObjectSet()

    for ty in TokenType:
        if not firstDict.get(ty):
            firstDict[ty] = ObjectSet()
        firstDict[ty].add(ty)

    nullableDict = {}
    nullableDict[TokenType.NULL] = True

    dirtyCount = 1
    while dirtyCount > 0:
        dirtyCount = 0

        for production in productionList:
            x = production.left
            if _isAllNullable(nullableDict, production.right) and not nullableDict.get(x):
                nullableDict[x] = True
                dirtyCount += 1

            for i in range(0, len(production.right)):
                y = production.right[i]

                firstDict[x], isDirty = ObjectSet.unionReportDirty(firstDict[x], firstDict[y])
                dirtyCount += isDirty

                if not nullableDict.get(y):
                    break

    return firstDict, nullableDict


def calcSTListFirst(firstDict, nullableDict, stList):
    first = ObjectSet()

    for st in stList:
        first = ObjectSet.union(first, firstDict[st])

        if not nullableDict.get(st):
            break

    return first


def goto(productionList, firstDict, nullableDict, itemSet, tokenType):
    newState = ObjectSet()

    for item in itemSet:
        if item.getNextSymbolType() == tokenType:
            newState.add(item.moveNext())

    return calcClosure(productionList, firstDict, nullableDict, newState)


def _isAllNullable(nullableDict, stList):
    for st in stList:
        if not nullableDict.get(st):
            return False

    return True


class Test(unittest.TestCase):

    def test(self):
        firstDict, nullableDict = calcFirstDict(productionList, TokenType)

        for ty in firstDict:
            print(ty, '-->')
            for ty2 in firstDict[ty]:
                print('\t', ty2)

        print(nullableDict)