Dict={"Math":3.0,
    "Physics":4.0}

print (Dict)

Dict['English']=3.0
print (Dict)
"""Key values in Dictionaries are supposed to be unique.
If you try to add keys and values for existing keys. 
It will just override existing value of the key """

Dict['Math']=2.0
#To get a value of a key
print (Dict['Math'])
#If you try to print a value of non existing key, it will throw 'KeyError'

print (Dict['telugu'])

#If you want to check without thrwoing error, Use the get method which will return 'None'
print (Dict.get('telugu'))

