import re
text = open("input.txt", "r").read().split("\n")[:-1]
digits1 = [ re.findall(r"\d", i) for i in text ]
sum1 = [ int(i[0] + i[-1]) for i in digits1 ]
print(sum(sum1))
digits2 = [ re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", i) for i in text ]
numbers = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
sum2 = [ int(numbers.get(i[0], i[0]) + numbers.get(i[-1], i[-1])) for i in digits2 ]
print(sum1[-10:])
