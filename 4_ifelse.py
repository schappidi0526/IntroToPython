#exercise #1

number = 21

value = ""

if (number>0):
    value ='positive'
if (number<0):
    value = 'negative'
if (number==0):
    value = 'zero'

print (value)


#exercise #2

std1=13
std2=80
std3=10


if (std2>std1):
    if(std2>std3):
        print (std2)
    else:
        print (std3)
elif (std3>std1):
    if(std3>std2):
        print (std3)
    else:
        print (std2)
else :
    print (std1)


#exercise 3

student_1 = 21
student_2 = 19
student_3 = 29

oldest_student = ""

if (student_2>student_1):
    if(student_2>student_3):
       oldest_student= student_2
    else:
        oldest_student=student_3
elif (student_3>student_1):
    if(student_3>student_2):
       oldest_student = student_3
    else:
       oldest_student =student_2
else :
    oldest_student= student_1
    
print (oldest_student)