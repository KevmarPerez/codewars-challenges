def lcs(x,y):
    lst  = []
    for i in list(y):
        if i in x and i not in lst:
            lst.append(i)
    # lst = [i for i in list(y) if i in x]
    return ''.join(lst)
    # return ''.join([i for i in list(y) if i in x])

test = lcs("anothertest", "notatest")
print(test)