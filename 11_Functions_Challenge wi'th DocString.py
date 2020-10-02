#Find the nthvalue in a fibinocci series

def fibinocci(n):
    previousnumber=0
    currentnumber=1
    strn=str(n)
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



nth=fibinocci(15)
print(nth)


#sum of numbers divisible by 5 between two numbers

def sum_numbers(startnumber,endnumber):
    sumofnumbers=0
    setofnumbers=range(startnumber,endnumber)
    for number in setofnumbers:
        if(number%5==0):
            sumofnumbers=sumofnumbers+number
    return sumofnumbers


sumof=sum_numbers(1,11)
print(sumof)

#Write a function to find the average for grades and return sum and average of grades.
#ctrl+space to display the docstring when assigning values to the functions arguments

def avg_grades(*grades):#'*' meaning user can provide any number of grades
    """
    //Provide the list of grades to calcualte the sum and average of//
    example:grades=3,4,5
    """
    i=0
    sumofgrades=0.0
    for grade in grades:
        sumofgrades=grade+sumofgrades
        i=i+1
    avggrades=sumofgrades/i
    return avggrades,sumofgrades
        
avg=avg_grades(3,4,5)
print(avg)

