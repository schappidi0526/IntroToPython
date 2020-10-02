#MixedLists

Mixedlist=[2,'Satish',5.11]
print (Mixedlist)
print (type(Mixedlist[0]))

#NestedLists

nestedlist=[Mixedlist,76.5,'NewYork']
print (nestedlist)
print (type(nestedlist[0]))

#Enumerator

grades=[3.0,4.0,5.0]

for grade in grades:
    print(grade)
#Helps you to get values along with the indexes
enum_grades=enumerate(grades)

for index,grade in enum_grades:
    print (index,grade)

#Why do we need an enumerator
#Suppose I want to skip every 3rd index in a list

list1=[1,2,3,4,5,6,7,8,9]

enumlist=enumerate(list1)

for index,listitem in enumlist:
    if ((index+1)%3)!=0:
        print (index,listitem)


#Combine and sorts lists

list_1=[1,2,3,4,5]
list_2=[11,13,8,9]
list_3=list_1+list_2
print (list_3)
list_3.sort()
print (list_3)

#List slice

print (list_3[3:5])
print (list_3[0:5])
print (list_3[5:])

a=[1,2,3,4]
a1=a[-3:-2]
a2=a[2:3]
print (a1)


#Add multiple values into a list

a1.extend([9,10])
print (a1)

