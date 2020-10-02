# #print 10th odd number between 30 and 60
#Using flag variables

flag='True'
counter=0
#print(flag)
while flag=='True':
    for i in range(30,60):
        if i%2!=0:
            counter+=1
            #print (i)
            #print (counter)
            if counter==10:
                flag='False'
                #print (i)
                print ('10th odd number between 30 and 60 is ' + str(i))
        #print(flag)


#Using BREAK and for loop. This helps us to eliminate using flag variable
counter=0

for i in range(30,60):
    if i%2!=0:
        counter+=1
        print (counter)
    if counter==10:
        print ('10th odd number between 30 and 60 is ' + str(i))
        break

#using BREAK and while loop
counter=0
min=30
max=60
while True:
    #print (counter) 
    min=min+1
    if counter<10 and (min%2!=0):
        counter+=1           
        if (counter==10):
            print (min)
            print ('10th odd number between 30 and 60 is ' + str(min))
            break
    


