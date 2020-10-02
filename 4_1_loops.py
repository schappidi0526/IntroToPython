#forloop

numbers = range(0,11)

for number in numbers:
    print (number)

#while loop

Numbers=[1,2,3,4,5,6,7]
print (len(Numbers))
indexid=0

while indexid<len(Numbers):
    print (Numbers[indexid])
    indexid=indexid+1

# Find all the odd numbers between 1 and 20. Append them to a string with spaces in between. 
# Like so


Numbers= range(0,20)
odd_numbers=''

for number in Numbers:
    cat=number%2
    if int(cat)>0:
        odd_numbers=odd_numbers+str(number) + ' '
print (odd_numbers.strip())

#this is working here but not in the udemy class note
# Numbers= range(0,20)
# odd_numbers=[]
# cat=0.0

# #print (cat)

# for number in Numbers:
#     cat=number%2
#     print ("for " + str(number) + " reminder is "+str(cat))
#     print (cat)
#     if int(cat)>0:
#         odd_numbers.append(number)
# #print (odd_numbers)
# odd_numbers_str=str(odd_numbers[0])+' '+str(odd_numbers[1])+' '+str(odd_numbers[2])+' '+str(odd_numbers[3])+' '+str(odd_numbers[4])+' '+str(odd_numbers[5])+' '+str(odd_numbers[6])+' '+str(odd_numbers[7])+' '+str(odd_numbers[8])+' '+str(odd_numbers[9])
# print (odd_numbers_str)