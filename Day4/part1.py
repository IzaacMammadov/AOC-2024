from re import findall

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

num_rows = len(input_text)
num_cols = len(input_text[0])
total = 0

# Rows
for row in input_text:
    total += len(findall(r"XMAS", row))
    total += len(findall(r"XMAS", row[::-1]))

# Columns
for col_idx in range(num_cols):
    col = "".join([input_text[row_idx][col_idx] for row_idx in range(num_rows)])
    total += len(findall(r"XMAS", col))
    total += len(findall(r"XMAS", col[::-1]))
# NE/SW Diagonals
for idx_sum in range(num_rows + num_cols - 1):
    diagonal = "".join(
        [
            input_text[row_idx][idx_sum - row_idx]
            for row_idx in range(
                max(0, idx_sum - num_cols + 1), min(num_rows, idx_sum + 1)
            )
        ]
    )
    total += len(findall(r"XMAS", diagonal))
    total += len(findall(r"XMAS", diagonal[::-1]))
# NW/SE Diagonals
for idx_diff in range(-num_cols + 1, num_rows):
    diagonal = "".join(
        [
            input_text[row_idx][row_idx - idx_diff]
            for row_idx in range(max(0, idx_diff), min(num_rows, num_cols + idx_diff))
        ]
    )
    total += len(findall(r"XMAS", diagonal))
    total += len(findall(r"XMAS", diagonal[::-1]))
print(total)
