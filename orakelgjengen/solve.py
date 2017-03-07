#!/usr/bin/env python3
from scipy.stats import pearsonr
from sys import stdin

table = {}
potential_companies = []
threshold = 0.6

#Ignore header
next(stdin)

for line in stdin:
    company, x, y = line.strip().split()

    if company not in table:
        table[company] = {}
        table[company]["x"] = []
        table[company]["y"] = []

    table[company]["x"].append(float(x))
    table[company]["y"].append(float(y))

for company in table.keys():
    pearson_score = pearsonr(table[company]["x"], table[company]["y"])[0]

    if (pearson_score ** 2) > threshold:
        potential_companies.append(company)


print(",".join(sorted(potential_companies)))
