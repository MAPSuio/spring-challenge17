def r_squared(x_values, y_values):
	x_mean = sum(x_values)/float(len(x_values))
	y_mean = sum(y_values)/float(len(y_values))
	r2 = sum((xi-x_mean)*(yi-y_mean) for (xi, yi) in zip(x_values, y_values))**2 / (sum((xi-x_mean)**2 for xi in x_values)*sum((yi-y_mean)**2 for yi in y_values))
	return r2

d = {}

with open("table.in", "r") as infile:
	infile.readline()
	for line in infile:
		l = line.split()
		if l[0] in d:
			d[l[0]].append((float(l[1]), float(l[2])))
		else:
			d[l[0]] = [(float(l[1]), float(l[2]))]

s = ""
for company in sorted(d.keys()):
	x_vals = [elem[0] for elem in d[company]]
	y_vals = [elem[1] for elem in d[company]]
	if r_squared(x_vals, y_vals) > 0.6:
		s += (company+",")
print s[:-1]
