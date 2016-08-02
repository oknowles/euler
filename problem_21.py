def sum_divisors(n):
    return sum([i for i in range(1, (n / 2) + 1) if (n % i == 0)])

def find_amicable_pairs(upper_bound):
    amicable_pairs = []
    for x in range(1,upper_bound):
        y = sum_divisors(x)
        if (x < y) and (sum_divisors(y) == x):
            amicable_pairs.append([x,y])
    return amicable_pairs

print sum([sum(l) for l in find_amicable_pairs(10000)])
