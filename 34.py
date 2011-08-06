import math
def sumEqualFactorial(x):
	number = str(x)
	factorialSum = 0
	for i in number:
		factorialSum += math.factorial(int(i))
	if(factorialSum == x):
		return True
	else:
		return False
suma = 0
for a in range(3, 1000000):
	if(sumEqualFactorial(a)):
		suma += a
print suma
