from itertools import cycle

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

original_guard_pos = (-1, -1)
obstacles = set()
num_rows = len(input_text)
num_cols = len(input_text[0])
for row_idx in range(num_rows):
    for col_idx in range(num_cols):
        match input_text[row_idx][col_idx]:
            case "^":
                original_guard_pos = (row_idx, col_idx)
            case "#":
                obstacles.add((row_idx, col_idx))
movements = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
no_extra_obstacles_explored = []
directions_cycle = cycle(["U", "R", "D", "L"])
guard_pos = original_guard_pos
guard_dir = next(directions_cycle)
while (0 <= guard_pos[0] < num_rows) and (0 <= guard_pos[1] < num_cols):
    no_extra_obstacles_explored.append((guard_pos, guard_dir))
    next_move = (
        guard_pos[0] + movements[guard_dir][0],
        guard_pos[1] + movements[guard_dir][1],
    )
    if next_move in obstacles:
        guard_dir = next(directions_cycle)
    else:
        guard_pos = next_move
valid_obstacles = set()
invalid_obstacles = set()
for idx, (old_position_passed, old_direction) in enumerate(no_extra_obstacles_explored):
    new_obstacle = (
        old_position_passed[0] + movements[old_direction][0],
        old_position_passed[1] + movements[old_direction][1],
    )
    if (
        new_obstacle
        in valid_obstacles | invalid_obstacles | obstacles | {original_guard_pos}
        or (not 0 <= new_obstacle[0] < num_rows)
        or (not 0 <= new_obstacle[0] < num_cols)
    ):
        continue
    explored = set(no_extra_obstacles_explored[:idx])
    guard_pos = old_position_passed
    directions_cycle = cycle(["U", "R", "D", "L"])
    guard_dir = next(directions_cycle)
    while guard_dir != old_direction:
        guard_dir = next(directions_cycle)
    obstacles.add(new_obstacle)
    while (0 <= guard_pos[0] < num_rows) and (0 <= guard_pos[1] < num_cols):
        if (guard_pos, guard_dir) in explored:
            valid_obstacles.add(new_obstacle)
            break
        explored.add((guard_pos, guard_dir))
        next_move = (
            guard_pos[0] + movements[guard_dir][0],
            guard_pos[1] + movements[guard_dir][1],
        )
        if next_move in obstacles:
            guard_dir = next(directions_cycle)
        else:
            guard_pos = next_move
    else:
        invalid_obstacles.add(new_obstacle)
    obstacles.remove(new_obstacle)
print(len(valid_obstacles))
