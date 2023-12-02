#
# Advent Calender of Code 2024 ©️ Lance Ruiz
#

import regex

string_digit_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def main():
    inputFile = open('input.txt', 'r')
    calibration_sum = 0

    for line in inputFile:
        digits = regex.findall(f'\d|{"|".join(string_digit_map)}', line, overlapped=True)

        first_digit, last_digit = digits[0], digits[-1]
        first_digit = string_digit_map[first_digit] if first_digit in string_digit_map else int(first_digit)
        last_digit = string_digit_map[last_digit] if last_digit in string_digit_map else int(last_digit)

        calibration_sum += ((first_digit * 10) + last_digit) # calibration value

    inputFile.close()
    print(calibration_sum)

main()

# my accepted expected output: 56324