import binascii
import sys

def isPrintable(x):
	if x < 0x20 or x > 0x79:
		return False
	else:
		return True

if __name__ == "__main__":
	
	ciphertextfilename = input("Enter the filname which contains ciphertexts:\n")
	
	ciphertexts = []
	with open(ciphertextfilename, "r") as f:
		ciphertexts = f.read().split('\n')

	if len(ciphertexts) == 0:
		print("Could not read ciphertexts.")
		sys.exit()
	
	for i in range(len(ciphertexts)):
		ciphertexts[i] = binascii.unhexlify(ciphertexts[i])
	
	try:
		lenciphers = len(ciphertexts)
		while True:
			targetindex = -1
			while targetindex < 0 or targetindex > len(ciphertexts):
				targetindex = int(input("Specify target ciphertext number[0-{0}] or key[{1}]:".format(lenciphers-1, lenciphers)))
			
			guessplain = input("Please guess the plaintext for the target from the beginning:\n")
			print("Guessed target plaintext="+guessplain)
			
			key = []
			plains = [[] for x in ciphertexts]
			if targetindex == lenciphers:
				key = bytes(guessplain, 'utf-8')			
			else:
				target = ciphertexts[targetindex]			
				for i in range(len(guessplain)):
					if len(target) <= i:
						break
					key.append(ord(guessplain[i])^target[i])
				
			for i in range(len(key)):
				for j in range(len(ciphertexts)):
					if len(ciphertexts[j]) <= i:
						continue
					tmpchr = (ciphertexts[j][i]^key[i])
					if isPrintable(tmpchr):
						plains[j].append(chr(tmpchr))
					else:
						plains[j].append(hex(tmpchr))
						
			print("Resulting decrypted texts:")
			for i in range(len(plains)):
				if len(plains[i]) > 0:
					print(str(i)+":"+"".join(plains[i]))
				else:
					print(str(i)+":")
					
			print("key=", [chr(x) if isPrintable(x) else hex(x) for x in key])
			
			ans = input("\nEnter 'q' to exit, something else to continue: ")
			if ans == 'q':
				sys.exit()
	except KeyboardInterrupt:
		sys.exit()
		
