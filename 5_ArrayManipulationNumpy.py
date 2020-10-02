#Append
import numpy as np
a=np.array([[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]]
)

a1=np.array([21,22,23,24,25])

print (np.append(a,[a1],axis=0))
#print (np.append(a,[a1],axis=1))#This will throw an error as this will not fit along axis=1
a11=np.array([21,22,23,24])
#reshaping a1
a2=a11.reshape(4,-1)
print (a2)
print (np.append(a,a2,axis=1))
print (np.append(a,a11.reshape(4,1),axis=1))
print (a2)
#Insert

ai=np.insert(a,2,a1,axis=0)
print (ai)
aj=np.insert(a,3,a11,axis=1)
print (aj)

#Delete

print (a)

nd=np.delete(a,0,axis=1)

print (nd)