import re
#example = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
#example2 = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

def find_calibrations(filename):
    calibration_sum = 0
    input = open(filename, "r")
    lines = input.readlines()

    for line in lines:
        first_digit = re.search("\d|one|two|three|four|five|six|seven|eight|nine|zero", line)[0]
        last_digit = re.search("\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|orez", line[::-1])[0]
        if not first_digit.isnumeric():
            first_digit = text_to_digit(first_digit)
        if not last_digit.isnumeric():
            last_digit = text_to_digit_rev(last_digit)
        print(first_digit + last_digit)
        calibration_sum += int(first_digit + last_digit)
    
    input.close()
    
    return calibration_sum

def text_to_digit(text):
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return str(digits.index(text))

def text_to_digit_rev(text):
    digits = ["orez", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
    return str(digits.index(text))

print(find_calibrations("input.txt"))
    
 