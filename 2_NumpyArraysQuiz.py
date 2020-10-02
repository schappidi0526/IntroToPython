import numpy as np
q1=np.array ([[1,2,3],
           [4,5,6],
           [7,8,9]])
print (q1.shape)
#Above will print 2-d array of 3*3

numbers_1 = [1,2,3]
numbers_2 = [4,5,6]
numbers_3 = [7,8,9]
q2 = np.array([numbers_1, numbers_2, numbers_3])
print (q2)
#Above will print 2-d array of 3*3

numbers_1 = [1,2,3]
numbers_2 = [4,5,6]
numbers_3 = [7,8,9]
q3 = np.array([numbers_1 + numbers_2 + numbers_3])
print (q3)
#Above will print 1-d array of 1*9

numbers = np.arange(1,13) 
print (numbers)
# print(numbers.reshape(2,6))
print(numbers.reshape(2,-6))#First value is for horizontal and second is vertical
print(numbers.reshape(-6,2))

q5=[[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
q5=np.array(q5)
print (q5.reshape(9,1))
print ((q5.reshape(9,1).shape))
print (q5.reshape(9,))
print ((q5.reshape(9,).shape))
print (q5.reshape(1,9))
print ((q5.reshape(1,9).shape))
#print (q5.reshape(3,4))


#below will give 2-d array of shape 100*1
a = range(100)
print (np.array(a))
print (np.array(a).shape)

a = np.array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
print (a)
a.reshape(3,4)