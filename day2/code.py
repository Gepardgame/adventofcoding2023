import re
text = open("input.txt", "r").read().split("\n")[:-1]
blue = 14
red = 12
green = 13
cubes = [{"id": int(re.findall(r"(?<=^Game\s)\d+", i)[0]), "blue": [int(x) for x in re.findall(r"\d+(?=\sblue)", i)], "red": [int(x) for x in re.findall(r"\d+(?=\sred)", i)], "green":  [int(x) for x in re.findall(r"\d+(?=\sgreen)", i)]}   for i in text ]
sum1 = [ i["id"] for i in cubes if max(i["blue"]) <= blue and max(i["red"]) <= red and max(i["green"]) <= green ]
print(sum(sum1))

sum2 = [ max(i["blue"]) * max(i["red"]) * max(i["green"]) for i in cubes ]
print(sum(sum2))
