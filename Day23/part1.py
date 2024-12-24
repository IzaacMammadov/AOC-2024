from collections import defaultdict
from itertools import combinations

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

connections = defaultdict(set)
for connection in input_text:
    person1, person2 = connection.split("-")
    connections[person1].add(person2)
    connections[person2].add(person1)
total = 0
for person1, person2, person3 in combinations(connections.keys(), 3):
    if (
        (person1[0] == "t" or person2[0] == "t" or person3[0] == "t")
        and person2 in connections[person1]
        and person3 in connections[person1]
        and person3 in connections[person2]
    ):
        total += 1
print(total)
