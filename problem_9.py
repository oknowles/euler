def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2

def find_triples(n):
    for a in range(1, n//3):
        for b in range(a+1, n//2):
            c = n - (a + b)
            if (is_pythagorean_triple(a,b,c)):
                return a*b*c

print(find_triples(1000))
