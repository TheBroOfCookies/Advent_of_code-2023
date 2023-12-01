import re
#example = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def find_calibrations(filename):
	calibration_sum = 0
	input = open(filename, "r")
	lines = input.readlines()

	for line in lines:
		first_digit = re.search("\d", line)[0]
		last_digit = re.search("\d", line[::-1])[0]
		calibration_sum += int(first_digit + last_digit)
	
	input.close()
	
	return calibration_sum

print(find_calibrations("input.txt"))
	
 