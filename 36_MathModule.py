#floor function rounds it to the next lowest interger
from math import floor
x=3.5
print(floor(x))
y=-3.5
print(floor(y))
#ceil function rounds it to next highest integer
from math import ceil
y=3.5
print (ceil(y))
x=-3.5
print(ceil(x))

from math import pow
print (pow(3,2))

#Trunc just removes the decimal part of the number
from math import trunc
X=3.5
print (trunc(X))
y=-3.5
print (trunc(y))

#Exp gives you the value of e to the power of x(x being the value provided)
from math import exp
x=3
print(exp(x))

#power function

from math import pow
print(pow(3,4))

#square root function

from math import sqrt
print(sqrt(9))

#log function
from math import log
print(log(100))#by default it is e 
print(log(100,10))

#Trignometric Functions

from math import sin
print (sin(30))# this will not help python to specify in degrees. So it will not give you correct value

from math import sin,radians
print(sin(radians(30)))
print(sin(radians(90)))

#Special functions in math library
"""If there are decimals in a list and if you want to sum of them using 'SUM' function
it might not be able to provide correct results"""
l=[1.0,2.5,2,3.5,3.3,4,0.01,0.02,0.3]
print (sum(l))

#to make sure 'fsum' is a function in math library
from math import fsum
l=[1.0,2.5,2,3.5,3.3,4,0.01,0.02,0.3]
print (fsum(l))

#factorial function
from math import factorial
print (factorial(5))