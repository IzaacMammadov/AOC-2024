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

explored = set()
discovered = [(0, start, 0)]
heapify(discovered)

while True:
    score, point_to_explore, direction = heappop(discovered)
    if point_to_explore == end:
        print(score)
        break
    if (point_to_explore, direction) not in explored:
        explored.add((point_to_explore, direction))
        for new_direction in ((direction + 1) % 4, (direction - 1) % 4):
            if (point_to_explore, new_direction) not in explored:
                heappush(discovered, (score + 1000, point_to_explore, new_direction))
        move = movement[direction]
        new_point = (point_to_explore[0] + move[0], point_to_explore[1] + move[1])
        if new_point not in walls and (new_point, direction) not in explored:
            heappush(discovered, (score + 1, new_point, direction))
