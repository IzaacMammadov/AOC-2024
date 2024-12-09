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
        for operand in ("__add__", "__mul__"):
            for current_total in current_totals:
                new_total = getattr(current_total, operand)(value)
                if new_total <= output:
                    new_totals.add(new_total)
                else:
                    break
        current_totals = new_totals
    total += output * int(output in current_totals)
print(total)
