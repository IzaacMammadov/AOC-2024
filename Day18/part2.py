from heapq import heapify, heappop, heappush

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

grid_size = 70
bytes_list = []
for byte in input_text:
    byte_x, byte_y = byte.split(",")
    bytes_list.append((int(byte_x), int(byte_y)))

movements = ((-1, 0), (1, 0), (0, 1), (0, -1))

bytes_needed_lower = 0
bytes_needed_upper = len(bytes_list) - 1
while bytes_needed_lower < bytes_needed_upper:
    mid = (bytes_needed_lower + bytes_needed_upper) // 2
    bytes = set(bytes_list[:mid])
    explored = set()
    discovered = [(0, 0, 0)]
    heapify(discovered)
    while discovered:
        distance, byte_x, byte_y = heappop(discovered)
        if (byte_x, byte_y) not in explored:
            explored.add((byte_x, byte_y))
            if byte_x == byte_y == grid_size:
                break
            for movement in movements:
                new_position = (byte_x + movement[0], byte_y + movement[1])
                if (
                    new_position not in bytes
                    and new_position not in explored
                    and all(0 <= coord <= grid_size for coord in new_position)
                ):
                    heappush(discovered, (distance + 1, *new_position))
    else:
        bytes_needed_upper = mid
        continue
    bytes_needed_lower = mid + 1

print(",".join([str(x) for x in bytes_list[bytes_needed_lower - 1]]))
