#ManyTimePadAttaker

##[Description]
This python script helps you find out a key that was used to encrypt many messages by trial-and-error method.
This is useful when you have multiple ciphertexts which were encrypted with a same long key, and want to find out the key and plaintexts.
The concept is that, guess a plaintext for one of the ciphertext, caculate the key and decrypt other ciphertexts. If the guess is correct, other plaintexts also make sense and you will know the right answer.

##[Dependency]

Python3.+

##[Usage]
"python ManyTimePadAttaker.py"

**The program run interactively. It will ask:**  
Enter the filname which contains ciphertexts:  
(It assumes ciphertexts are hex-encoded. The file should look like this: ![file example](https://github.com/636F57/resource/mtp-example3s.png).

**Specify target ciphertext number[(a range of number)] or key[(a number)]:**  
(Enter integer. The ciphertext with the index of specified number will be used as a ciphertext with known plaintext. If key is specifed, the key is used directly to deciher ciphertexts.)

**Please guess the plaintext for the target from the beginning:**  
(Just guess and enter some plaintext for the specifed ciphertext.)

Then it will calculate and print the temporary decrypted texts and the key.    
You can continue this routine until you quit.

Belows are screenshots of demo.
![screenshot1](https://github.com/636F57/resource/mtp-example1.png)
![screenshot2](https://github.com/636F57/resource/mtp-example2.png)

###[Note]
This software was made for quick personal use. Not tested much and probably will not be maintained.
Please feel free to fork/download to modify by yourself if needed.

