from collections import defaultdict

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

total = 0
cant_have_after = defaultdict(set)
for row in input_text:
    if "|" in row:
        num_1, num_2 = row.split("|")
        cant_have_after[int(num_2)].add(int(num_1))
    elif row:
        nums = [int(x) for x in row.split(",")]
        cant_see = set()
        for num in nums:
            if num in cant_see:
                break
            cant_see = cant_see | cant_have_after[num]
        else:
            total += nums[(len(nums) - 1) // 2]
print(total)
