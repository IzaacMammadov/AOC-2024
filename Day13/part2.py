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
    target = (
        int(target_x.removeprefix("X=")) + 10000000000000,
        int(target_y.removeprefix("Y=")) + 10000000000000,
    )
    sol_a, sol_b = (
        (button_b_move[1] * target[0] - button_b_move[0] * target[1])
        // (button_a_move[0] * button_b_move[1] - button_a_move[1] * button_b_move[0]),
        (-button_a_move[1] * target[0] + button_a_move[0] * target[1])
        // (button_a_move[0] * button_b_move[1] - button_a_move[1] * button_b_move[0]),
    )
    if (
        (
            (button_b_move[1] * target[0] - button_b_move[0] * target[1])
            % (
                button_a_move[0] * button_b_move[1]
                - button_a_move[1] * button_b_move[0]
            )
        )
        == 0
        and (
            (-button_a_move[1] * target[0] + button_a_move[0] * target[1])
            % (
                button_a_move[0] * button_b_move[1]
                - button_a_move[1] * button_b_move[0]
            )
        )
        == 0
        and sol_a > 0
        and sol_b > 0
    ):
        total += 3 * sol_a + sol_b

print(total)
