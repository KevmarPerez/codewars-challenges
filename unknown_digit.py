def solve_runes(runes):
    ops = ['+', '-', '*']
    operands, result = runes.split("=")
    for val in operands:
        if val in ops:
            return val
            
print(solve_runes("1+-1=?"))