from collections import defaultdict
from copy import deepcopy

with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()

connections = defaultdict(set)
for connection in input_text:
    person1, person2 = connection.split("-")
    connections[person1].add(person2)
    connections[person2].add(person1)

max_clique_size = 0
max_clique = set()


def bron_kerbosch(R, P, X):
    global max_clique
    global max_clique_size
    if (not P) and (not X) and len(R) > max_clique_size:
        max_clique = R
        max_clique_size = len(R)
    for person in deepcopy(P):
        bron_kerbosch(R | {person}, P & connections[person], X & connections[person])
        P -= {person}
        X |= {person}


bron_kerbosch(set(), set(connections.keys()), set())
print(",".join(sorted(max_clique)))
