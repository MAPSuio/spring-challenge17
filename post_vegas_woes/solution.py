#!/usr/bin/env python3

from sys import stdin
from itertools import combinations

graph = {}

names = ["Amin", "Pedro", "Joey", "Alex"]

# Build a graph
for name_a in names:
    graph[name_a] = {}
    for name_b in names:
        graph[name_a][name_b] = 0


# Process transactions
for line in stdin:

    byer, beneficiaries_str, amount = line.split("-")

    beneficiaries = beneficiaries_str.split(",")

    amount_per_beneficiary = int(amount) // len(beneficiaries)

    for b in beneficiaries:
        graph[b][byer] += amount_per_beneficiary


for pair in combinations(sorted(names), 2):

    a, b = pair

    # Joey owes Amin 40, Amin owes Joey 30
    if graph[a][b] >= graph[b][a]:

        #Joey owes Amin 10
        graph[a][b] -= graph[b][a]

        #Amin owes Joey 0
        graph[b][a] = 0
    else:
    # Amin owes Joey 40, Joey owes Amin 30
        graph[b][a] -= graph[a][b]

        graph[a][b] = 0

result = []
for name_a in sorted(names):
    for name_b in sorted(names):
        if name_a == name_b:
            continue
        result.append(graph[name_a][name_b])

print(" ".join(map(str, result)))
