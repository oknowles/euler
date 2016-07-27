from math import factorial

def digit_list(n):
    digits = []
    while (n):
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    return digits

print sum(digit_list(factorial(100)))
