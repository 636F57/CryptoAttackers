#WienersAttack

##[License]
MIT License. See [here](https://github.com/636F57/CryptoAttackers/blob/master/LICENSE) for detail.

##[Description]
This python script trys to derive private exponent d from public exponents N and e of RSA public-key protocol, using Wiener's Attack method.
Note that Wiener's Attack works only when d is smaller than 4th root of N over 3. 
Reference: https://en.wikipedia.org/wiki/Wiener's_attack 

##[Dependency]

Python3.+

##[Usage]
To run the program, simply type in console:
"python WienersAttack.py"

The program will ask you to input N and e., and possible maximum value of x.
Please input them as base-10 integer.

Below is a screenshot of demo.

![screenshot1](https://github.com/636F57/resource/blob/master/wn-example1.png)

###[Note]
This software was made for quick personal use. Not tested much and probably will not be maintained.
Please feel free to fork/download to modify by yourself if needed.

