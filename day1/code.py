import re
text = open("input.txt", "r").read().split("\n")
#digits1 = [ re.findall(r"\d", i) for i in text ]
#sum1 = [ int(i[0] + i[-1]) for i in digits1 ]
#print(sum(sum1))

digits2 = [ re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", i) for i in text ]
numbers = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
sum2 = [ int(numbers.get(i[0], i[0]) + numbers.get(i[-1], i[-1])) for i in digits2 ]
print(sum2[-10:])
print(sum(sum2))

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def convert_to_digit(match):
    return numbers.get(match.group(0), match.group(0))

to_numbers = [re.sub(r"\d|one|two|three|four|five|six|seven|eight|nine", convert_to_digit, i) for i in text]
digits2 = [ re.findall(r"\d", i) for i in to_numbers ]
calibration_values = [int(line[0] + line[-1]) for line in digits2]
print(sum(calibration_values))
