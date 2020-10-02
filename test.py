# udemynames={'Father': 'SatishChappidi',
#             'Mother': 'GeethaBanka',
#             'Son': 'Virat Aditya'}

# #Keys should be unique. no duplicate keys allowed. Key values are hashed for uinqueness
# #if the key value exists, it will change the value
# udemynames['Father']='Chanti'
# #if the key vaue doesn't exist, it will add the key and value
# udemynames['Godfather']='buddy'
# #append a value to a key
# udemynames.get('Father').append('Harish')
# #if the key doesn't exist, the program stops when printing 
# print (udemynames)



l1=[10,20,30]
l2=l1
print (id(l1)==id(l2))
l2=l1.copy()
print (l2)
print (l1)
print (id(l1)==id(l2))