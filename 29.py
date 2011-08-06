numbers = []
for a in range(2, 101):
	for b in range(2, 101):
		if(not(a ** b in numbers)):
			numbers.append(a ** b)
print len(numbers)
