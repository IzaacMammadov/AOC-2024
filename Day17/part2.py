with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

program = [int(x) for x in input_text[4].removeprefix("Program: ").split(",")]
a = 0
position = 0
offsets = [0]

while position < len(program):
    if program[-1 - position] == ((a % 8) ^ 5 ^ 6 ^ (a // (2 ** ((a % 8) ^ 5)))) % 8:
        a *= 8
        position += 1
        offsets.append(0)
    elif offsets[-1] < 7:
        a += 1
        offsets[-1] += 1
    else:
        while offsets[-1] >= 7 and position > 0:
            a //= 8
            offsets.pop(-1)
            position -= 1
        a += 1
        offsets[-1] += 1


print(a // 8)
