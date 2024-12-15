from copy import deepcopy

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

movement = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
blocking_points = {
    ">": [(0, 2)],
    "<": [(0, -1)],
    "^": [(-1, 0), (-1, 1)],
    "v": [(1, 0), (1, 1)],
}


def push_box(box_location, instruction, input_map):
    potential_blocking_points = [
        (box_location[0] + bp[0], box_location[1] + bp[1])
        for bp in blocking_points[instruction]
    ]
    copy_made = False
    for pbp in potential_blocking_points:
        match input_map.get(pbp):
            case "#":
                raise ValueError
            case "[":
                copy_made = True
                input_map = push_box(pbp, instruction, input_map)
            case "]":
                copy_made = True
                input_map = push_box((pbp[0], pbp[1] - 1), instruction, input_map)
    if not copy_made:
        input_map = deepcopy(input_map)
    del input_map[box_location]
    del input_map[(box_location[0], box_location[1] + 1)]
    move = movement[instruction]
    input_map[(box_location[0] + move[0], box_location[1] + move[1])] = "["
    input_map[(box_location[0] + move[0], box_location[1] + move[1] + 1)] = "]"
    return input_map


current_pos = (-1, -1)
map = {}
instructions = False
for row in range(len(input_text)):
    if input_text[row] and not instructions:
        for col in range(len(input_text[0])):
            match input_text[row][col]:
                case "O":
                    map[(row, 2 * col)] = "["
                    map[(row, 2 * col + 1)] = "]"
                case "#":
                    map[(row, 2 * col)] = "#"
                    map[(row, 2 * col + 1)] = "#"
                case "@":
                    current_pos = (row, 2 * col)
    elif not input_text[row]:
        instructions = True
    else:
        for instruction in input_text[row]:
            move = movement[instruction]
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            match map.get(new_pos):
                case None:
                    current_pos = new_pos
                case "[" | "]":
                    try:
                        map = push_box(
                            (
                                new_pos[0],
                                new_pos[1] - (1 if map[new_pos] == "]" else 0),
                            ),
                            instruction,
                            map,
                        )
                    except ValueError:
                        continue
                    current_pos = new_pos

print(sum(row * 100 + col for (row, col), item in map.items() if item == "["))
