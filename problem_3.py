# we know any number can be written as a product of primes so we can loop through all primes, starting with 2 and append each factor

def prime_factors(n):
    prime_factors = []

    while (n % 2 == 0):
        prime_factors.append(2)
        n //= 2

    p = 3
    while (n > 1):
        if (n % p == 0):
            prime_factors.append(p)
            n //= p
        else:
            p += 2

    return prime_factors

print(max(prime_factors(600851475143)))
