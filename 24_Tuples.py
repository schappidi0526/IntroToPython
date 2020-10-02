"""Tuples are immutable and cannot be changes. They are just snippets of data.
    you cannot make any changes to tuples. Tuples are used to store small amounts of data
    while Lists are used to store large amounts of data"""

#Tuple
Person_1=('Satish',33,'NewYork')

#Creating a tuple with a single element

Person_2=('Virat')

print (type(Person_2))#Produces string

Person_3=('virat',)

print(type(Person_3))

#Converting a list into a tuple

list1=['Satish',33,'NewYork']
tuple1=tuple(list1)

print(tuple1)

#Indexing in tuples is same as in list
print(tuple1[0])
#converting a tuple into a list

list1=list(tuple1)

print (list1)
#slicing in tulpes
print (tuple1[:2])
print(tuple1[-3:])

"""You cannot alter values inside a tuple. But You can alter values inside a tuple if the
values are in list. """

tuple2=([1,2,3],[4,5,6])#you cannot change[1,2,3] to [2,3,4] which means you are changing the value

tuple2[0][1]=2.1

print(tuple2)


"""Advantages of tuples over lists
    1) Since tuples are immutable,it is easy to process tuples in loops
    2) Since tuples cannot be overwritten i.e., write protected,so it can used to hold data 
        which are global in nature
"""
#COunt method tells you the number of occurences of a value in a tuple

tuple3=(1,2,3,3,4,4,5,6,3,2)

print (tuple3.count(3))

#index method gives you the first occurence of a value in a tuple
print (tuple3.index(3))

#delete a tuple
del(tuple3)


tuple4=('accc','bxxx','cbbb')

print (min(tuple4))

print (max(tuple4))


#Filter method

ages=(4,5,7,3,4,7,8,5,8,5,11,15,13)


def primaryages(age):
    if 11>=age>=5:
        return True
    else:
        return False

primaryschoolages= filter(primaryages,ages)

print (type(primaryschoolages))

for age in primaryschoolages:
    print (age)

