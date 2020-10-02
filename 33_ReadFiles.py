"""
Syntax
f=open('filepath','mode')
(Types of modes:
'r'-read,
'w'-write,
'a'-append,
'x'-exclusive right,
'b'-binary mode,
'+'-read and write
)"""

f=open('C:\\Users\\kumar\\Downloads\\Ahmed_Intro.txt','r')
print (f)#Type of f
print (f.read())#Reads all the data in the file
# #Readline reads data line by line from the file. you cannot use readline after you use f.read()
# #YOu will have to open the file again
f=open('C:/Users/kumar/Downloads/Ahmed_Intro.txt','r')#Either you give'/' or two'\\' when specifying path
#f is the pointer in above lien
print (f.readline())
print (f.readline())
print (f.readline())
print (f.readline())

#Print each line in a for loop
f=open('C:\\Users\\kumar\\Downloads\\Ahmed_Intro.txt','r')
for line in f:
    print(line)
