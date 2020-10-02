'''The primary use of sets is to perform operations like Intersect,Union and difference
    Sets can only have one distinct element. There is no ordering in sets 
    and No index based process
'''

Set1={'snowy','windy','sunny','sunny','windy','windy'}
#Add element to a set
Set1.add('fall')
print (Set1)
#remove a random element from a set
Set1.pop()
print (Set1)
#remove a particular element from  a set
Set1.remove('windy')
print (Set1)
#Clear a set
Set1.clear()
print (Set1)
#Remove a particular element without erroring out if it is not available
print(Set1.discard('windy'))
#deleting the set
del Set1
print (Set1)
#Creating an empty set

set1=set()

print (type(set1))

