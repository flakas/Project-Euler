def arrivesAt89(x):
	while(True):
		a = x
		x = sum([int(i) ** 2 for i in str(x)])
		if(a == x):
			return False
		if(x == 89):
			return True
count = 0
for i in range(1, 10000000):
	print i
	if(arrivesAt89(i)):
		count += 1
print count
