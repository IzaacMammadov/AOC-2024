from sortedcontainers import SortedList

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

total = 0
for row in input_text:
    output, values = row.split(": ")
    output = int(output)
    values = [int(x) for x in values.split()]
    current_totals = SortedList([values[0]])
    for value in values[1:]:
        new_totals = SortedList()
        for operand in (
            lambda x, y: x + y,
            lambda x, y: x * y,
            lambda x, y: int(str(x) + str(y)),
        ):
            for current_total in current_totals:
                new_total = operand(current_total, value)
                if new_total <= output:
                    new_totals.add(new_total)
                else:
                    break
        current_totals = new_totals
    total += output * int(output in current_totals)
print(total)
