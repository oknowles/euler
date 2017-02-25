from sets import Set

def find_divisors(n):
    return [i for i in range(1, (n / 2) + 1) if (n % i == 0)]

def sum_divisors(n):
    return sum(find_divisors(n))

def is_abundant(n):
    return sum_divisors(n) > n

def find_abundant_numbers(n):
    return [i for i in range(n) if is_abundant(i)]

def find_adundant_pair_sums(n):
    abundant_numbers = find_abundant_numbers(n)
    abundant_pair_sums = Set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            if abundant_numbers[i]+abundant_numbers[j] <= n:
                abundant_pair_sums.add(abundant_numbers[i] + abundant_numbers[j])
            else:
                break;
    return abundant_pair_sums

abundant_pair_sums = find_adundant_pair_sums(28123)
print sum([i for i in range(28123) if (i not in abundant_pair_sums)])
