""" There are four objects in DATETIME module. DATE,TIME,TIMEDELTA,DATETIME.
DATETIME combines both DATE and TIME modules"""

from datetime import date# from the datetime module import only date object
t=date.today()
print(t)
print (t.day)
print (t.month)
print (t.year)

#manually enter year,month and date
t1=date(2019,8,17)
print (t1)
#Replace date from t
t=t.replace(day=10)
print(t)
t=t.replace(year=2019)
print (t)
#print weekday of the date. Monday starts with '0'
print(t.weekday())

print (t1.weekday())
#strftime is used to format the date into string
st=t.strftime('%m-%d-%Y:%a')
print (st)
st1=t1.strftime('%m-%d-%Y')
print (st1)
st2=t.strftime('%b-%d-%y')
print (st2)
st3=t.strftime("%b '%d")#If you want to separate with " ' "
print (st3)
print (t)
print (t.strftime("%W"))

t=date(2019,1,7)# The order should be year,month and date
t1=date(2019,2,7)
t2=t-t1
print (t2)

#strptime is used to format string into date
from datetime import datetime
st1=input('Enter the date in yyyy-mm-dd format:')
sp=datetime.strptime(st1,'%Y-%m-%d')
print(1)
print (sp)
print (2)
""" You can only add days,weeks to current date. 
    You cannot add or subtract months and years from timedelta"""
from datetime import date,timedelta

today=date.today()
tomorrow=today+timedelta(days=1)
print (tomorrow)
"""Below will error out
NextYear=today+timedelta(year=-1)
print (NextYear)"""
oneweeklater=today+timedelta(weeks=1)
print (oneweeklater)
print(type(oneweeklater))
oneweekprior=today-timedelta(weeks=1)
print (oneweekprior)


#SUbtract days to current date
yesterday=today-timedelta(days=1)
print(yesterday)

days=today-yesterday
print(type(days))


""" Types of outputs for date operations

timedelta=date_1-date_2
date_2=date_1+timedelta
date_2=date_1-timedelta
boolean=date_1>date_2
"""
"""Datetime object is the combination of date and time"""

import datetime
dt=datetime.datetime.now()
print (dt)

#Construct a datetime parameter
import datetime
dtime=datetime.datetime(1988,8,17,12,34,56,3400)
print (dtime)
dtime1=datetime.datetime(1988,8,17)# it will take even if you give just the data params
print (dtime1)