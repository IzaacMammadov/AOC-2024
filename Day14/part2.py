from collections import defaultdict
from statistics import stdev

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

num_x = 101
num_y = 103
initial_positions = []
velocities = []
for line in input_text:
    p_sec, v_sec = line.split()
    initial_positions.append([int(i) for i in p_sec.split("=")[1].split(",")])
    velocities.append([int(i) for i in v_sec.split("=")[1].split(",")])

for counter in range(10000):
    block_counts = defaultdict(int)
    new_initial_positions = []
    for initial_pos, velocity in zip(initial_positions, velocities):
        new_position = [
            (initial_pos[0] + velocity[0]) % num_x,
            (initial_pos[1] + velocity[1]) % num_y,
        ]
        new_initial_positions.append(new_position)
        block_counts[(new_position[0] // 5, new_position[1] // 5)] += 1
    if stdev(block_counts.values()) > 3:
        print(counter + 1)
    initial_positions = new_initial_positions
