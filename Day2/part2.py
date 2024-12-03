def increasing_safe(nums):
    no_drop = nums[0]
    yes_drop = {None}
    for num in nums[1:]:
        yes_drop = ({no_drop} if no_drop is not None else set()) | (
            {num} if any(i is None or i < num < i + 4 for i in yes_drop) else set()
        )
        no_drop = num if no_drop is not None and no_drop < num < no_drop + 4 else None
        if no_drop is None and not yes_drop:
            return False
    return True


def decreasing_safe(nums):
    no_drop = nums[0]
    yes_drop = {None}
    for num in nums[1:]:
        yes_drop = ({no_drop} if no_drop is not None else set()) | (
            {num} if any(i is None or i - 4 < num < i for i in yes_drop) else set()
        )
        no_drop = num if no_drop is not None and no_drop - 4 < num < no_drop else None
        if no_drop is None and not yes_drop:
            return False
    return True


with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
total = 0
for line in input_text:
    nums = [int(x) for x in line.split()]
    total += increasing_safe(nums) or decreasing_safe(nums)
print(total)
