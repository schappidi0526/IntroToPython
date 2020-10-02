#Merge/Update dictionary

dict1={'Math':99,
        'science':98,
        'history':33}

dict2={'telugu':88,
        'hindi':77,
        'english':99,
        'Math':69}#If you have same keys in both dictionaries,values will be updated

dict1.update(dict2)
print (dict1)

dict2.update(dict1)
print(sorted(dict2.keys()))
print(sorted(dict2.values()))
#Delete keys in dictionary based on the keys

del dict1["hindi"]
print (dict1)

dict1.pop('english')
print (dict1)
#if you try to pop a key that doesn't exist, it will throw keyerror
# dict1.pop('hindi')
# print (dict1)


#clear all elements

dict1.clear()
print (dict1)

#get function
print (dict1.get('hindi'))
"""By default above will print 'None'. If a key doesn't exist and if you want to specify a 
value other than 'None'"""
print (dict1.get('hindi','Not found'))

#Add lists to dictionary
L1=[1,2,3,4,5]
count=['count1','count2','count3','count4','count5']
dict2={"l1":L1,
        "count":count}
print (dict2)

#Another way

d1=dict(zip(L1,count))

print (d1)


print (help())