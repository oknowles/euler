def is_palindrome(n):
    digits = []
    while (n > 0):
        digits.append(n % 10)
        n //= 10

    tail = 0
    head = len(digits) - 1
    while (tail <= head):
        if digits[tail] != digits[head]:
            return False
        tail += 1
        head -= 1
    return True

def find_largest_palindrome():
    palindromes = []
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            n = i * j
            if is_palindrome(n):
                palindromes.append(n)
    return max(palindromes)

print(find_largest_palindrome())
