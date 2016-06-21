cur_term = total = t_1 = 0
t_2 = 1

while (cur_term <= 4000000):
    cur_term = t_1 + t_2
    if (cur_term % 2 == 0):
        total += cur_term
    t_1 = t_2
    t_2 = cur_term

print(total)
