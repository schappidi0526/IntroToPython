#Below classes are not inherting any methods. They are just parent and child classes

class x:

    def show(self):
        print ('A in show')

class y:
    pass
#======================================================

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
        self.pay= self.pay+(self.pay*self.raise_amount)

class Developer(Employee1):
    raise_amount=float(.1)#Overwriting the raise amount in parent class
   
    def __init__(self,fname,lname,pay,prog_lang):
        super().__init__(fname,lname,pay)
        """Employee1.__init__(self,fname,lname,pay)--Another way of initiating from super class"""
        self.prog_lang=prog_lang

class Manager(Employee1):
    def __init__(self,fname,lname,pay,employees=None):
        super().__init__(fname,lname,pay)
        if employees==None:
            self.employees=[]
        else:
            self.employees=employees
    #add employees
    def addemployee(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)
    #remove employees
    def removeemployee(self,employee):
        if employee in self.employees:
            self.employees.remove(employee)
    #print employees
    def printemployees(self):
        for employee in self.employees:
            print ('-->', employee.fullname())

dev_1=Developer('Satish','chappidi',9000,'Python')
dev_2=Developer('john','cao',4000,'Python')
print (dev_1.__dict__)
#print (help(dev_1))#Gives you information of whats happening 

# print (dev_1.pay)
# dev_1.raise_apply()
# print(dev_1.pay)
mgr_1=Manager('Geetha','Banka',90000,[dev_1])
print (mgr_1.fname)
mgr_1.raise_apply()
print (mgr_1.pay)
mgr_1.printemployees()
print ('1')
#add one more employee
mgr_1.addemployee(dev_2)
mgr_1.printemployees()
#remove an employee
mgr_1.removeemployee(dev_1)
mgr_1.printemployees()


print (isinstance(mgr_1,Manager))#True
print (isinstance(mgr_1,Employee1))#True
print (isinstance(mgr_1,Developer))#False

print (issubclass(Developer,Employee1))#true
print (issubclass(Developer,Manager))#false
"""
    if you do not have a init in sub class, when you call a method in sub class, it will check
    the sub class for init function, if it cant find anything in there then it will go the 
    parent class's init function
    """
"""
Multi Level Inheritance is inherting methods from two different methods
"""
class a:
    def __init__(self):
        print ("A feature")

    def feature(self):
        print ("feature a")
class b:
    def __init__(self):
        print ("B feature")
    def feature(self):
        print ("feature b")
class c(b,a):
    
    def __init__(self):
        super().__init__()
        """ 
        when you are inheriting from two classes and you want inherit methods from both, the precedence will be given to
        the left class when initializing (class c(a,b)). This concept is called Method resolution order(MRO). The same concept applies
        for methods as well. If you have two functions with the same , the method from left class will be given precedence
        """
        print ("c feature")

c1=c()

print (c1.feature())