from functools import cache

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()


@cache
def num_keypad_paths(start, end):
    output = []
    x_diff = abs(end[0] - start[0])
    y_diff = abs(end[1] - start[1])
    horiz_char = ">" if end[0] > start[0] else "<"
    vert_char = "v" if end[1] > start[1] else "^"
    for path in {
        tuple([horiz_char] * x_diff + [vert_char] * y_diff),
        tuple([vert_char] * y_diff + [horiz_char] * x_diff),
    }:
        if not (
            (start == (0, 0) and path[:3] == ("v", "v", "v"))
            or (start == (0, 1) and path[:2] == ("v", "v"))
            or (start == (0, 2) and path[:1] == ("v",))
            or (start == (1, 3) and path[:1] == ("<",))
            or (start == (2, 3) and path[:2] == ("<", "<"))
        ):
            output.append(list(path) + ["A"])
    return output


@cache
def dir_keypad_paths(start, end):
    output = []
    x_diff = abs(end[0] - start[0])
    y_diff = abs(end[1] - start[1])
    horiz_char = ">" if end[0] > start[0] else "<"
    vert_char = "v" if end[1] > start[1] else "^"
    for path in {
        tuple([horiz_char] * x_diff + [vert_char] * y_diff),
        tuple([vert_char] * y_diff + [horiz_char] * x_diff),
    }:
        if not (
            (start == (1, 0) and path[:1] == ("<",))
            or (start == (2, 0) and path[:2] == ("<", "<"))
            or (start == (0, 1) and path[:1] == ("^",))
        ):
            output.append(list(path) + ["A"])
    return output


num_keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}
directional_keypad = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}

total = 0
for code in input_text:
    current_pos = (2, 3)
    solutions = [[]]
    for character in code:
        new_pos = num_keypad[character]
        solutions = [
            solution + path
            for solution in solutions
            for path in num_keypad_paths(current_pos, new_pos)
        ]
        current_pos = new_pos
    solutions_2_outer = []
    for solution in solutions:
        current_pos = (2, 0)
        solutions_2 = [[]]
        for character in solution:
            new_pos = directional_keypad[character]
            solutions_2 = [
                partial_solution + path
                for partial_solution in solutions_2
                for path in dir_keypad_paths(current_pos, new_pos)
            ]
            current_pos = new_pos
        solutions_2_outer += solutions_2
    solutions_3_outer = []
    for solution in solutions_2_outer:
        current_pos = (2, 0)
        solutions_3 = [[]]
        for character in solution:
            new_pos = directional_keypad[character]
            solutions_3 = [
                partial_solution + path
                for partial_solution in solutions_3
                for path in dir_keypad_paths(current_pos, new_pos)
            ]
            current_pos = new_pos
        solutions_3_outer += solutions_3
    total += min(len(x) for x in solutions_3_outer) * int(code[:3])
print(total)
