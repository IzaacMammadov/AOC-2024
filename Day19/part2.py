from functools import cache

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

towels_trie = {}
for towel in input_text[0].split(", "):
    inner_dict = towels_trie
    for letter in list(towel):
        if letter not in inner_dict:
            inner_dict[letter] = {}
        inner_dict = inner_dict[letter]
    inner_dict[None] = None


@cache
def pattern_possible(pattern):
    if not pattern:
        return 1
    patterns_needed = []
    trie = towels_trie
    for i, letter in enumerate(pattern):
        if letter in trie:
            trie = trie[letter]
            if None in trie:
                patterns_needed.append(pattern[i + 1 :])
        else:
            break
    return sum(pattern_possible(sub_pattern) for sub_pattern in patterns_needed)


print(sum(pattern_possible(pattern) for pattern in input_text[2:]))
