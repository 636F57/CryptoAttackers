### WienersAttack.py 
### https://en.wikipedia.org/wiki/Wiener's_attack
###
### MIT License 
### Copyright (c) 2017 636F57@GitHub 
### See more detail at https://github.com/636F57/CryptoAttackers/blob/master/LICENSE 

from decimal import *
from fractions import Fraction
import math

# return a list of continuous fraction
def contFraction(number, maxlen=15, cutoff=1e-10):
	result = []
	value = Decimal(number)
	remainder = int(number)
	result.append(remainder)

	while len(result) < maxlen:
		value -= remainder
		if value > cutoff:
			value = Decimal(1) / value
			remainder = int(value)
			result.append(remainder)
		else:
			break
	return result
	
# convert a list of continuous fraction into a list of (numerator, denominator) 
def getConvergence(fraclist):
	result = []
	nume = 1
	denom = 1
	i0 = 0
	for i in range(len(fraclist)):
		if fraclist[i] == 0:
			result.append((0,1))
			i0 = 1
		else:
			nume = 1
			denom = fraclist[i]
			for j in reversed(range(i0,i)):
				prev_denom = denom
				denom = denom * fraclist[j] + nume
				nume = prev_denom
			gcd = math.gcd(int(nume),int(denom))
			denom /= gcd
			nume /= gcd
			result.append((int(nume), int(denom)))
	return result

# return two x as solution of ax^2+bx+c=0
# solve only for real numbers
def solveQuadratic(a,b,c):
	D = b*b - 4*a*c 
	if D < 0 or a == 0:
		return None, None
	else:
		x1 = (-b - math.sqrt(D))/(2*a)
		x2 = (-b + math.sqrt(D))/(2*a)
		return x1, x2
		
def solveQuadratic(a:Decimal, b:Decimal, c:Decimal):
	D = b*b - Decimal(4)*a*c 
	if D < 0 or a == 0:
		return None, None
	else:
		x1 = (-b - D.sqrt())/(2*a)
		x2 = (-b + D.sqrt())/(2*a)
		return x1, x2
		
def calcPhi(e, d, k):
	if k == 0:
		return None
	else:
		return ((e*d-1)/k)

def isInteger(num:float):
	return ((num % 1) == 0 )
	
def isInteger(num:Decimal):
	return (num == num.to_integral_value())


if __name__ == "__main__":
	
	print("RSA Wieners Attack: Derive private exponent d from public exponents N and e when d is smaller than 4th root of N over 3.\n")

	N = input("Enter N as base-10 integer:")
	e = input("Enter e as base-10 integer:")

	p = 0
	q = 0
	phi = 0
	d = 0
	
	getcontext().prec = 4096
	fraclist = contFraction(Decimal(e)/Decimal(N))
	#print(fraclist)
	convlist = getConvergence(fraclist)
	#print(convlist)
	for conv in convlist:
		k = conv[0]
		d = conv[1]
		phi = calcPhi(Decimal(e), Decimal(d), Decimal(k))
		if phi == None:
			continue
		if not isInteger(phi):
			continue
		a = Decimal(1)
		b=  - Decimal(N) + phi - Decimal(1)
		c = Decimal(N)
		x1, x2 = solveQuadratic(a, b, c)
		if x1 == None:
			continue
		if x1 < 0 or x2 < 0:
			continue
		if isInteger(x1) and isInteger(x2):
			p = x1
			q = x2
			print("phi=",phi)
			print("d=",d)
			print("p=",p)
			print("q=",q)

	print("done")
