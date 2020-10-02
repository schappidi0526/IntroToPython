#sum of alternate odd numbers till that point 

def oddnumbers(n):
    oddrange=range(1,n)
    oddlist=[]
    alternateoddlist=[]
    sumoflaternumbers=0
    for number in oddrange:
        rem=number%2
        if rem!=0:
            oddlist.append(number)
    lenoddlist=len(oddlist)
    oddlistrange=range(0,lenoddlist)
    for oddindex in oddlistrange:
        remodd=oddindex%2
        if remodd==0:
            alternateoddlist.append(oddlist[oddindex])
    for alternumber in range(0,len(alternateoddlist)):
        sumoflaternumbers=alternateoddlist[alternumber]+sumoflaternumbers

    print(len(alternateoddlist))
    return sumoflaternumbers



odd=oddnumbers(10)
print (odd)

#Return the first prime number between a given range of numbers

def first_prime (number_1, number_2) :
    firstprime=0
    divisionrange=range(2,6)
    
    primerange=range(number_1,number_2)
    for number in primerange:
        divisioncount=0
        #print ('firstprime'+str(firstprime))
        #print(number)
        for divisionnumber in divisionrange:
            #print('divisionnumber'+str(divisionnumber))
            if(number%divisionnumber!=0 and firstprime==0):
                divisioncount+=1
                #print ('divisioncount'+str(divisioncount))
                if(divisioncount>=4):
                    #print('number'+str(number))
                    firstprime=number
    return firstprime



# prime=first_prime(15,20)
# print(prime)


# def reverse (name):
#     #inputname=name
#     lenname=len(name)
#     lennamedup=lenname
#     counter=0
#     #print (name[lenname])
#     string1=""
#     while(counter<int(lennamedup)):
#         #print (name[lenname-1])
#         string1+= name[lenname-1]
#         counter+=1
#         lenname-=1    
        
#     return string1

# reversename=reverse('satish')
# print (reversename)


# #Create a function which takes two arguments and prints in format 'a|b a-b a|b a-b a|b a-b a|b a-b'

# def pattern(str_1,str_2):
#     counter=5
#     count=0
#     string=''
#     while(count<counter):
#         string+=' '+str_1+'|'+str_2+' '+str_1+'-'+str_2 
#         count=count+1
#     return string.lstrip(' ')

# str=pattern('a','b')
# print (str)


def alternate_odd(n):
    oddlist=[]
    #sumodd=0
    for number in range(0,n+1):
        if (number%2!=0):
            oddlist.append(number)
    for n in oddlist:
    return oddlist


sum=alternate_odd(10)
print (sum)