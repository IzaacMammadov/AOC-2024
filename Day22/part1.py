with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

total = 0
for secret in input_text:
    secret = int(secret)
    for _ in range(2000):
        MOD = 16777216
        secret = ((secret << 6) ^ secret) % MOD
        secret = ((secret >> 5) ^ secret) % MOD
        secret = ((secret << 11) ^ secret) % MOD
    total += secret
print(total)
