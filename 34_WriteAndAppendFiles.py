#Read a picture
f=open('C:\\Users\\kumar\\OneDrive\\Desktop\\Satish.jpg','rb')#rb is for read binary
#print (f.read())#you will get the o/p in binary format
data=f.read()
#Write data into a new file
fw=open('C:\\Users\\kumar\\OneDrive\\Desktop\\Satish_09112020.jpg','wb')
fw.write(data)
fw.close()#We have to close the file after each write as the operation will block the file to open
          
""" On a usual scenario Write operation deletes the exisitng data from the file and writes data 
    into it. Thats where append comes into place"""
#Write
f=open('C:/Users/kumar/Downloads/Ahmed_Intro.txt','w')
# print (f.read())
f.write('A dummy dialog')
f.close()
#Append
f=open('C:/Users/kumar/Downloads/Ahmed_Intro.txt','a')
f.write('\nA double dummy dialog')
f.close()

#copy data from one file to another file

f=open('Mydata','r')

f1=open('copydata','r')

for data in f:
    f1.write(data)
