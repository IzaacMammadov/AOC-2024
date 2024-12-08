with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

guard_pos = (-1, -1)
guard_dir = None
obstacles = set()
explored = set()
num_rows = len(input_text)
num_cols = len(input_text[0])
for row_idx in range(num_rows):
    for col_idx in range(num_cols):
        match input_text[row_idx][col_idx]:
            case "^":
                guard_pos = (row_idx, col_idx)
                guard_dir = "U"
                explored.add(guard_pos)
            case "#":
                obstacles.add((row_idx, col_idx))

while (0 <= guard_pos[0] < num_rows) and (0 <= guard_pos[1] < num_cols):
    match guard_dir:
        case "U":
            if (guard_pos[0] - 1, guard_pos[1]) in obstacles:
                guard_dir = "R"
            else:
                guard_pos = (guard_pos[0] - 1, guard_pos[1])
        case "R":
            if (guard_pos[0], guard_pos[1] + 1) in obstacles:
                guard_dir = "D"
            else:
                guard_pos = (guard_pos[0], guard_pos[1] + 1)
        case "D":
            if (guard_pos[0] + 1, guard_pos[1]) in obstacles:
                guard_dir = "L"
            else:
                guard_pos = (guard_pos[0] + 1, guard_pos[1])
        case "L":
            if (guard_pos[0], guard_pos[1] - 1) in obstacles:
                guard_dir = "U"
            else:
                guard_pos = (guard_pos[0], guard_pos[1] - 1)
    explored.add(guard_pos)
print(len(explored))
