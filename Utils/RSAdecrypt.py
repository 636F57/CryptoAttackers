### RSAdecrypt.py 
### Decrypt hex-coded RSA ciphertext from RSA components of N, e, d.
###
### MIT License 
### Copyright (c) 2017 636F57@GitHub 
### See more detail at https://github.com/636F57/CryptoAttackers/blob/master/LICENSE 

from Crypto.PublicKey import RSA
import binascii

	
if __name__=="__main__":
	
	N = int(input("Enter N as base-10 integer:"))
	e = int(input("Enter e as base-10 integer:"))
	d = int(input("Enter d as base-10 integer:"))
	cipher = input("Enter the ciphertext (hex-coded):")
	
	ciphertext = binascii.unhexlify(cipher)
	
	RSAkey = RSA.construct((N, e, d))
	print(RSAkey)
	
	plain = RSAkey.decrypt(ciphertext)
	print(plain)
	
	print("done")
