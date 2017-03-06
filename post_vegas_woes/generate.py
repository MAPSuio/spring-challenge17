#!/usr/bin/env python3

from random import choice, sample, randrange

names = ["Amin", "Pedro", "Joey", "Alex"]


def make_transaction():

    payer = choice(names)

    n_beneficiaries = randrange(1, len(names)+1)
    beneficiaries = sample(names, n_beneficiaries)

    amount = randrange(20, 2000 + 1) * n_beneficiaries

    return payer + "-" + ",".join(beneficiaries) + "-" + str(amount)

n_transactions = 10000

for t in range(n_transactions):
    print(make_transaction())
