def dig_pow(n, p):
    q, rem = divmod(sum([int(elem)**(p+index) for index, elem in enumerate(str(n))]), n)
    return q if rem ==0 else -1

print(dig_pow(3456789,5))

# my_list = [1,4,3,4,3]
# for i, val in enumerate(my_list):
#     print(i,",", val)
46288, 3456789, 3456789
5,1,5