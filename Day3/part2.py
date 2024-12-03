from re import findall

with open("input.txt") as input_file:
    input_text = input_file.read()
total = 0
do = True
for res in findall(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))", input_text):
    if do and res[0]:
        total += int(res[0]) * int(res[1])
    elif do and res[2]:
        do = False
    elif (not do) and res[3]:
        do = True
print(total)
