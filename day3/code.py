import re
from aocd import get_data
text = get_data(day=3, year=2023)
part_of = list(map(int, re.findall(r"(?<=[+*@/#$\-=&%])\d+|\d+(?=[+*@/#$\-=&%])", text)))
sign = [ [ x.start() for x in  list(re.finditer(r"[+*@/#$\-=&%]", i))] for i in text.split("\n")[:-1] ]
over = sign[1:]+[[-1]]
under = [[-1]] + sign[:-1]
maybe_part_of = [ re.finditer(r"(?<![+*@/#$\-=&%])\b\d+\b(?![+*@/#$\-=&%])", i) for i in text.split("\n")[:-1] ]
#maybe_part_of = (maybe_part_of, sign[1:]+[-1], sign[:-1]+[-1])
part_of += [ sum([ int(x.group()) for x in i if any( x.start()-1 <= y <= x.end() for y in under[j] ) or any( x.start()-1 <= y <= x.end() for y in over[j] ) ]) for j, i in enumerate(maybe_part_of) ]
print(part_of[-10:])
print(sum(part_of))
