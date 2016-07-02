# Assume grid of size m x n. As the only two directions are D and R each path contains exactly m D and n R movements. The number of possible combinations of m + n unique values (m+n)!. Within the set of all grid paths however there are many paths that are duplicated. For each path, there are n! ways to rearrange the right movements and m! ways to rearrange the down movements. Hence the number of unique paths is (m+n)!/(n!m!)

gridsize = [20,20]

def factorial(n):
    total = 1
    while (n > 1):
        total *= n
        n -= 1
    return total

print(factorial(gridsize[0] + gridsize[1]) / (factorial(gridsize[0]) * factorial(gridsize[1])))
