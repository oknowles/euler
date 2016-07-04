num_map = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eightenn', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

def digit_list(n):
    digits = []
    while (n):
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    return digits

def get_written_form(n):
    if (n in num_map):
        return num_map[n]

    written_form = ''
    digits = digit_list(n)
    total_size = len(digits)
    for i in range(total_size):
        num_zeros = total_size - i
        if num_zeros = 3:
            written_form += str(digits[i]) + 'thousand'

word_count = 0
for i in range(1,10001):
    word_count += get_written_form(i)
