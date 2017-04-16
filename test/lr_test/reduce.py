from .nonterminals import *

def r1(t, e):
    e = E()
    e.lhs = t
    e.rhs = e
    return e


def r2(t):
    e = E()
    e.lhs = t
    pass


def r3():
    pass
