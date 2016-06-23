def is_prime(n):
    if (n in [2, 3]):
        return True

    prime_factors = []
    while (n % 2 == 0 and len(prime_factors) < 3):
        prime_factors.append(2)
        n //= 2

    p = 3
    while (n > 1 and len(prime_factors) < 3):
        if (n % p == 0):
            prime_factors.append(p)
            n //= p
        else:
            p += 2

    return len(prime_factors) > 1

# returns the nth prime assuming n > 1
def nth_prime(n):
    num_primes = 2
    cur_p = 3

    while (num_primes < n):
        cur_p += 2
        while (is_prime(cur_p)):
            cur_p += 2
        num_primes += 1

    return cur_p

print(nth_prime(10001))
