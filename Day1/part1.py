with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
list1 = []
list2 = []
for line in input_text:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))
print(sum(abs(x - y) for x, y in zip(sorted(list1), sorted(list2))))
