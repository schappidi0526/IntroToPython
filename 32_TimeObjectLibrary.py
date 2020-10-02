
#Time
from datetime import time
time=time(5,8,7,32000)
print(time)

#To print current time
from datetime import datetime
t=datetime.now().time()
print(t)



"""this is a different kind of time which will help us to find the number of seconds
from Jan 1st,1970(epoch time: All computers will have a chip in them with this date)"""
import time
now=time.time()
print(now)
#time.time will be used in order to calculcate how long a process is taking to run
#For example, below
import time
before=time.time()
sum=0
for i in range(1000000):
    sum=sum+1
after=time.time()
time=after-before
print(time)

