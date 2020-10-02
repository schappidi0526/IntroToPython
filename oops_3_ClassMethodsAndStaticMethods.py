class Employee1():
    raise_amount=float(.04)
    num_of_reps=0
    def __init__(self,fname,lname,pay):#Self acts as an instance and fname,lname are arguments
        #Set the instance variables
        self.fname=fname# this is similar to above emp_1.fname='Satish'. 
        self.lname=lname
        self.pay=pay
        self.email=fname + '.' + lname +'@company.com'

        Employee1.num_of_reps +=1

    def fullname(self):
        return'{} {}'.format(self.fname,self.lname)

    def raise_apply(self):
        return self.pay+(self.pay*self.raise_amount)

    @classmethod
    def cls_raise_amt(cls,amount):
        cls.raise_amount=amount
    """ If you are working with instance you will use
    'self' and if you are working with class you will use 'cls' or any other. So any method
    which is not using self has to be defined as @classmethod """
    @classmethod
    def split_string(spt,emp_split_string):
        first,last,pay=emp_split_string.split('-')
        return spt(first,last,pay)

    @staticmethod
    def is_weekday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True

"""
The main difference between static method and class method you do not use 'self' in static method
"""
emp_1=Employee1('Satish','Chappidi',50000)
print (Employee1.num_of_reps)
emp_2=Employee1('Geetha','Banka',60000)
print (Employee1.num_of_reps)


Employee1.cls_raise_amt(1.05)
print (emp_1.__dict__,emp_1.raise_apply())
print (emp_2.__dict__,emp_2.raise_apply())

emp_1=Employee1.split_string('Satish-Chappidi-7000')
print(emp_1.fname)
print(emp_1.lname)
print(emp_1.pay)


from datetime import datetime 
emp_date=datetime(2020,9,27)
print (Employee1.is_weekday(emp_date))

import datetime 
emp_date=datetime.datetime(2020,9,27)
print (Employee1.is_weekday(emp_date))

"""

Applied the same functionality above
emp_str1= 'Satish-Chappidi-7000'
emp_str2='Geetha-Banka-8000'

first,last,pay=emp_str1.split('-')

emp_1=Employee1(first,last,pay)

print (emp_1.__dict__)"""

import datetime
print (datetime.datetime.now())

