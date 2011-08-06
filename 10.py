"""import math
primes = [2]
def isPrime(x):
	root = math.sqrt(x)
	i = 0
	if(primeCount == 0):
		return 1
	while(primes[i] < root):
		if(x % primes[i] == 0):
			return 0
		i += 1
	return 1
	
primeCount = 1
i = 3;
sum = 2;
z = 0;
while(i < 2000000):
	if(isPrime(i)):
		primes.append(i)
		primeCount += 1
		sum += i
		if(z >= 5000):
			print str(i) + ' ' + str(sum)
			z = 0
	i = i + 2
	z = z + 1
print sum
"""
def iter_primes ():
        # handle trivial case
        yield 2
        val = 1
        primesq_pairs = []
        while True:
                curr = None
                while (curr is None):
                        val += 2
                        curr = val
                        for prime, square in primesq_pairs:
                                if (curr < square):
                                        break
                                if (curr % prime == 0):
                                        curr = None
                                        break
                primesq_pairs.append ((curr, curr ** 2))
                yield curr


sum = 0
for x in iter_primes():
        if (x < 2000000):
                sum += x
        else:
                break
print sum