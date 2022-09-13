from operator import *
ops = {
    '+' : add,'-' : sub,'*' : mul,'/' : truediv}

def zero(m=None, n=0):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def one(m=None, n=1):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def two(m=None, n=2):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def three(m=None, n=3):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def four(m=None, n=4):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def five(m=None, n=5):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def six(m=None, n=6):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def seven(m=None, n=7):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def eight(m=None, n=8):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def nine(m=None, n=9):
    if m != None:
        op, val = m
        return int(ops[op](n, val))
    return n

def plus(n):
    return  '+', n
def minus(n):
    return  '-', n
def times(n):
    return  '*', n
def divided_by(n):
    return  '/', n


print(five(divided_by(six())))