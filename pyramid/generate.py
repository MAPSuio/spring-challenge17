#!/usr/bin/env python3

def floor_cost(n):
    return 2 + (n-1)*2

def total_cost(n):
    return (n  * (floor_cost(1) + floor_cost(n))) // 2


#Chosen to give a number > 10 ** 12
print(total_cost(50005000))
