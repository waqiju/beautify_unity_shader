from .base_types import ObjectSet, Item
from ..syntax_nonterminal import Nonterminal


def calcClosure(productList, itemSet):
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
                closure, isTmpDirty = ObjectSet.unionReportDirty(closure, _productions2ItemSet(Symbol.leadingProductions))
                isDirty = isDirty + isTmpDirty

    return closure


def goto(productList, itemSet, tokenType):
    newState = ObjectSet()

    for item in itemSet:
        if item.getNextSymbolType() == tokenType:
            newState.add(item.moveNext())

    return calcClosure(productList, newState)


def _productions2ItemSet(productions):
    itemSet = ObjectSet()
    for p in productions:
        itemSet.add(Item(p))

    return itemSet