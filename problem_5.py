def divisible_by_range(n, max_range):
    for i in range(1,max_range):
        if ((n % i) != 0):
            return False
    return True

def smallest_multiple(max_range):

    n = 2500
    while (n < 100000000):
        if (divisible_by_range(n, max_range)):
            return n
        n += 2
    return -1

print(smallest_multiple(20))
