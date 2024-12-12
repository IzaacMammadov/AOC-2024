with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

plot = {
    (row, col): input_text[row][col]
    for row in range(len(input_text))
    for col in range(len(input_text[0]))
}
plots_remaining_to_consider = set(plot)
movements = ((0, 1), (0, -1), (1, 0), (-1, 0))
total_cost = 0
while plots_remaining_to_consider:
    plot_to_consider = plots_remaining_to_consider.pop()
    plot_name = plot[plot_to_consider]
    explored = set()
    to_explore = {plot_to_consider}
    less_fences = 0
    while to_explore:
        adjacent_plot = to_explore.pop()
        explored.add(adjacent_plot)
        plots_remaining_to_consider.discard(adjacent_plot)
        for movement_row, movement_col in movements:
            potential_extension = (
                adjacent_plot[0] + movement_row,
                adjacent_plot[1] + movement_col,
            )
            if plot.get(potential_extension) == plot_name:
                less_fences += 1
                if potential_extension not in explored:
                    to_explore.add(potential_extension)
    total_cost += len(explored) * (4 * len(explored) - less_fences)
print(total_cost)
