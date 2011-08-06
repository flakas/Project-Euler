import math
primes = []
def genPrimes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]
def isPrime(x):
	if x == 1:
		return False
	for z in primes:
		if(z == x):
			continue
		if(x % z == 0):
			return False
	return True

def isTruncatable(x):
	number = str(x)
	length = len(number)
	for i in range(0, length): #truncate from left
		if(not(isPrime(int(number[i:])))):
			return False
	for i in range(0, length):
		if(not(isPrime(int(number[:(length - i)])))):
			return False
	return True
		
primes = genPrimes(1000000)
print primes
sum = 0
for a in range(8, 1000000):
	if(isTruncatable(a)):
		sum += a
		print a
print sum

