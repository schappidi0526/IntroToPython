#sum of numbers from 1 to 1000
numbers=range(1,1001)

sumofNumbers=0

while sumofNumbers<=1000:
    for number in numbers:
        sumofNumbers=int(sumofNumbers)+int(number)

print (sumofNumbers)

#FInd the odd numbers between 1 to 20
Numbers= range(0,20)
odd_numbers=''

for number in Numbers:
    if int(number%2)>0:
        odd_numbers=odd_numbers+str(number) + ' '
print (odd_numbers.strip())

#print numbers 1 to 10 in reverse order using for and while loop
#my answer
maxnumber=10
minnumber=1

while (maxnumber>=minnumber):
    print (maxnumber)
    maxnumber=maxnumber-1

#Ajay's answer
#1
for number in range(10):
    print (10-number)
#2
for number in range(10,0,-1):
    print (number)
#print the first 10 numbers in fibinocci series

#Using for loop
previousnumber=0
currentnumber=1


for r in range(10):
    print(previousnumber)
    nextnumber=currentnumber+previousnumber
    previousnumber=currentnumber
    currentnumber=nextnumber

#Using while loop
previousnumber=0
currentnumber=1
count=0

while count<10:
    print(previousnumber)
    nextnumber=currentnumber+previousnumber
    previousnumber=currentnumber
    currentnumber=nextnumber
    count+=1

#print all the numbers multiple by 5 until 100
#Using while loop
maxnumber_1=100
minnumber_1=1
while (minnumber_1<=maxnumber_1):
    reminder=minnumber_1%5
    if int(reminder)==0:
        print(minnumber_1)
    minnumber_1=minnumber_1+1

#Using for loop

for number in range(100):
    if int(number%5==0):
        print(number)


    








