with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

states = {}
XOR = []
OR = []
AND = []
for line in input_text:
    if ":" in line:
        wire, value = line.split(": ")
        states[wire] = wire
    elif "XOR" in line:
        wires, output = line.split(" -> ")
        wire1, wire2 = wires.split(" XOR ")
        XOR.append((wire1, wire2, output))
    elif "OR" in line:
        wires, output = line.split(" -> ")
        wire1, wire2 = wires.split(" OR ")
        OR.append((wire1, wire2, output))
    elif "AND" in line:
        wires, output = line.split(" -> ")
        wire1, wire2 = wires.split(" AND ")
        AND.append((wire1, wire2, output))
while not all(f"z{x:02d}" in states for x in range(46)):
    for op_list, op in ((XOR, "__xor__"), (OR, "__or__"), (AND, "__and__")):
        new_list = []
        for wire1, wire2, output in op_list:
            if states.get(wire1) is not None and states.get(wire2) is not None:
                if states[wire1] > states[wire2]:
                    wire1, wire2 = wire2, wire1
                states[output] = f"({states[wire1]}{op}{states[wire2]})"
            else:
                new_list.append((wire1, wire2, output))
        op_list = new_list

expected_states = {}
expected_states["z00"] = "(x00__xor__y00)"
expected_states["c01"] = "(x00__and__y00)"
for i in range(1, 45):
    expected_states[f"z{i:02d}"] = (
        f"({expected_states[f'c{i:02d}']}__xor__(x{i:02d}__xor__y{i:02d}))"
    )
    expected_states[f"c{i+1:02d}"] = (
        f"(({expected_states[f'c{i:02d}']}__and__(x{i:02d}__xor__y{i:02d}))__or__(x{i:02d}__and__y{i:02d}))"
    )
for x in range(46):
    calc = states[f"z{x:02d}"]
    exp_calc = expected_states[f"z{x:02d}"]
    if calc != exp_calc:
        print(f"z{x:02d} = {calc}")
        print(f"zed = {exp_calc}")
