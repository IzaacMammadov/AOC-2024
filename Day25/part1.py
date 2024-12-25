with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

all_locks = []
all_keys = []

for i in range(len(input_text) // 8 + 1):
    if "." not in input_text[8 * i]:  # lock
        spaces = []
        for j in range(5):
            space = 5
            while input_text[8 * i + 6 - space][j] == "#":
                space -= 1
            spaces.append(space)
        all_locks.append(spaces)
    else:  # key
        ridges = []
        for j in range(5):
            ridge = 0
            while input_text[8 * i + 5 - ridge][j] == "#":
                ridge += 1
            ridges.append(ridge)
        all_keys.append(ridges)

print(
    sum(
        all(lock[i] >= key[i] for i in range(5))
        for lock in all_locks
        for key in all_keys
    )
)
