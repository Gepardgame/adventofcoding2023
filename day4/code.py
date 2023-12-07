import regex as re
from aocd import get_data
text = get_data(day, year=2023).split("\n")
numbers1 = [ ( re.findall(r"\b\d+\b(?!:)(?=.+\|)", i), re.findall(r"(?<=\|.+)\b\d+\b", i) ) for i in text ]
sum1 = [ int(2**(len(set(i).intersection(j))-1)) for i, j in numbers1 ]
print(sum(sum1))
t = [ 1 ] * len(text)
numbers2 = [ len(set(i).intersection(j)) for i, j in numbers1 ]
for i, j in enumerate(numbers2):
    for k in range(i+1, i+j+1):
        t[k] += t[i]
print(sum(t))
