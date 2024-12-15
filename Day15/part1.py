with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

current_pos = (-1, -1)
map = {}
movement = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
instructions = False
for row in range(len(input_text)):
    if input_text[row] and not instructions:
        for col in range(len(input_text[0])):
            match input_text[row][col]:
                case "O":
                    map[(row, col)] = "O"
                case "#":
                    map[(row, col)] = "#"
                case "@":
                    current_pos = (row, col)
    elif not input_text[row]:
        instructions = True
    else:
        for instruction in input_text[row]:
            move = movement[instruction]
            boxes_pushed = 0
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            while True:
                end_box_pos = (
                    current_pos[0] + (1 + boxes_pushed) * move[0],
                    current_pos[1] + (1 + boxes_pushed) * move[1],
                )
                match map.get(end_box_pos):
                    case "O":
                        boxes_pushed += 1
                    case "#":
                        break
                    case None:
                        if boxes_pushed > 0:
                            map[end_box_pos] = "O"
                            del map[new_pos]
                        current_pos = new_pos
                        break
print(sum(row * 100 + col for (row, col), item in map.items() if item == "O"))
