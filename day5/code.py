import regex as re
from itertools import pairwise
text = open("input.txt", "r").read()
splitter = ["seed", "seed-", "soil-", "fertilizer-", "water-", "light-", "temperature-", "humidity-", ""]
splitted = [ list(map(int, re.findall(r"(?<=" + i + r".*:.*)\b\d+\b(?=.*\n" + j[:-1] + r".*)", text, flags=re.S)))  for i, j in pairwise(splitter) ]
splitted[1:] = [ [ (i[j], i[j+1], i[j+2]) for j in range(0, len(i), 3) ] for i in splitted[1:] ]
print(splitted)
