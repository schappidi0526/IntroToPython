#add grades to the list 

grades=[]

while True:#this will be true for infinite time unless you use break
    grade=input('enter grade: ')

    if grade=='e': #Infirte loop will exit if value='e' followed by break
        break
    else:
        grade=float(grade)
        grades.append(grade)
        

print (grades)
grades[1]=2.3#replace second index in the list 
print (grades)

#Find how many vowels are there in a given list

Sentence = input("enter the sentence:")

vowelslist=['a','e','i','o','u']
vowels_count=0

for i in list(Sentence):#you can convert a string into a list this way only when iterating
    if i in vowelslist:
        vowels_count+=1

print ('The number of vowels in the sentence is '+str(vowels_count))


#Merge two lists into one

list_1=[1,2,3]
list_2=[4,5,6]
list_1=list_1.extend(list_2)
print (list_1)

#ListIndexing

List=[1,2,3,5,9,6,7]
#Postive indexing starts with 0
print(List[2])
#negative indexing starts with -1 from the last and follows
print (List[-2])
#insert elements into a list(3 is the index and 4 is the element)
List.insert(3,4)
print (List)
#By default pop removes the last element
List.pop()
print(List)
#Specify the index position on which you want to remove
List.pop(4)
print(List)
#remove goes by value
List.remove(9)
print(List)

List.append(4)
print(List)
#If we have two same values in the list, it will remove the first occurence
List.remove(4)
print(List)
#Clear the list
List.clear()
print(List)