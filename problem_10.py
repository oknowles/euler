def is_prime(n):
    if (n in [2, 3]):
        return True

    prime_factors = []
    while (n % 2 == 0 and len(prime_factors) < 3):
        if (len(prime_factors) == 1):
            return False
        prime_factors.append(2)
        n //= 2

    p = 3
    while (n > 1 and len(prime_factors) < 3):
        if (n % p == 0):
            if (len(prime_factors) == 1):
                return False
            prime_factors.append(p)
            n //= p
        else:
            p += 2

    return len(prime_factors) == 1

def sum_primes(upper_limit):
    if upper_limit == 2:
        return 2
    total = 5
    for p in range(5, upper_limit, 2):
        if is_prime(p):
            total += p
    return total


print(sum_primes(2000000))
