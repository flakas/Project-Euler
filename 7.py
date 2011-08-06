primes = []
def isPrime(x):
	for i in primes:
		if(x % i == 0):
			return 0
	return 1
	
primeCount = 0
i = 2;
while(primeCount <= 10001):
	if(isPrime(i)):
		print i
		primes.append(i)
		primeCount = primeCount + 1
		if(primeCount == 10001):
			print i
			break
	i = i + 1