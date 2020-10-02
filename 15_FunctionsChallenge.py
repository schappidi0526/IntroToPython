#sum of alternate odd numbers till that point 

# def alternate_odd (n) :
    
#     oddlist=[]
#     alternateindex=[]
#     sum=0
#     for i in range(1,n+1):
#         if(i%2!=0):
#             oddlist.append(i)
#     for index in oddlist[::2]:
#         alternateindex.append(index)
#     for num in alternateindex:
#         sum+=num
#     return sum

# print (alternate_odd(5))


#First prime number between a given range of numbers
number_1=10
number_2=20 
firstprime=0
for num in range(number_1,number_2):
    divisioncount=0
    for div in range(2,6):            
        if(num%div!=0):
            divisioncount+=1
            #print (divisioncount)
            #break
    if (divisioncount>=4):
        firstprime=num
        print(firstprime)
        break
  

