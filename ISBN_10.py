test_val = '1112223339'

def linear_sol():
    myList = []
    for pos in range(len(test_val)):
        val = int(test_val[pos])* (pos+1)
        myList.append(val)
    sumList = sum(myList)
    mod_val = sumList % 11
    valid = True if not mod_val else False
    return valid

def alt_sol():
    valid = sum([pos*int(val) for pos, val in enumerate(list(test_val),1)]) % 11
    return True if not valid else False

print(alt_sol())

# x  = [num for num in range(1,11)]

# myList = [pos*val for pos, val in enumerate(x,1)]
# print(sum(myList))