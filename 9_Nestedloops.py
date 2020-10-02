for i in range(1,11):
    for j in range(0,i):
        print (i, end=" ")
    print()


#Print 10th odd number between 30 and 60
flag='True'
counter=0
#print(flag)
while flag=='True':
    #print(flag)
    for i in range(30,60):
        if i%2!=0:
            counter+=1
            #print (counter)
            if counter==10:
                flag='False'
                print ('10th odd number between 30 and 60 is ' + str(i))
#print(flag)