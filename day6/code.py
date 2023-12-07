import regex as re
from aocd import get_data
text = get_data(day=6, year=2023)
times = [ (int(i), int(j)) for i, j in zip(re.findall(r"(?<=Time:.*)\b\d+\b", text), re.findall(r"(?<=Distance:.*)\b\d+\b", text)) ]
sum1 = [ int((-i-(i**2-4*j)**0.5)/(-2))-int((-i+(i**2-4*j)**0.5)/(-2))  for i, j in times ]
print(sum1)

times1 = (re.findall(r"(?<=Time:.*)\b\d+\b", text), re.findall(r"(?<=Distance:.*)\b\d+\b", text))
t = (int("".join(times1[0])), int("".join(times1[1])))
sum2 = int((-t[0]-(t[0]**2-4*t[1])**0.5)/(-2))-int((-t[0]+(t[0]**2-4*t[1])**0.5)/(-2))
print(sum2)
