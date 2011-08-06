maximum = 0
for a in range(1, 100):
	for b in range (1, 100):
		number = str(a ** b)
		number = [int(i) for i in number]
		suma = sum(number)
		if(suma > maximum):
			maximum = suma
print maximum

