def increasing_safe(nums):
    return all(nums[i] < nums[i + 1] < nums[i] + 4 for i in range(len(nums) - 1))


def decreasing_safe(nums):
    return all(nums[i] - 4 < nums[i + 1] < nums[i] for i in range(len(nums) - 1))


with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
total = 0
for line in input_text:
    nums = [int(x) for x in line.split()]
    total += increasing_safe(nums) or decreasing_safe(nums)
print(total)
