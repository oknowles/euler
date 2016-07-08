num_map = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eightenn', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

# if going from thousands to hundreds then put comma
# if going from hundreds to tens or units then add 'and'
# i.e for a 4 digit number, and and will only go in the 3 digit number (if applicable)

# digits = 1 2 3 4, written_form = 'one thousand, two hundred and thirty four'
#
# cur_digit = 1, cur_size = 4 => 'one thousand'
# cur_digit = 2, cur_size = 3 => '2 hundred and'
# cur_digit = 3, cur_size = 2 => 'thirty'
# cur_digit = 4, cur_size = 1 => 'four'

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

    num_digits = len(digits)
    for i in range(num_digits):
        cur_digit = digits[i]
        num_zeros = num_digits - (i + 1)

        if (num_zeros == 3):
            written_form += str(num_map[cur_digit]) + ' thousand, '
        elif (num_zeros == 2) and (cur_digit != 0):
                written_form += num_map[cur_digit] + ' hundred '
        elif (num_zeros == 1):
            if (num_digits > 2):
                written_form += 'and '

            tens_num = int(str(cur_digit) + str(digits[i+1]))
            if (tens_num in num_map):
                return written_form + num_map[tens_num] + ' '
            elif (cur_digit != 0):
                written_form += num_map[cur_digit*10] + ' '
        elif (num_zeros == 0) and (cur_digit != 0):
            written_form += num_map[cur_digit]

    if (written_form.endswith(' and ')):
        written_form = written_form.replace(' and ', '')

    return written_form.strip(',')

countable_words = ''
for i in range(1,1001):
    countable_words += get_written_form(i).replace(' ','')

print(len(countable_words))
