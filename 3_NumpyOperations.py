#Element wise operations
"""Numpy treates each element and add each element in each numpy list"""
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b
print(c)
"""We can do all operations on each element of a numpy array"""
print(c*3)
"""if we give other list with only one element, numpy will assume all other elements with the same
    value in other numpy array. This concept is called broadcasting"""
x=np.array([4,5,6])
y=np.array([2])
z=x+y
print (z)
"""But it doesn't work if we give two values which will result in syntax error"""
# x=np.array([4,5,6])
# y=np.array([2,3])
# z=x+y
# print (z)


#Aggregate Operators
a=np.array([[1,2,3],
            [4,5,6]])
"""Horizontal ins axis 0 and vertical is axis 1.If you are dealing with 3-d array
then you will have axis 2"""
suma1=np.sum(a,axis=1)
print (suma1)