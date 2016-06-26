def find_primes(n):
    prime_flags = [True] * n

    for p in range(3, int(n**0.5)+1, 2):
        if prime_flags[p]:
            prime_flags[2*p::p] = [False] * ((n-p-1)/p)
    return [2] + [i for i in range(3, n, 2) if prime_flags[i]]

primes = find_primes(10001*50)
print(primes[10001 - 1])
