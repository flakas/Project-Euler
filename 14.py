def getLength(n):
	length = 0
	while n > 1:
		if(n % 2 == 0):
			n /= 2
		else:
			n = n * 3 + 1
		length += 1
	return length + 1

longest = 0
number = 0
for i in range(1000000):
	x = getLength(i)
	if(x > longest):
		longest = x
		number = i
print str(number) + ' is ' + str(longest) + ' long'
