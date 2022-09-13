import numpy as np
def fold_array(array, runs):
    for run in  range(runs):
        n = len(array)
        if n % 2 != 0:
            array.insert(round(n/2), 0) 
        newarr = np.array_split(array, 2)
        result = map(lambda x, y: x+y, newarr[0], np.flipud(newarr[1]))
        array = list(result)
    else:
        return array

arr = [-9, 9, -8, 8, 66, 23]
print(fold_array(arr, 1))