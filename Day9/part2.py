with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

file_structure = [
    (i // 2 if not i % 2 else -1, int(x)) for i, x in enumerate(input_text[0])
]
current_index = len(file_structure) - (1 if file_structure[-1][0] != -1 else 2)
while current_index > 0:
    for idx, (space_id, space_length) in enumerate(file_structure[:current_index]):
        if space_id == -1 and space_length >= file_structure[current_index][1]:
            file_structure = (
                file_structure[:idx]
                + [
                    (-1, 0),
                    file_structure[current_index],
                    (-1, space_length - file_structure[current_index][1]),
                ]
                + file_structure[idx + 1 :]
            )
            if current_index + 2 < len(file_structure) - 1:
                file_structure[current_index + 1] = (
                    -1,
                    file_structure[current_index + 1][1]
                    + file_structure.pop(current_index + 3)[1]
                    + file_structure.pop(current_index + 2)[1],
                )
            else:
                file_structure[current_index + 1] = (
                    -1,
                    file_structure[current_index + 1][1]
                    + file_structure.pop(current_index + 2)[1],
                )
            break
    else:
        current_index -= 2
total = 0
idx = 0
for file_id, file_length in file_structure:
    if file_id != -1:
        total += int(file_id * file_length * (idx + (file_length - 1) / 2))
    idx += file_length
print(total)
