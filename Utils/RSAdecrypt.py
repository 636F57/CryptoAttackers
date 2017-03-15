### RSAdecrypt.py 
### Decrypt hex-coded RSA ciphertext from RSA components of N, e, d.
###
### MIT License 
### Copyright (c) 2017 636F57@GitHub 
### See more detail at https://github.com/636F57/CryptoAttackers/blob/master/LICENSE 

import binascii
import math


def powerMod(num, expo, modu):
	expo2_max = int(math.log2(expo))
	
	# create power table
	powertable = {0:1}
	tmp = (num*num) % modu
	for i in range(1,expo2_max+1):
		powertable[i] = tmp
		tmp = (tmp*tmp) % modu
	
	# multiply using powertable
	expo_r = expo
	expo2 = expo2_max
	result = 1
	while expo2 > 1:
		result = (result * powertable[expo2]) % modu
		expo_r = expo_r - 2**expo2
		expo2 = int(math.log2(expo_r))
	if expo_r > 0:
		result = result * num % modu
	
	return result
	
	
if __name__=="__main__":
	
	N = int(input("Enter N as base-10 integer:"))
	d = int(input("Enter d as base-10 integer:"))
	cipher = input("Enter the ciphertext (hex-coded):")
	
	cipherint = int("0x"+cipher,16)
	
	plainint = powerMod(cipherint, d, N)
	
	plainhex = hex(plainint)[2:]
	if len(plainhex) % 2 == 1:
		plainhex = "0"+plainhex
	
	plain = binascii.unhexlify(plainhex)
	print(plain)
	
	print("done")
