#Arithmatic Operators

marbles = 2
marbles = marbles +3
print (marbles)
#shortcut for marbles = marbles + 3
marbles += 3

print (marbles)

marbles -= 3

print (marbles)

marbles *= 3 

print (marbles)

marbles /= 3

print (int(marbles))


#Modulo division helps us to get the reminder

a=20
b=21

c=21%20

print (c)

#Floor division helps you to get quotient

x=40
y=45

z=y/x

print (z)

#Exponentiation

count = 2

print (count ** 3)

#Comparision operators

number = 15

not number / 15

#String multiplication
str='satish'
print (3 * str)

#raw string
print ('C:\docs\navin')
print (r'C:\docs\navin')

#Logical operators

age = 21
qualification = "Bachelors"
experience = 2


if (age>=21 and (qualification=='Bachelors' or qualification=='Masters') and experience >=2):
    print('match')
else:
    print('not match')