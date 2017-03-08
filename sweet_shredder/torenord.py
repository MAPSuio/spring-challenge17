from sys import stdin

# Usage: python3 torenord.py < input.txt

lines = stdin.readlines()

for i in range(len(lines)):
    print(lines[i].strip(), end="")
    if i % 40 == 39:
        print()
