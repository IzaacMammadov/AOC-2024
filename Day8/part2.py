from collections import defaultdict
from itertools import combinations
from math import gcd

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

total = 0
num_rows = len(input_text)
num_cols = len(input_text[0])
antennas = defaultdict(list)
for row in range(num_rows):
    for col in range(num_cols):
        if (char := input_text[row][col]) != ".":
            antennas[char].append((row, col))
antinodes = set()
for locations in antennas.values():
    for location1, location2 in combinations(locations, 2):
        antenna_displacement = [
            location2[0] - location1[0],
            location2[1] - location1[1],
        ]
        antinode_displacement = [
            x // gcd(*antenna_displacement) for x in antenna_displacement
        ]
        current_multiple = 0
        while True:
            new_antinode = (
                location2[0] + antinode_displacement[0] * current_multiple,
                location2[1] + antinode_displacement[1] * current_multiple,
            )
            if 0 <= new_antinode[0] < num_rows and 0 <= new_antinode[1] < num_cols:
                antinodes.add(new_antinode)
                current_multiple += 1
            else:
                break
        current_multiple = -1
        while True:
            new_antinode = (
                location2[0] + antinode_displacement[0] * current_multiple,
                location2[1] + antinode_displacement[1] * current_multiple,
            )
            if 0 <= new_antinode[0] < num_rows and 0 <= new_antinode[1] < num_cols:
                antinodes.add(new_antinode)
                current_multiple -= 1
            else:
                break
print(len(antinodes))
