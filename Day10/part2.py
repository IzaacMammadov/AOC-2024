from collections import defaultdict

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

num_rows = len(input_text)
num_cols = len(input_text[0])
topography = {}

for row in range(num_rows):
    for col in range(num_cols):
        topography[(row, col)] = int(input_text[row][col])

movements = ((1, 0), (-1, 0), (0, 1), (0, -1))
paths_from = {point: 1 for point, height in topography.items() if height == 9}
for height in range(8, -1, -1):
    new_paths_from = defaultdict(int)
    for point, value in paths_from.items():
        for movement in movements:
            potential_new_point = (
                point[0] + movement[0],
                point[1] + movement[1],
            )
            if topography.get(potential_new_point) == height:
                new_paths_from[potential_new_point] += value
    paths_from = new_paths_from

print(sum(paths_from.values()))
