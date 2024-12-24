with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

states = {}
z_wires = []
XOR = []
OR = []
AND = []
for line in input_text:
    if ":" in line:
        wire, value = line.split(": ")
        states[wire] = bool(int(value))
    elif "XOR" in line:
        wires, output = line.split(" -> ")
        wire1, wire2 = wires.split(" XOR ")
        XOR.append((wire1, wire2, output))
        if output[0] == "z":
            z_wires.append(output)
    elif "OR" in line:
        wires, output = line.split(" -> ")
        wire1, wire2 = wires.split(" OR ")
        OR.append((wire1, wire2, output))
        if output[0] == "z":
            z_wires.append(output)
    elif "AND" in line:
        wires, output = line.split(" -> ")
        wire1, wire2 = wires.split(" AND ")
        AND.append((wire1, wire2, output))
        if output[0] == "z":
            z_wires.append(output)
while not all(z in states for z in z_wires):
    for op_list, op in ((XOR, "__xor__"), (OR, "__or__"), (AND, "__and__")):
        new_list = []
        for wire1, wire2, output in op_list:
            if states.get(wire1) is not None and states.get(wire2) is not None:
                states[output] = getattr(states[wire1], op)(states[wire2])
            else:
                new_list.append((wire1, wire2, output))
        op_list = new_list
place = 0
total = 0
while f"z{place:02d}" in states:
    total += int(states[f"z{place:02d}"]) << place
    place += 1
print(total)
