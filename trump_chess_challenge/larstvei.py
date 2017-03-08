ratings = [2838.0, 2822.0, 2817.0, 2811.0, 2803.0, 2793.0, 2786.0, 2783.0, 2774.0, 2772.0, 2771.3, 2761.0, 2759.0, 2755.1, 2751.1, 2751.0, 2750.0, 2749.6, 2746.8, 2745.0, 2741.0, 2739.0, 2734.0, 2732.0, 2728.6]

def combinations(lst, r, tobeat, score, j, l):
    count = 0
    n, i = len(lst), 0
    ns = range(n)
    q = [[True] * r + [False] * (n-r)]
    while True:
        selection = [x for k, x in enumerate(lst) if q[i][k]]
        avg = (sum(selection) + score)/float(j-1+l)
        if avg > tobeat:
            count += 1
            for c in [k for k, b in enumerate(q[i][:-1]) if q[i][k]]:
                if not q[i][c+1]:
                    shifted = [not q[i][k] if k == c or k == c+1 else q[i][k] for k in ns]
                    if shifted not in q:
                        q.append(shifted)

        if all(q[i][-r:]) or i == len(q) - 1:
            return count
        i += 1

n = len(ratings)
count = n+1

for i in range(n):
    for j in range(i+1, n):
        if j == 1:
            continue
        score = sum(ratings[:j]) - ratings[i]
        tobeat = (ratings[i]+ratings[j])/float(2)

        if score/float(j-1) > tobeat:
            count += 1 if j != 2 else 0
        else:
            continue

        candidates = ratings[j+1:]
        for l in range(1, len(candidates) + 1):
            count += combinations(candidates, l, tobeat, score, j, l)

print count
