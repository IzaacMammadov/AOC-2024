with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

plot = {
    (row, col): input_text[row][col]
    for row in range(len(input_text))
    for col in range(len(input_text[0]))
}
plots_remaining_to_consider = set(plot)
movements = [
    (0, 1, "v", 0, 1),
    (0, -1, "v", 0, 0),
    (1, 0, "h", 1, 0),
    (-1, 0, "h", 0, 0),
]
total_cost = 0
while plots_remaining_to_consider:
    plot_to_consider = plots_remaining_to_consider.pop()
    plot_name = plot[plot_to_consider]
    explored = set()
    to_explore = {plot_to_consider}
    v_fence_gaps = set()
    h_fence_gaps = set()
    while to_explore:
        adjacent_plot = to_explore.pop()
        explored.add(adjacent_plot)
        plots_remaining_to_consider.discard(adjacent_plot)
        for (
            movement_row,
            movement_col,
            fence_orientation,
            fence_relative_row,
            fence_relative_col,
        ) in movements:
            potential_extension = (
                adjacent_plot[0] + movement_row,
                adjacent_plot[1] + movement_col,
            )
            if (
                plot.get(potential_extension) == plot_name
                and potential_extension not in explored
            ):
                to_explore.add(potential_extension)
                fence_location = (
                    adjacent_plot[0] + fence_relative_row,
                    adjacent_plot[1] + fence_relative_col,
                )
                if fence_orientation == "v":
                    v_fence_gaps.add(fence_location)
                else:
                    h_fence_gaps.add(fence_location)
    top_fences = set(explored) - h_fence_gaps
    bottom_fences = {(row + 1, col) for row, col in explored} - h_fence_gaps
    left_fences = set(explored) - v_fence_gaps
    right_fences = {(row, col + 1) for row, col in explored} - v_fence_gaps
    sides = 0
    for _, _, orientation, row_offset, col_offset in movements:
        fences_used = {
            (row + row_offset, col + col_offset) for row, col in explored
        } - (h_fence_gaps if orientation == "h" else v_fence_gaps)
        while fences_used:
            fence_row, fence_col = fences_used.pop()
            sides += 1
            for starting_offset in (1, -1):
                offset = starting_offset
                while (
                    fence := (
                        fence_row + (offset if orientation == "v" else 0),
                        fence_col + (offset if orientation == "h" else 0),
                    )
                ) in fences_used:
                    fences_used.remove(fence)
                    offset += starting_offset
    total_cost += len(explored) * (sides)
print(total_cost)
