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

def num_factors(n):
    p_factors = prime_factors(n)
    prev_p = p_factors[0]
    count = 0
    total_factors = 1
    for p in p_factors:
        if p == prev_p:
            count += 1
        else:
            total_factors *= (count+1)
            prev_p = p
            count = 1

    return total_factors*(count+1)

t = 5000
t_num = sum(range(t+1))
while (num_factors(t_num) < 500):
    print(t)
    t += 1
    t_num += t

print('result: triangle number [' + str(t_num) + '] with [' + str(num_factors(t_num)) + '] factors')
