def array_diff(a,b):
    for elem_b in b:
        print(elem_b)
        while elem_b in a:
            a.remove(elem_b)

    return a

result = array_diff([], [1,2])

# my_arr = [1,4,3,2,6,4]
# while 4 in my_arr:
#     my_arr.remove(4)
# print(my_arr)
    
# print(4 in my_arr)
# for el in my_arr:
#     if el == 4:
#         del my_arr[my_arr.index(el)]


# print(my_arr)
# print(result)