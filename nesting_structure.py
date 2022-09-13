def same_structure_as(original,other):
    if len(original) == len(other):
        for i in range(len(original)):
            if type(original[i]) != type(other[i]):
                return False
        return True
    return False

arr1 = same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
arr2 = same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ])
test = arr1
print(test)