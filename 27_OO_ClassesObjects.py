
''' Classes can hold variables and methods to perform action based on the values of the variables'''


"""Class is a blueprint and object is the house. There can be 
multiple objects in a class"""

class Account:
    percentage=8  #class variable. It doesn't change with each object
    def __init__ (self, number):#'__init__' is a function which helps to initialize a class
        '''whenever you are using 'self' you are trying to create object variable. It says
            that each object which accesses this class will have a separate accountnumber value'''
        self.account_number = number #Instance variable
#Class has been created



    def account_type(self):
        if str(self.account_number).startswith("1"):
            self.type='Checking'#dynamically creating an instance variable
        elif str(self.account_number).startswith("2"):
            self.type='Saving'
        return self.type
    def interest_rate(self):
        self.account_type()#call a method from inside another method
        if self.type=='Checking':
            self.rate=1
        elif self.type=='Saving':
            self.rate=5
        return self.rate


acc = Account(2001)#acc is object and Account is class


# acc1 =Account(1002)
# print (acc1.account_number)
# print (acc1.percentage)
print (acc.account_type())
print (acc.interest_rate())

print (acc.__class__)#gives the class of the object

print (isinstance(acc,Account))

#Print output from a Class

class Account1:
    def __init__ (self,number,name,balance):
        self.account_number=number
        self.account_name=name
        self.account_balance=balance
    def __str__(self):#Only when you invoke this,function will return strings
        return 'The balance in ' + str(self.account_name) + "'s account is " + str(self.account_balance)
acc = Account1(1001,'Satish',100.00)

print (acc)