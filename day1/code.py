import re
from aocd import get_data
text = get_data(day=1, year=2023).split("\n")
digits1 = [ re.findall(r"\d", i) for i in text ]
sum1 = [ int(i[0] + i[-1]) for i in digits1 ]
print(sum(sum1))
"""text = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]"""
digits2 = [ re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", i) for i in text ]
numbers = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
#sum2 = [ int(numbers.get(i[0], i[0]) + numbers.get(i[-1], i[-1])) for i in digits2 ]
sum2 = []
for i in digits2:
    #print(i)
    first_digit = numbers.get(i[0], i[0])
    last_digit = numbers.get(i[-1], i[-1])
    current_sum = int(first_digit + last_digit)
    #print("f: ", first_digit, "l: ", last_digit, "s: ", current_sum)
    sum2.append(current_sum)
print(sum2[-10:])
print(sum(sum2))

