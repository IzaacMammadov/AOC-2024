with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

a = int(input_text[0].removeprefix("Register A: "))
b = int(input_text[1].removeprefix("Register B: "))
c = int(input_text[2].removeprefix("Register C: "))
program = [int(i) for i in input_text[4].removeprefix("Program: ").split(",")]
program = [(program[2 * i], program[2 * i + 1]) for i in range(len(program) // 2)]
address = 0
output = []
while address < len(program):
    opcode, operand = program[address]
    address += 1
    match operand:
        case 0 | 1 | 2 | 3:
            combo = operand
        case 4:
            combo = a
        case 5:
            combo = b
        case 6:
            combo = c
        case _:
            assert False
    match opcode:
        case 0:
            a //= 2**combo
        case 1:
            b ^= operand
        case 2:
            b = combo % 8
        case 3:
            if a:
                address = operand // 2
        case 4:
            b ^= c
        case 5:
            output.append(str(combo % 8))
        case 6:
            b = a // (2**combo)
        case 7:
            c = a // (2**combo)
print(",".join(output))
