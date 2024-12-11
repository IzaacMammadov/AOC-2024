from functools import cache

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()


@cache
def stones_created(num, rounds):
    if rounds == 0:
        return 1
    elif num == 0:
        return stones_created(1, rounds - 1)
    elif len(str(num)) % 2 == 0:
        return stones_created(
            int(str(num)[: len(str(num)) // 2]), rounds - 1
        ) + stones_created(int(str(num)[len(str(num)) // 2 :]), rounds - 1)
    else:
        return stones_created(num * 2024, rounds - 1)


nums = [int(x) for x in input_text[0].split()]
print(sum(stones_created(x, 25) for x in nums))
