from math import prod

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

num_x = 101
num_y = 103
quadrant_count = [0, 0, 0, 0]
for line in input_text:
    p_sec, v_sec = line.split()
    initial_pos = [int(i) for i in p_sec.split("=")[1].split(",")]
    velocity = [int(i) for i in v_sec.split("=")[1].split(",")]
    final_x, final_y = (
        (initial_pos[0] + 100 * velocity[0]) % num_x,
        (initial_pos[1] + 100 * velocity[1]) % num_y,
    )
    if final_x < (num_x - 1) / 2 and final_y < (num_y - 1) / 2:
        quadrant_count[0] += 1
    elif final_x < (num_x - 1) / 2 and final_y > (num_y - 1) / 2:
        quadrant_count[1] += 1
    elif final_x > (num_x - 1) / 2 and final_y < (num_y - 1) / 2:
        quadrant_count[2] += 1
    elif final_x > (num_x - 1) / 2 and final_y > (num_y - 1) / 2:
        quadrant_count[3] += 1
print(prod(quadrant_count))
