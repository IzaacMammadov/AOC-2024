from re import findall

with open("input.txt") as input_file:
    input_text = input_file.read()
total = 0
for res in findall(r"mul\((\d+),(\d+)\)", input_text):
    total += int(res[0]) * int(res[1])
print(total)
