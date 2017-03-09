### DiscreteLog.py 
###
### Compute x when given h, g prime p, and the range of x [0 <= x <= max], such that g**x = h mod p 
###
### This uses meet-in-the-middle-attack, namely, expand x as x = x0 * sqrt(max) + x1, find x0 and x1
### such that h/(g**x1) == (g**sqrt(max) )**x0 in mod p, by exausive attack.
###
### MIT License 
### Copyright (c) 2017 636F57@GitHub 
### See more detail at https://github.com/636F57/CryptoAttackers/blob/master/LICENSE 


import gmpy2
from gmpy2 import mpz  # multiple precision integers module
import sys
import pickle
import hashlib
import math

bTablefiles = True

def createTable(g, p, B): 
	print("Creating table...")
	table = {}
	pp = mpz(p)
	gB = (mpz(g)** mpz(B)) % pp  
	key = mpz(1)
	progressbase = int(B/10)
	for x0 in range(B+1):  # create table of [(g**B)^x0] mod p
		table[key] = x0
		key = ( key * gB ) % pp
		if x0 % progressbase == 0:
			print( x0*10 // progressbase, "% done.")
	return table



if __name__ == "__main__":

	g = mpz(input("Enter g:"))
	h = mpz(input("Enter h:"))
	p = mpz(input("Enter p:"))
	max = int(input("Enter max of 0 <= x <= max:"))
	B = int(math.sqrt(max)) + 1
	
	# create table file name
	m = hashlib.sha1()
	m.update(bytes(str(g),'utf-8'))
	m.update(bytes(str(p),'utf-8'))
	m.update(bytes(str(B),'utf-8'))
	tablefilename = m.hexdigest()
	
	table = {}
	if bTablefiles:
		try:
			fr = open(tablefilename, "rb")
			table = pickle.load(fr)
			fr.close()
			print("Table data loaded.")
		except:
			table = createTable(g, p, B)
			fw = open(tablefilename, "wb")
			pickle.dump(table, fw)
			fw.close()
			print("Table data saved.", tablefilename)
	else:
		table = createTable(g, p, B)
			
	if len(table) == 0:
		print("No table data.")
		sys.exit()
		
		
	x0 = -1
	x1 = -1
	hh = mpz(h) % p
	gg = mpz(g) % p
	# look up [h/(g^x1) mod p] in the table to find a matching x0
	print("Looking up the table...")
	progressbase = int(B/10)
	gg_tmp = 1
	for x1 in range(B+1):
		ginv = gmpy2.invert(gg_tmp, p)
		if ginv > 0:
			key = ( hh * mpz(ginv) ) % p
			x0 = table.get(key, -1)
			if x0 > -1:
				x = x0 * B + x1
				print("Found. x0 =",x0, ", x1 =", x1, ", x =", x)
				sys.exit()
		gg_tmp = ( gg_tmp * gg ) % p
		if x1 % progressbase == 0:
			print( x1*10 // progressbase, "% done.")
	else:
		print("No x found.")
		
