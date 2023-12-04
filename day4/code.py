import regex as re
text = open("input.txt", "r").read().split("\n")
numbers1 = [ ( re.findall(r"(?<=Card\s+)\d+(?=:)", i),  re.findall(r"\b\d+\b(?!:)(?=.+\|)", i), re.findall(r"(?<=\|.+)\b\d+\b", i) ) for i in text ]
sum1 = [ int(2**(len(set(i).intersection(j))-1)) for _, i, j in numbers1 ]
print(sum(sum1))

numbers2 = [ (k, len(set(i).intersection(j))) for k, i, j in numbers1 ]
for i, j in numbers2:
    


#x = [ [ for k in range(i, i+j ] for i, j in numbers2 ]
