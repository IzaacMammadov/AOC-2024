from re import finditer

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

num_rows = len(input_text)
num_cols = len(input_text[0])

ne_sw_diag_mas = set()
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
    for match in finditer(r"MAS", diagonal):
        ne_sw_diag_mas.add(
            (
                max(0, idx_sum - num_cols + 1) + match.start() + 1,
                idx_sum - max(0, idx_sum - num_cols + 1) - match.start() - 1,
            )
        )
    for match in finditer(r"MAS", diagonal[::-1]):
        ne_sw_diag_mas.add(
            (
                min(num_rows, idx_sum + 1) - 2 - match.start(),
                idx_sum - min(num_rows, idx_sum + 1) + 2 + match.start(),
            )
        )

nw_se_diag_mas = set()
# NW/SE Diagonals
for idx_diff in range(-num_cols + 1, num_rows):
    diagonal = "".join(
        [
            input_text[row_idx][row_idx - idx_diff]
            for row_idx in range(max(0, idx_diff), min(num_rows, num_cols + idx_diff))
        ]
    )
    for match in finditer(r"MAS", diagonal):
        nw_se_diag_mas.add(
            (
                max(0, idx_diff) + match.start() + 1,
                max(0, idx_diff) + match.start() + 1 - idx_diff,
            )
        )
    for match in finditer(r"MAS", diagonal[::-1]):
        nw_se_diag_mas.add(
            (
                min(num_rows, num_cols + idx_diff) - 2 - match.start(),
                min(num_rows, num_cols + idx_diff) - 2 - match.start() - idx_diff,
            )
        )
print(len(nw_se_diag_mas & ne_sw_diag_mas))
