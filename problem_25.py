def num_digits(n):
    digits = []
    while (n):
        digits.append(n % 10)
        n //= 10
    return len(digits)

def fibonacci_index(digitLimit):
	prev = 1
	cur = 1
	index = 2
	while (num_digits(cur) < digitLimit):
		temp = cur
		cur = cur + prev
		prev = temp
		index += 1

	return index

print fibonacci_index(1000)