from itertools import cycle

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

guard_pos = (-1, -1)
obstacles = set()
explored = set()
num_rows = len(input_text)
num_cols = len(input_text[0])
for row_idx in range(num_rows):
    for col_idx in range(num_cols):
        match input_text[row_idx][col_idx]:
            case "^":
                guard_pos = (row_idx, col_idx)
            case "#":
                obstacles.add((row_idx, col_idx))
directions_cycle = cycle(["U", "R", "D", "L"])
guard_dir = next(directions_cycle)
movements = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
while (0 <= guard_pos[0] < num_rows) and (0 <= guard_pos[1] < num_cols):
    explored.add(guard_pos)
    next_move = (
        guard_pos[0] + movements[guard_dir][0],
        guard_pos[1] + movements[guard_dir][1],
    )
    if next_move in obstacles:
        guard_dir = next(directions_cycle)
    else:
        guard_pos = next_move
print(len(explored))
