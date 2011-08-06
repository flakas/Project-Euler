triangles = []
pentagonals = []
hexagonals = []
for i in range(1, 100000):
	triangles.append(i * (i + 1) / 2)
	pentagonals.append(i * (3 * i - 1) / 2)
	hexagonals.append(i * (2 * i - 1))
for i in triangles:
	if((i in pentagonals) and (i in hexagonals)):
		print i
