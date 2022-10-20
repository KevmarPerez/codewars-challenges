keypad = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ['','0','']
]

num=['8', '11', '369']
def get_index(n):
    # find the position of the value of interest and returns a list of its position
    for i, x in enumerate(keypad):
        if n in x:
            return [i, x.index(n)]

def find_adj(n):
    # find the adjacent values of any individual value passed
    # e.g for 2 => [1,3,5,2] returned as a string
    val = get_index(n)
    rc = keypad[val[0]][val[1]]
    c1 = keypad[val[0]-1][val[1]] if val[0] != 0 else None
    c2 = keypad[val[0]+1][val[1]] if val[0] < len(keypad)-1 else None
    r1 = keypad[val[0]][val[1]-1] if val[1] != 0 else None
    r2 = keypad[val[0]][val[1]+1] if val[1] < len(keypad[0])-1 else None
    raw_adj = [rc, r1, r2, c1, c2]
    return [v for v in raw_adj if v not in [None, '']]

def comb_func(ls1, ls2):
    # Combines 2 lists into one
    # e.g [['1', '2', '4'], ['2', '1', '3', '5']] => ['12', '11', '13', '15', '22', '21', '23', '25', '42', '41', '43', '45']
    new_ls = []
    for a in ls1:
        for b in ls2:
            new_ls.append(a+b)
    return new_ls

def get_pins(observed):
    adj_ls = [find_adj(n) for n in observed]
    init_ls = adj_ls[0]
    if len(observed) >1:
        for item in adj_ls[1:]:
            adj_comb = comb_func(init_ls, item)
            init_ls = adj_comb
        return sorted(adj_comb)
    else:
        return adj_ls[0]


    