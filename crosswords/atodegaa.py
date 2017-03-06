l = []
with open("data.txt", "r") as infile:
    for line in infile:
        l.append(line.strip())

print sorted(l, key=lambda s: (len(s), s))[9999]
