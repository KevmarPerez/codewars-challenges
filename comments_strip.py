test = "apples, pears # and bananas\ngrapes\nbananas !apples"
cond = ["#", "!"]
split_lines = test.split('\n')
el = [string.split(' ') for string in split_lines]
for ls in el:
    for char in cond:
        for val in ls:
            if char in val:
                break
    print(val)
