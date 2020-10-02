"""Numpy is faster than regular python functions as it stores values CONTINOUSLY where as 
   python stores values randomly"""

#without Numpy
import time
sum=0
starttime=time.time()
for i in range(10000000):
    sum=sum+i
print (sum)
endtime=time.time()
time=endtime-starttime
print (time)

#using numpy
import numpy as np
import time
sum=0
starttime=time.time()
numbers = np.arange(10000000)
sum=np.sum(numbers,dtype=np.uint64)
print(sum)
endtime=time.time()
time=endtime-starttime
print (time)
