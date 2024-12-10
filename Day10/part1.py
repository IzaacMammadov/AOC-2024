with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

num_rows = len(input_text)
num_cols = len(input_text[0])
topography = {}

for row in range(num_rows):
    for col in range(num_cols):
        topography[(row, col)] = int(input_text[row][col])

movements = ((1, 0), (-1, 0), (0, 1), (0, -1))
nine_reachable_from = {
    point: {point} for point, height in topography.items() if height == 9
}
for height in range(8, -1, -1):
    new_nine_reachable_from = {}
    for nine_point, old_reachable_froms in nine_reachable_from.items():
        new_reachable_froms = set()
        for old_point in old_reachable_froms:
            for movement in movements:
                potential_new_point = (
                    old_point[0] + movement[0],
                    old_point[1] + movement[1],
                )
                if topography.get(potential_new_point) == height:
                    new_reachable_froms.add(potential_new_point)
        if new_reachable_froms:
            new_nine_reachable_from[nine_point] = new_reachable_froms
    nine_reachable_from = new_nine_reachable_from

print(sum(len(starting_points) for starting_points in nine_reachable_from.values()))
