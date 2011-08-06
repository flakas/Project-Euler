import math
sum = 0
for i in range(1000):
	sum += i ** i
sum = str(sum)
print sum[-10:]
