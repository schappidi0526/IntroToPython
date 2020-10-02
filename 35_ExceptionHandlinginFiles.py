#File handling using try except finally blocks 

try:
    f=open('C:/Users/kumar/Downloads/Ahmed_Intro.txt','w')
    1/0
except:
    print ('Exception has occured')
finally:
    f.close()

#'with' helps to do the same operation as exception handling.
#It makes sure that the file is closed if the operation is failed 
with open('C:/Users/kumar/Downloads/Ahmed_Intro.txt','w') as f:
    result=1/0
    f.write('a new line in the file')
print(f.closed)