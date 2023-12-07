import regex as re
from itertools import pairwise
from aocd import get_data
text = get_data(day, year=2023)
splitter = ["seed", "seed-", "soil-", "fertilizer-", "water-", "light-", "temperature-", "humidity-", ""]
splitted = [ list(map(int, re.findall(r"(?<=" + i + r".*:.*)\b\d+\b(?=.*\n" + j[:-1] + r".*)", text, flags=re.S)))  for i, j in pairwise(splitter) ]
splitted[1:] = [ [ (i[j], i[j+1], i[j+2]) for j in range(0, len(i), 3) ] for i in splitted[1:] ]
sum1 = []
for i in splitted[0]:
    for x in splitted[1:]:
        for j, k, l in x:
            if not (k <= i <= k + l): continue
            i = j+(i-k)
            break
    sum1.append(i)
print(min(sum1))
seeds = [ (splitted[0][i], splitted[0][i+1])  for i in range(0, len(splitted[0]), 2) ]
sum2 = []
for i, j in seeds:
    for y in range(i, i+j):
        for x in splitted[1:]:
            for j, k, l in x:
                if not (k <= i <= k + l): continue
                i = j+(i-k)
                break
        sum2.append(i)
print(min(sum2))
