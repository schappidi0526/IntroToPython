Age= 23
print(Age)
print(id(Age))#Print the address of the variable
'''
if you have two variables with same values of data, Python will store it in the same
address which makes Python memory efficient
'''
a=10
b=a
print (id(a))
print (id(b))

print (type(Age))

#swap variables

age_1=22
age_2=23

temp_age_1=age_1
age_1=age_2
age_2=temp_age_1

print(age_2)
print(age_1)

#concat variables
a=input()
b=2
c=int(a)+b
print (c)

#TYpe conversion

age ='23'


print (int(age))

print (type(int(age)))


#Multiple assignments

age,weight=(23,175)

print(age)
print(weight)

# take variable value from before
y=10
x=y+9
z=_+10
print (z)