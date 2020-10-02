grades={'Math': 100,
        'Science': 80,
        'History': 60,
        'English': 50}

grades['Biology']=70
#To print just keys
for key in grades:
    print(key)
#To print keys along with their values
for key in grades:
    print(key,grades[key])

for key in grades.keys():
    print(key,grades[key])
#To print values from a dictionary
for value in grades.values():
    print (value)


#keys and values are dynamic objects and read only. When the dict changes these will change
values=grades.values()
keys=grades.keys()
print (sorted(keys))
print (sorted(values))


#to make changes to the keys
"""though keys structure appear to be as lists but those
are not lists, we need to convert to list to make changes"""
keys_l=list(keys)
keys_l.append('Zoology')
print(keys_l)


