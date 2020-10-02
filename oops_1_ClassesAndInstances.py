#Create a blank class
class Employee():
    pass

emp_1=Employee()
emp_2=Employee()

emp_1.fname='Satish'
emp_1.lname='Chappidi'

emp_2.fname='Geetha'
emp_2.lname='Banka'

print (emp_1.fname)
print (emp_1.lname)

#Initialize values to a class
class Employee1():

    def __init__(self,fname,lname):#Self acts as an instance and fname,lname are arguments
        #Set the instance variables
        self.fname=fname# this is similar to above emp_1.fname='Satish'. 
        self.lname=lname
        self.email=fname + '.' + lname +'@company.com'

    def fullname(self):
        return'{} {}'.format(self.fname,self.lname)

emp_1=Employee1('Virat','Chappidi')
print (emp_1.fullname())

# print ('{} {}'.format(emp_1.fname,emp_1.lname))
# print('{fname} {lname}'.format(fname=emp_1.fname,lname=emp_1.lname))