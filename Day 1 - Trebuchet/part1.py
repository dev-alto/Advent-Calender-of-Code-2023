#
# Advent Calender of Code 2024 ©️ Lance Ruiz
#

import re as regex

def main():
    inputFile = open('input.txt', 'r')

    calibration_sum = 0

    for line in inputFile:
        digits = regex.findall('\d', line)
        # print(digits)

        first_digit = int(digits[0])
        last_digit = int(digits[-1])

        calibration_value = (first_digit * 10) + last_digit

        # print(calibration_value)
        calibration_sum += calibration_value

    print(calibration_sum)
    inputFile.close()

main()

# confirmed expected output: 55108