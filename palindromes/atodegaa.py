l = []
with open("data.txt", "r") as infile:
    for line in infile:
        line = line.strip()
        if line == line[::-1] and len(set(line)) > 1:
            l.append(line)

print len(l), max(l, key=lambda s: len(s))
