import math
primes = []
def isPrime(x):
	if x == 1:
		return False
	for z in primes:
		if(z == x):
			continue
		if(x % z == 0):
			return False
	return True
def isCircularPrime(x):
	number = list(str(x))
	for i in range(1, len(number)):
		y = number.pop(0)
		number.append(y)
		if(not(isPrime(int("".join(number))))):
			return False
	return True
for i in range(2, 1000000):
	if(isPrime(i)):
		primes.append(i)
count = 0
for a in primes:
	if(isCircularPrime(a)):
		count += 1
print count
