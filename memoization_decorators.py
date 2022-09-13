memory = {}

def memoize_factorial(f):

    #This inner function has access to memory and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('rtrunng result from saved memory')
        return memory[num]
    
    return inner

@memoize_factorial
def factorial(num):
    return 1 if num == 1 else num * factorial(num-1)

print(factorial(4))