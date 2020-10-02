"""The diff between storing data in Numpy is different than in lists. 
   Lists store the data in memory with index pointers randomly so you can insert or delete 
   elements in it.
   But Numpy deletes the entire list and creates another with updated list. Data is continous in
   Numpy which makes arrays in Numpy faster than lists in Python especially with Numeric operations like
   SUM or AVERAGE. With strings it doesn't really matter which one we use.

   Numpy under the hood is built on C which makes it faster as well than Python
"""

#Numpy can handle multi dimensional arrays
#1 dimensional array
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
print (a)
#converting a list into a numoy array
import numpy as np
a1=[1,2,3,4,5,6,7,8,9,10]
a1=np.array(a1)
print (a1)
#2 dimensional array
import numpy as np
a1=np.array([[1,2,3,4,5,6,7,8,9,10],
            [11,12,13,14,15,16,17,18,19,20]])
print (1)
print (a1.shape)#Shape in not a function. So no '()'. It is a property of numpy array.
#converting two lists into a numpy array
import numpy as np
a1=[1,2,3,4,5,6,7,8,9,10]
a2=[11,12,13,14,15,16,17,18,19,20]
a3=np.array([a1,a2])
print(a3)
"""Below will give you  a tuple (2,10). 2 being the no of rows and 10 being the no of columns
""" 
print (a3.shape)

#Reshape an array in numpy
print (a3.reshape(10,2))

import numpy as np
a1=[1,2,3,4,5,6,7,8,9,10]#The dimension of the array is (10,0)
a1=np.array(a1)
print(a1.shape)#this will result in (10,) which is same as 1*10
print(a1.reshape(5,2))
print(a1.reshape(-5,2))

#Examples of three dimensional array

mylist = [
        [['@', '@'], ['@', '@']], 
        [['@', '@'], ['@', '@']], 
        [['@', '@'], ['@', '@']]
        ]

"""

1-dimensional is called as Vector
2-dimensional is called as Matrix
3-dimensional is called as Multi-dimensional

"""

#arange function. This is eactly same as range in Python

import numpy as np 
n=np.arange(10)
print (n)