from collections import defaultdict

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

start = (-1, -1)
end = (-1, -1)
walls = set()
for row in range(len(input_text)):
    for col in range(len(input_text[0])):
        match input_text[row][col]:
            case "S":
                start = (row, col)
            case "E":
                end = (row, col)
            case "#":
                walls.add((row, col))

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
no_cheat_move_count = {start: 0}
current_pos = start
move_count = 0
while current_pos != end:
    for row_move, col_move in moves:
        new_pos = (current_pos[0] + row_move, current_pos[1] + col_move)
        if new_pos not in walls and new_pos not in no_cheat_move_count:
            move_count += 1
            current_pos = new_pos
            no_cheat_move_count[current_pos] = move_count
            break
cheats = defaultdict(int)
for (initial_row, initial_col), step in no_cheat_move_count.items():
    for row_move, col_move in moves:
        cheat_pos = (initial_row + 2 * row_move, initial_col + 2 * col_move)
        if no_cheat_move_count.get(cheat_pos, 0) > 2 + step:
            cheats[no_cheat_move_count[cheat_pos] - step - 2] += 1
print(sum(count for saving, count in cheats.items() if saving >= 100))
