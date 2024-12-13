with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

total = 0
for problem in range((len(input_text) + 1) // 4):
    button_a_move_x, button_a_move_y = (
        input_text[problem * 4].removeprefix("Button A: ").split(", ")
    )
    button_a_move = (
        int(button_a_move_x.removeprefix("X+")),
        int(button_a_move_y.removeprefix("Y+")),
    )
    button_b_move_x, button_b_move_y = (
        input_text[problem * 4 + 1].removeprefix("Button B: ").split(", ")
    )
    button_b_move = (
        int(button_b_move_x.removeprefix("X+")),
        int(button_b_move_y.removeprefix("Y+")),
    )
    target_x, target_y = input_text[problem * 4 + 2].removeprefix("Prize: ").split(", ")
    target = (int(target_x.removeprefix("X=")), int(target_y.removeprefix("Y=")))

    min_cost = float("inf")
    for a_presses in range(101):
        for b_presses in range(101):
            if (
                a_presses * button_a_move[0] + b_presses * button_b_move[0],
                a_presses * button_a_move[1] + b_presses * button_b_move[1],
            ) == target:
                min_cost = min(min_cost, a_presses * 3 + b_presses)
    if min_cost < float("inf"):
        total += min_cost
print(total)
