from heapq import heapify, heappop, heappush

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

grid_size = 70
num_fallen = 1024
bytes = set()
for byte in input_text[:num_fallen]:
    byte_x, byte_y = byte.split(",")
    bytes.add((int(byte_x), int(byte_y)))

movements = ((-1, 0), (1, 0), (0, 1), (0, -1))
explored = set()
discovered = [(0, 0, 0)]
heapify(discovered)
while True:
    distance, byte_x, byte_y = heappop(discovered)
    if (byte_x, byte_y) not in explored:
        explored.add((byte_x, byte_y))
        if byte_x == byte_y == grid_size:
            print(distance)
            break
        for movement in movements:
            new_position = (byte_x + movement[0], byte_y + movement[1])
            if (
                new_position not in bytes
                and new_position not in explored
                and all(0 <= coord <= grid_size for coord in new_position)
            ):
                heappush(discovered, (distance + 1, *new_position))
