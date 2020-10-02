age_1 = 22
age_2 = 23

age_3=age_2
age_2=age_1
age_1=age_3
print(age_1,age_2)
print(age_2)


age = "23"

# As you can see from the double quotes, age is a string. convert age to an integer
age_int= int(age)

print (type(age_int))

number = 15

not number % 15


# characteristics of a probable candidate for a job opening
age = 21
qualification = "Bachelors"
experience = 2


if (age>=21 and (qualification=='Bachelors' or qualification=='Masters') and experience >=2):
    print('match')
else:
    print('not match')
    

# Let the variable "match" be a Logical variable. So, it takes a True or False.
# Write an if statement such that based on the following conditions the program should determine if the 
# candidate can be considered for a job interview or not. 

# The conditions are
# 1. candidates with at least an age of 21 and 
# 2. a qualification of either "Bachelors" or "Masters"  
# 3. and at least an experience of 2 years.


# match = 