import re
def to_postfix (infix):
    """Convert infix to postfix"""
    # 1) parentheses, 2) exponentiation, 3) times/divide, 4) plus/minus
    par = ['(',')']
    operators = ['+', '-', '*', '\\', '*']
    find_par = re.findall('\(.*?\)', infix)
    for strings in find_par:
        re_arr = ''.join([r for r in strings if r not in par])
    return re_arr

if __name__ == '__main__':
    s = "5+(6-2)*9+3^(7-1)"
    x = re.sub('\(|\)', " ", s)
    print(x)
    # print(to_postfix(s))