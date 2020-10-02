# #find the position of thesubstring
name='satish chappidi'
print (name.find('chappidi'))

string='Python is a hot language'
print (string.find('hot'))
print (string.find('not'))#if you select something which is not in the string it will give -1
#Lenght of string
print (len(string))

#split strings

name1='satish chappidi'
print(name1.split())

#Default is space but you can pass arguments with what you want to split

name2='satish kumar, chappidi'
print(name2.split(','))

#Stringstrpping

name3=' satish chappidi '
name4='satish chappidi'
name3=name3.strip()

print (name3 == name4)

#isalnum helps you to check if the string has any alpha numeric(no special characters) in it

name6='satish4'
print (name6.isalnum())

#isalpha(no numbers or special characters) checks if there are only characters in a string

name5='satishchappidi$@#?'
print(name5.isalpha())

name5='satishchappidi'
print(name5.isalpha())

#String concatenation

name1='satish'
name2='chappidi'
name=name1+' '+name2

print (name)

#Upper
name='satishchappidi'
print (name.upper())

#lowe
name='SATISH'
print(name.lower())

#IntialLetterCaps

name6='satish chappidi'
print(name6.title())
print(name6.capitalize())

#swapcase swaps upper case to lower case and vice versa
name='SatishChappidi'
print (name.swapcase())

#Isupper checks if the characters are uppercase
name='Satish'
print (name.isupper())

#Islower checks if the characters are lowercase
name='satish'
print (name.islower())

#reverse a string
#Using while loop
name7='satishchappidi'
lengthname7=len(name7)
print (lengthname7)
reversename7=''

while(lengthname7>0):
    reversename7+=name7[(lengthname7)-1]
    lengthname7-=1
print (reversename7)

#Using for loop
#name7=input()
name7='satishchappidi'
len7=len(name7)
rev7=''
for i in name7:
    var=name7[len7-1]
    rev7+=var
    len7-=1
print (rev7)


#Split a user entered string into its words printing each letter in capitals
name8='satish chappidi'
splituppername8=name8.split()
uppername8=''
print(splituppername8)

for word in splituppername8:
    capuppername8=word.capitalize()
    uppername8=uppername8+' '+capuppername8
print(uppername8.strip())
    #print(word)

#number of occurences of a character in a user entered string
#Using while loop
name9='virataditya'
keyword=input('enter the character you want to search:')
lengthname9=len(name9)
counter=0

while(lengthname9>0):
    if name9[lengthname9-1]==keyword:
        counter+=1
        lengthname9-=1
        
    else:
        lengthname9-=1
print ('the number of occurences of '+ str(keyword) + ' in ' + str(name9) +' is '+str(counter))

#Using for loop

name9='virataditya'
keyword=input('enter the character you want to search:')
counter=0
for i in name9:
    if i==keyword:
        counter+=1
print ('the number of occurences of '+ str(keyword) + ' in ' + str(name9) +' is '+str(counter))     






