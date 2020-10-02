class student:

    def __init__(self,name,age,brand,cpu,ram):
        self.name=name
        self.age=age
        self.lap=self.Laptop(brand,cpu,ram)

    def show(self):
        print (self.name,self.age)
        print ('1')
        self.lap.show()
    
    class Laptop:

        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        #The object of inner class has to be defined in outer class

        def show(self):
            print (self.brand,self.cpu,self.ram)

s1=student('virat',3,'Hp','i5','16gb')

print (s1.show())
#call inside class variable



print (s1.lap.brand)

"""
You can call an inner class inside the outer class
or
You can call an inner class outside the outer class provided you use outer class name to
call it"""

lap1=student.Laptop('Hp','i5','16gb') 

print (lap1.brand,lap1.cpu,lap1.ram)

