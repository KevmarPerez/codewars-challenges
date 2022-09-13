import operator
def calc(expr):
    li = expr.split()
    ''.join(list(li))
    if len(li) > 0 and len(li) > 2:
        a = int(li[0])
        b = int(li[1])
        oper = li[2]
    else:
        result = int(li)
    if oper == "+":
        result =operator.add(a,b)
    elif oper == "-":
        result =operator.sub(a,b)
    elif oper == "*":
        result =operator.mul(a,b)
    elif oper == "/":
        result = operator.truediv(a,b)
    return 0 if len(expr) == 0 else result

val = "1 3 +"
print(calc(val))