memory = {}
def memoize_fibonacci(f):

    #This inner function has access to memory and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            # print('result saved in memory')
        # else:
        #     print('returning result from saved memory')
        return memory[num]
    
    return inner

@memoize_fibonacci
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

res = fibonacci(50)
print(res)