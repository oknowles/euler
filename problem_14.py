def next_collatz_num(n):
    return (n/2) if (n%2 == 0) else (3*n + 1)

def collatz_sequence(start_num):
    sequence = [start_num]
    cur_n = start_num
    while (cur_n > 1):
        cur_n = next_collatz_num(cur_n)
        sequence.append(cur_n)
    return sequence

def find_longest_chain(upper_limit):
    chain_lengths = []
    for i in range(1, upper_limit):
        if (i % 100000 == 0):
            print(i)
        chain_lengths.append(len(collatz_sequence(i)))
    return chain_lengths.index(max(chain_lengths)) + 1

print(find_longest_chain(1000000))
