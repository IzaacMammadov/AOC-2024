from collections import defaultdict
from itertools import combinations

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
        for antinode in (
            (2 * location1[0] - location2[0], 2 * location1[1] - location2[1]),
            (2 * location2[0] - location1[0], 2 * location2[1] - location1[1]),
        ):
            if 0 <= antinode[0] < num_rows and 0 <= antinode[1] < num_cols:
                antinodes.add(antinode)
print(len(antinodes))
