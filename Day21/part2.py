from collections import Counter, defaultdict
from copy import deepcopy
from functools import cache
from itertools import pairwise

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

num_keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}
directional_keypad = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}


@cache
def num_keypad_path_count(start_num, end_num):
    start = num_keypad[start_num]
    end = num_keypad[end_num]
    x_diff = abs(end[0] - start[0])
    y_diff = abs(end[1] - start[1])
    horiz_char = ">" if end[0] > start[0] else "<"
    vert_char = "v" if end[1] > start[1] else "^"
    possible_path_counts = [
        Counter(pairwise(["A"] + list(possible_path)))
        for possible_path in {
            tuple([horiz_char] * x_diff + [vert_char] * y_diff + ["A"]),
            tuple([vert_char] * y_diff + [horiz_char] * x_diff + ["A"]),
        }
        if not (
            (start == (0, 0) and possible_path[:3] == ("v", "v", "v"))
            or (start == (0, 1) and possible_path[:2] == ("v", "v"))
            or (start == (0, 2) and possible_path[:1] == ("v",))
            or (start == (1, 3) and possible_path[:1] == ("<",))
            or (start == (2, 3) and possible_path[:2] == ("<", "<"))
        )
    ]
    if len(possible_path_counts) == 1:
        return possible_path_counts[0]
    original_possible_path_counts = deepcopy(possible_path_counts)
    for _ in range(4):
        for path_id in range(2):
            new_path_count = defaultdict(int)
            for move, count in possible_path_counts[path_id].items():
                for new_move, new_count in dir_keypad_path_count(*move).items():
                    new_path_count[new_move] += count * new_count
            possible_path_counts[path_id] = new_path_count
        if sum(possible_path_counts[0].values()) < sum(
            possible_path_counts[1].values()
        ):
            return original_possible_path_counts[0]
        elif sum(possible_path_counts[0].values()) > sum(
            possible_path_counts[1].values()
        ):
            return original_possible_path_counts[1]


@cache
def dir_keypad_path_count(start_dir, end_dir):
    start = directional_keypad[start_dir]
    end = directional_keypad[end_dir]
    x_diff = abs(end[0] - start[0])
    y_diff = abs(end[1] - start[1])
    horiz_char = ">" if end[0] > start[0] else "<"
    vert_char = "v" if end[1] > start[1] else "^"
    possible_move_counts = [
        [Counter(pairwise(["A"] + list(possible_path)))]
        for possible_path in {
            tuple([horiz_char] * x_diff + [vert_char] * y_diff + ["A"]),
            tuple([vert_char] * y_diff + [horiz_char] * x_diff + ["A"]),
        }
        if not (
            (start == (1, 0) and possible_path[:1] == ("<",))
            or (start == (2, 0) and possible_path[:2] == ("<", "<"))
            or (start == (0, 1) and possible_path[:1] == ("^",))
        )
    ]
    if len(possible_move_counts) == 1:
        return possible_move_counts[0][0]
    original_possible_move_counts = possible_move_counts
    for _ in range(4):
        new_possible_move_counts = [[], []]
        for path_id in range(2):
            for old_move_count in possible_move_counts[path_id]:
                move_count_to_append = [defaultdict(int)]
                for old_move, old_count in old_move_count.items():
                    dicts_to_add_on = [
                        defaultdict(
                            int,
                            {
                                new_move: old_count * new_count
                                for new_move, new_count in new_move_count.items()
                            },
                        )
                        for new_move_count in naive_dir_keypad_path_count(
                            directional_keypad[old_move[0]],
                            directional_keypad[old_move[1]],
                        )
                    ]
                    move_count_to_append = [
                        defaultdict(
                            int,
                            {
                                a: dict_1[a] + dict_2[a]
                                for a in dict_1.keys() | dict_2.keys()
                            },
                        )
                        for dict_1 in move_count_to_append
                        for dict_2 in dicts_to_add_on
                    ]
                new_possible_move_counts[path_id] += move_count_to_append
        possible_move_counts = [
            [
                x
                for x in new_possible_move_counts[i]
                if sum(x.values())
                == min(sum(y.values()) for y in new_possible_move_counts[i])
            ]
            for i in range(2)
        ]
        if sum(possible_move_counts[0][0].values()) < sum(
            possible_move_counts[1][0].values()
        ):
            return original_possible_move_counts[0][0]
        elif sum(possible_move_counts[0][0].values()) > sum(
            possible_move_counts[1][0].values()
        ):
            return original_possible_move_counts[1][0]


@cache
def naive_dir_keypad_path_count(start, end):
    x_diff = abs(end[0] - start[0])
    y_diff = abs(end[1] - start[1])
    horiz_char = ">" if end[0] > start[0] else "<"
    vert_char = "v" if end[1] > start[1] else "^"
    possible_paths = [
        Counter(pairwise(["A"] + list(possible_path)))
        for possible_path in {
            tuple([horiz_char] * x_diff + [vert_char] * y_diff + ["A"]),
            tuple([vert_char] * y_diff + [horiz_char] * x_diff + ["A"]),
        }
        if not (
            (start == (1, 0) and possible_path[:1] == ("<",))
            or (start == (2, 0) and possible_path[:2] == ("<", "<"))
            or (start == (0, 1) and possible_path[:1] == ("^",))
        )
    ]
    return possible_paths


total = 0
for code in input_text:
    move_count = Counter(pairwise("A" + code))
    new_move_count = defaultdict(int)
    for move, count in move_count.items():
        for new_move, new_count in num_keypad_path_count(*move).items():
            new_move_count[new_move] += new_count * count
    move_count = new_move_count
    for _ in range(25):
        new_move_count = defaultdict(int)
        for move, count in move_count.items():
            for new_move, new_count in dir_keypad_path_count(*move).items():
                new_move_count[new_move] += new_count * count
        move_count = new_move_count
    total += sum(move_count.values()) * int(code[:3])
print(total)
