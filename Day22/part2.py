from collections import defaultdict

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

value = defaultdict(int)
for secret in input_text:
    secret = int(secret)
    sequence = []
    sequences_seen = set()
    for _ in range(2000):
        previous_secret = secret
        MOD = 16777216
        secret = ((secret << 6) ^ secret) % MOD
        secret = ((secret >> 5) ^ secret) % MOD
        secret = ((secret << 11) ^ secret) % MOD
        sequence.append(secret % 10 - previous_secret % 10)
        if len(sequence) > 4:
            sequence.pop(0)
        if len(sequence) == 4:
            tuple_sequence = tuple(sequence)
            if tuple_sequence not in sequences_seen:
                value[tuple_sequence] += secret % 10
                sequences_seen.add(tuple_sequence)
print(max(value.values()))
