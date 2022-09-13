ran = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
myList = []
temp = [] 

for i in range(len(ran)):
    if i < (len(ran)-1):
        current = ran[i]
        next_val = ran[i+1]
        if current+1 != next_val:
            temp.append(next_val)
print(temp)