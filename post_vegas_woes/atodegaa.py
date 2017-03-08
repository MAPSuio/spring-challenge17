people = ["Amina", "Joey", "Pedro"]
pairs = [(person1, person2) for person1 in people for person2 in people if person1 != person2]

owes = {pair: 0 for pair in pairs}
with open("input.in", "r") as infile:
	for line in infile:
		paid, benefit, money = line.split("-")
		benefit = benefit.split(",")
		money = int(money)
		for person in benefit:
			if person != paid:
				owes[(person, paid)] += (money // len(benefit))

for pair in pairs:
	if owes[pair] >= owes[(pair[1], pair[0])]:
		print pair[0], "owes", pair[1], owes[pair] - owes[(pair[1], pair[0])]

#Then letting the sum Joey owes Amina be transferred to the other two payments such that
#Amina pays Pedro 86489 - 4222 = 82267 and
#Joey pays Pedro 102333 + 4222 = 106555
