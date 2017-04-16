from enum import Enum
import unittest


class ObjectSet:

    def __init__(self, srcSet=None):
        self.set = {}
        self.serialNumber = {}
        self.hashValue = ''

        if srcSet:
            for i in srcSet:
                self.add(i)

    def add(self, obj):
        if self.has(obj):
            return

        key = obj.getHashValue()
        self.set[key] = obj
        self.serialNumber[key] = len(self) - 1
        self.updateHashValue()

    def has(self, obj):
        return self.set.get(obj.getHashValue()) is not None

    @staticmethod
    def unionReportDirty(lhs, rhs):
        newSet = ObjectSet(lhs)
        for i in rhs:
            newSet.add(i)

        if len(newSet) > len(lhs):
            return newSet, True
        else:
            return newSet, False

    def __len__(self):
        return self.set.__len__()

    def __iter__(self):
        return (self.set[key] for key in self.set)

    def __str__(self):
        text = ''
        for obj in self:
            text = text + str(obj) + ', '
        return '(%s)' % text

    def updateHashValue(self):
        self.hashValue = ''
        for key in sorted(self.set.keys()):
            self.hashValue = self.hashValue + '__S_' + key

    def getHashValue(self):
        return self.hashValue

    def getSerialNumber(self, obj):
        return self.serialNumber.get(obj.getHashValue())


class Item:

    def __init__(self, production, point=0):
        self.production = production
        self.point = point
        # may there is a better way
        self.hashValue = '__h_' + str(production) + '__p_' + str(point)

    def getHashValue(self):
        return self.hashValue

    def getNextSymbolType(self):
        if self.point < len(self.production.right):
            return self.production.right[self.point]
        else:
            return None

    def moveNext(self):
        return Item(self.production, self.point + 1)

    def __str__(self):
        # return 'Item<%s , %s>' % (str(self.production), self.point)

        left = self.production.left
        text = '%s -> ' % (left.name if isinstance(left, Enum) else left)
        for index, symbolTypeOrString in enumerate(self.production.right):
            if self.point == index:
                text = text + '.'
            text = text + (symbolTypeOrString.name if isinstance(
                symbolTypeOrString, Enum) else symbolTypeOrString) + ' '
        if self.point == len(self.production.right):
            text = text[:-1] + '. '
        return text


class Test(unittest.TestCase):

    def test(self):
        item1 = Item('production', 1)
        item2 = Item('prod', 2)
        item3 = Item('prod', 3)

        s1 = ObjectSet()
        s1.add(item1)
        s1.add(item1)
        self.assertTrue(len(s1) == 1)

        s2 = ObjectSet()
        s2.add(item2)
        s2.add(item3)
        self.assertTrue(len(s2) == 2)

        s3, isDirty = ObjectSet.unionReportDirty(s1, s2)
        self.assertTrue(isDirty)
        self.assertTrue(len(s3) == 3)
