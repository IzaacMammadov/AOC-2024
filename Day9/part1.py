with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

file_structure = [
    (i // 2 if not i % 2 else -1, int(x)) for i, x in enumerate(input_text[0])
]  # File ID -1 means free space
buffer = None
total = 0
current_index = 0

while file_structure:
    file_id, length = file_structure.pop(0)
    if file_id == -1:
        while length:
            if not buffer:
                while file_structure and file_structure[-1][0] == -1:
                    file_structure.pop(-1)
                if file_structure:
                    buffer = file_structure.pop(-1)
                else:
                    break
            if length >= buffer[1]:
                total += int(
                    buffer[0] * buffer[1] * (current_index + (buffer[1] - 1) / 2)
                )
                current_index += buffer[1]
                length -= buffer[1]
                buffer = None
            else:
                total += int(buffer[0] * length * (current_index + (length - 1) / 2))
                current_index += length
                buffer = (buffer[0], buffer[1] - length)
                length = 0
    else:
        total += int(file_id * length * (current_index + (length - 1) / 2))
        current_index += length
if buffer:
    total += int(buffer[0] * buffer[1] * (current_index + (buffer[1] - 1) / 2))
print(total)
