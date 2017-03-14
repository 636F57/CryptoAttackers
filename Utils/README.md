#DiscreteLog.py

##[License]
MIT License. See [here](https://github.com/636F57/CryptoAttackers/blob/master/LICENSE) for detail.

##[Description]
This python script outputs x when given h, g, prime p, and the range of x [0 <= x <= max], such that g\*\*x = h mod p .
This uses meet-in-the-middle-attack, namely, expand x as x = x0 \* sqrt(max) + x1, then find x0 and x1, 
such that h/(g\*\*x1) == (g\*\*sqrt(max) )\*\*x0 in mod p, by exausive attack. Note that 0<= x0,x1 <= sqrt(max),
so it basically computes in about sqrt of time compared to the case of simple exausive attack (in which just try all x).

##[Dependency]

Python3.+

[gmpy2](https://pypi.python.org/pypi/gmpy2) package for high-precision caculation.  
You can install by "pip install gmpy2".

##[Usage]
To run the program, simply type in console:
"python DiscreteLog.py"

The program will ask you to input g, h, p, and possible maximum value of x.
Please input them as base-10 integer.
  

It will first make the table of [(g\*\*sqrt(max) )\*\*x0 in mod p], then compute [h/(g\*\*x1)] and try to
look it up in the table to find the matching pair of x0 and x1. It threre is, it is the answer.
By default, this stores the table data into a file for future use. Next time you input the same g, h, max values,
then the table will be re-used. Otherwise a new table will be created and saved. If you do not want to save to files,
you can turn this function off by setting the flag, bTablefiles, to False in the source file. Then it will create 
tables on memory everytime. 


Below is a screenshot of demo.

![screenshot1](https://github.com/636F57/resource/blob/master/dl-example2.png)

###[Note]
This software was made for quick personal use. Not tested much and probably will not be maintained.
Please feel free to fork/download to modify by yourself if needed.

