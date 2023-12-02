#
# Advent Calender of Code 2024 ©️ Lance Ruiz
#

import regex

string_digit_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def main():
    inputFile = open('input.txt', 'r')

    calibration_sum = 0

    for line in inputFile:
        digits = regex.findall('\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        # print(digits)

        first_digit = digits[0]
        last_digit = digits[-1]

        if first_digit in string_digit_map:
            first_digit = string_digit_map[first_digit]
        else:
            first_digit = int(first_digit)

        if last_digit in string_digit_map:
            last_digit = string_digit_map[last_digit]
        else:
            last_digit = int(last_digit)

        calibration_value = (first_digit * 10) + last_digit

        # print(calibration_value)
        calibration_sum += calibration_value

    print(calibration_sum)
    inputFile.close()

main()

# confirmed expected output: 56324