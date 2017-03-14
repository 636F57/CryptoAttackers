### FermatsFactor.py 
### https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
###
### MIT License 
### Copyright (c) 2017 636F57@GitHub 
### See more detail at https://github.com/636F57/CryptoAttackers/blob/master/LICENSE 


from decimal import *
import time
import sys


bFileOutput = True

def fermatsFactorBasic(N):  
	NN = Decimal(N)
	A = NN.sqrt()    
	A = A.to_integral_value(rounding=ROUND_CEILING)
	b2 = A * A - NN
	
	try:
		tmp = b2.sqrt()
		while tmp != tmp.to_integral_value():
			A += 1                  # search upward to find A such that A = (p+q)/2
			b2 = A * A - NN
			tmp = b2.sqrt()
	except KeyboardInterrupt:
		print("Interrupted. A=",A)
		sys.exit()
		
	p = A + tmp                 # tmp = abs((p-q)/2)
	q = A - tmp
	return int(p), int(q) 

if __name__ == "__main__":

	getcontext().prec = 4096

	N = Decimal(input("Enter N as base-10 integer:"))

	if N < 0 or N % Decimal(2) == 0:
		print("N must be a positive odd integer.")
		sys.exit()	
	
	t_start = time.time()
	
	p, q = fermatsFactorBasic(N)  

	t_taken = time.time()-t_start

	if bFileOutput:
		with open("factor_out.txt", "w") as f:
			strOut = "N = " + str(N) + "\n"
			f.write(strOut)
			print(strOut)
			strOut = "p = " + str(p) + "\n"
			f.write(strOut)
			print(strOut)  
			strOut = "q = " + str(q) + "\n"
			f.write(strOut)
			print(strOut)
			strOut = "calc time =" + str(t_taken // 60) + " min " + str(t_taken % 60) + " sec" + "\n"
			f.write(strOut)
			print(strOut) 
	else:
		print( "N =", N)
		print( "p =", p)
		print( "q =", q)
		print( "calc time =", t_taken // 60, " min", t_taken % 60, "sec")
		
	print("done")
