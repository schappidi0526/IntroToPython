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



emp_1=Employee1('Satish','Chappidi',50000)
print (Employee1.num_of_reps)
emp_2=Employee1('Geetha','Banka',560000)
print (Employee1.num_of_reps)
Employee1.raise_amount=float(.08)#Overwrite the raise_amount 
print (emp_1.fullname(),emp_1.pay+(emp_1.pay*emp_1.raise_amount))
print (emp_1.fullname(),emp_1.raise_apply())
print (emp_1.__dict__)#prints everything belonging to that instance


