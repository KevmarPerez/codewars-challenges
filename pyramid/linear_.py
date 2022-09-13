def beeramid(bonus, price):
    n = 0
    sum_of_cans = 0
    while (bonus // price)-sum_of_cans>=(n+1)**2:
        n += 1
        sum_of_cans = sum([cpl**2 for cpl in range(1,n+1)])
    # return n
    print(n, sum_of_cans)


beeramid(5000, 3)