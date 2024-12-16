from heapq import heapify, heappop, heappush

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

start = (-1, -1)
end = (-1, -1)
walls = set()
movement = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

for row in range(len(input_text)):
    for col in range(len(input_text[0])):
        match input_text[row][col]:
            case "#":
                walls.add((row, col))
            case "S":
                start = (row, col)
            case "E":
                end = (row, col)

explored = {}
min_end_score = float("inf")
discovered = [(0, start, 0, {start})]
heapify(discovered)
best_path_points = set()

while True:
    score, point_to_explore, direction, visited = heappop(discovered)
    if point_to_explore == end:
        if score <= min_end_score:
            min_end_score = score
            best_path_points |= visited
        else:
            break
    elif score <= explored.get((point_to_explore, direction), float("inf")):
        explored[(point_to_explore, direction)] = score
        for new_direction in ((direction + 1) % 4, (direction - 1) % 4):
            if score + 1000 <= explored.get(
                (point_to_explore, new_direction), float("inf")
            ):
                heappush(
                    discovered, (score + 1000, point_to_explore, new_direction, visited)
                )
        move = movement[direction]
        new_point = (point_to_explore[0] + move[0], point_to_explore[1] + move[1])
        if new_point not in walls and score + 1 <= explored.get(
            (new_point, direction), float("inf")
        ):
            heappush(
                discovered,
                (score + 1, new_point, direction, visited | {new_point}),
            )

print(len(best_path_points))
