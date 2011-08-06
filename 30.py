def canBeWritten(x):
	nums = str(x)
	sum = 0
	for i in nums:
		sum += int(i) ** 5
	if(sum == x):
		return True
	else:
		return False
found = []
for a in range(2, 1000000):
	if(canBeWritten(a)):
		found.append(a)
		print a
print ''
print sum(found)
