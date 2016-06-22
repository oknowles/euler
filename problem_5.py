def divisible_by_set(n, nums):
    for i in nums:
        if ((n % i) != 0):
            return False
    return True

# find the unique factors in a given range, e.g. for upper_limit = 10
# the unique factors would be 6,7,8,9,10
# that is, if a number is divisible by 10 then it is also divisible by 5 so no need to check that
def unique_factors(upper_limit):
    factors = range(2, upper_limit + 1)

    for i in range(1, upper_limit):
        j = 2
        while (i * j <= upper_limit):
            if i * j in factors:
                if i in factors:
                    factors.remove(i)
            j += 1
    return factors

print(unique_factors(20))

def smallest_multiple(max_range):
    facs = unique_factors(max_range)
    n = 2500
    while (n < 1000000000):
        if (divisible_by_set(n, facs)):
            return n
        n += 2
    return -1

print(smallest_multiple(20))
