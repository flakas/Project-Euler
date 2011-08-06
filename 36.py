def isPalindromic(x):
	binary = bin(x)
	binary = binary[2:]
	number = str(x)
	reversedBinary = binary[::-1]
	reversedNumber = number[::-1]
	if(binary == reversedBinary and number == reversedNumber):
		return True
	else:
		return False
sum = 0
for i in range(1, 1000000):
	if(isPalindromic(i)):
		sum += i
print sum
