import math

num_dict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    "g": 16,
    "h": 17,
    "i": 18,
    "j": 19,
    "k": 20,
    "l": 21,
    "m": 22,
    "n": 23,
    "o": 24,
    "p": 25,
    "q": 26,
    "r": 27,
    "s": 28,
    "t": 29,
    "u": 30,
    "v": 31,
    "w": 32,
    "x": 33,
    "y": 34,
    "z": 35
}

# change the number from the given base to base 10
def standardize_num(orig_num, start_base):
    if start_base == 10:
        return orig_num

    standard_num = 0
    curr_index = 0
    curr_exponent = len(orig_num) - 1

    # add the decimal value of each digit of the original number to the standard number
    while curr_exponent >= 0:
        standard_num += math.pow(start_base, curr_exponent) * num_dict[orig_num[curr_index]]

        curr_index += 1
        curr_exponent -= 1

    return standard_num

# change the number from base 10 to the desired end base
def change_to_base(num, end_base):
    if end_base == 10:
        return str(num)

    curr_exponent = 0
    converted_num = ''
    curr_digit = 0

    # determine the greatest exponent needed
    while num >= math.pow(end_base, curr_exponent + 1):
        curr_exponent += 1

    # for each exponent, starting with the greatest one required,
    # subtract multiples of the end base raised to the exponent without going negative
    while curr_exponent >= 0:
        while num - math.pow(end_base, curr_exponent) * curr_digit >= math.pow(end_base, curr_exponent):
            curr_digit += 1

        # after the correct multiple has been determined,
        # subtract the product from the starting number
        num -= math.pow(end_base, curr_exponent) * curr_digit

        # find the letter or number that corresponds to the multiple and
        # append it to the converted number
        for key in num_dict:
            if num_dict[key] == curr_digit:
                converted_num += key

        curr_digit = 0
        curr_exponent -= 1

    return converted_num

# convert a given number between the two provided bases
def convert_num(orig_num, start_base, end_base):
    # check for valid bases
    if start_base < 2 or start_base > 36:
        raise Exception("Please choose a start base between 2 and 36")
    if end_base < 2 or end_base > 36:
        raise Exception("Please choose an end base between 2 and 36")

    # note if the number is negative and remove the sign to simplify converison
    is_negative = False
    if orig_num[0] == '-':
        is_negative = True
        orig_num = orig_num[1:]

    # make sure the number is valid
    for digit in orig_num:
        try:
            num_dict[digit]
        except:
            raise Exception("'" + digit + "' is an invalid character.")

        if num_dict[digit] >= start_base:
            raise Exception("'" + digit + "' is an invalid digit for the base '" + str(start_base) + "'. Please enter a valid number.")

    # change number to base 10
    standard_num = standardize_num(orig_num, start_base)

    # convert number from base 10 to the desired base
    if is_negative:
        return '-' + change_to_base(int(standard_num), end_base)
    else:
        return change_to_base(int(standard_num), end_base)

print(convert_num("5555", 6, 4))
