class Employee():
    raise_amount=float(.04)
    num_of_reps=0
    def __init__(self,fname,lname,pay):#Self acts as an instance and fname,lname are arguments
        #Set the instance variables
        self.fname=fname# this is similar to above emp_1.fname='Satish'. 
        self.lname=lname
        self.pay=pay
        self.email=fname + '.' + lname +'@company.com'

        Employee.num_of_reps +=1

    def fullname(self):
        return'{} {}'.format(self.fname,self.lname)

    def raise_apply(self):
        self.pay= self.pay+(self.pay*self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.fname,self.lname,self.pay)

    def __str__(self):
        return '{} - {} - {}'.format(self.fname,self.pay,self.raise_apply())
        #if you are calling a func it shld be in " () "

    def __add__(self,other):#add is an inbuilt function which adds values from two objects
        return self.pay+other.pay   

emp_1=Employee('Virat','Chappidi',2000)
emp_2=Employee('satish','Chappidi',12000)
print (emp_1+emp_2)

#Call particular function is the class
print (repr(emp_1))
print (str(emp_1))

#another type
print (emp_1.__repr__())
print (emp_1.__str__())
print (emp_1.pay)
print (emp_2.pay)
print (emp_1+emp_2)