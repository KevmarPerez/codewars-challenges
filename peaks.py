def pick_peaks(arr):
    pos = []
    peak = []
    mylist = []
    for x in range(len(arr)):
        if arr[x] == 1:
            mylist.append(x)
    return mylist

test = [1,2,3,6,4,1,2,3,2,1]
print(pick_peaks(test))