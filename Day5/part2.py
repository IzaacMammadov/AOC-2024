from collections import defaultdict

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()


class PageNumber:
    ordering = defaultdict(set)

    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        return other.num not in self.ordering[self.num]


total = 0
cant_have_after = defaultdict(set)
for row in input_text:
    if "|" in row:
        num_1, num_2 = row.split("|")
        cant_have_after[int(num_2)].add(int(num_1))
    elif not row:
        PageNumber.ordering = cant_have_after
    else:
        nums = [int(x) for x in row.split(",")]
        cant_see = set()
        for num in nums:
            if num in cant_see:
                page_numbers = sorted([PageNumber(x) for x in nums])
                total += page_numbers[(len(page_numbers) - 1) // 2].num
                break
            cant_see = cant_see | cant_have_after[num]
print(total)
