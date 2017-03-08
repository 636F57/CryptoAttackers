#PaddingOracleAttacker

##[License]
MIT License. See [here](https://github.com/636F57/CryptoAttackers/blob/master/LICENSE) for detail.

##[Description]
This python script helps you retrieve plaintext from ciphertext by CBC-padding oracle attack. 
This can be used when the ciphertext is encrypted RSA-CBC with PKCS5 padding and the server returns different error codes between the invalid padding and failure of message authentication.
The attack is basically exausive attack and it requires ca. 256 * (byte length of ciphertext) attemps at worst case.
And the program assumes the query is done by GET request. Please modify by yourself if you need POST and so on.

##[Dependency]

Python3.+

##[Usage]
To run the program, simply type in console:
"python PaddingOracleAttacker.py"

The program run interactively. It will ask:  
  
**Enter URL which will be followed by ciphertexts:**    
(You must enter the full URL til right before the ciphertext follows. For example, if the server accepts ciphertext like, 
http://hostname.com/foo.php?re=f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bdbdf302936266926ff37dbf7035d5eeb4
then you should enter "http://hostname.com/foo.php?re=" here.)

**Enter the ciphertext (hex-coded):**  
(In the example case above, you are expected to enter "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bdbdf302936266926ff37dbf7035d5eeb4" here.)

**Enter the HTTP error code number which the server returns when it detects invalid padding.(ex. 404 etc):**  
(Enter integer, 404 or 403 or something like that, as it says.)


Then it will first try to find out the correct padding. Then find out the rest of the plaintext, skipping the padding bytes to save the attemps. 
So, the program fails if the ciphertext is encrypted with wrong padding. In that case, you can try exausive attack on every ciphertext bytes by changing the flag, bAllExausive, from False to True in source code.  

Belows are screenshots of demo.

![screenshot1](https://github.com/636F57/resource/blob/master/po-example1.png)
![screenshot2](https://github.com/636F57/resource/blob/master/po-example2.png)

###[Note]
This software was made for quick personal use. Not tested much and probably will not be maintained.
Please feel free to fork/download to modify by yourself if needed.

