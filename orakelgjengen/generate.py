#!/usr/bin/env python3

from string import ascii_uppercase as companies
from sklearn.utils import shuffle
import random


random.seed(1337)

print("Company\t\tX\t\tY")

for company in companies:

    dataset_length = random.randrange(100, 1000 + 1)

    predicted = [True] * random.randrange(dataset_length+1)
    other = [False] * (dataset_length - len(predicted))

    is_predicted = shuffle(predicted + other)
    alpha = random.randrange(100, 1000)
    beta = random.randrange(100, 1000)

    for x in range(1, dataset_length + 1):
        if is_predicted.pop():
            print(company + "\t\t" + str(x) + "\t\t" + str(alpha + (beta * x)))
        else:
            print(company + "\t\t" + str(x) + "\t\t" + str(alpha + (random.randrange(1000) * x)))
