#Find the nth Fibinocci number
def fib(n):
    previousnumber=0
    currentnumber=1
    #strn=str(n)
    i=2
    if(n>2):
        while(i<n):
            nextnumber=previousnumber+currentnumber
            previousnumber=currentnumber
            currentnumber=nextnumber        
            i=i+1
            #print (nextnumber)
        return nextnumber   
    elif(n==1):
        nextnumber=0
        return nextnumber   
    else:
        nextnumber=1
        return nextnumber   

print (fib(8))

#Write a function that takes in 2 numbers. Find out all the numbers divisible by 5 between those numbers and add them up. Return the sum.

def sum_numbers(startnumber,endnumber):
    sumofnumbers=0
    setofnumbers=range(startnumber,endnumber)
    for number in setofnumbers:
        if(number%5==0):
            sumofnumbers=sumofnumbers+number
    return sumofnumbers