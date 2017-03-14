#FermatsFactor

##[License]
MIT License. See [here](https://github.com/636F57/CryptoAttackers/blob/master/LICENSE) for detail.

##[Description]
This python script trys to factor N of RSA public-key cryptosystem, namely trys to find two primes p and q such that N = p*q, by Fermat's factorization method.   
This runs efficiently when p and q are close values, otherwise it would take too long.  
(Execution time roughly 10 mins for |p-q| < 2**200)   

Reference: https://en.wikipedia.org/wiki/Fermat%27s_factorization_method 

##[Dependency]

Python3.+

##[Usage]
To run the program, simply type in console:
"python FermatsFactor.py"  

The program will ask you to input N. N must be a positive odd integer. Please input N as base-10 integer.     
When factorization succeeds, it outputs p and q as base-10 integers.  

By default, it stores the result in a file, "factor_out.txt". If you do not want to store, 
set the flag "bFileOut" to False in the source file.  

Below is a screenshot of demo.

![screenshot1](https://github.com/636F57/resource/blob/master/ff-example1.png)

###[Note]
This software was made for quick personal use. Not tested much and probably will not be maintained.
Please feel free to fork/download to modify by yourself if needed.

