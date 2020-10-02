#Using for loop

for i in range(2, 101) :
     # flag variable
    print (i)
    print(int((i)/2)+1)
    found_prime = True   
    for j in range(2,int((i)/2)+1) : 
        print(i) 
        print(j)
        if i % j == 0 : 
            print ( "number ", i , " is not prime")
            found_prime = False
            break
           
    if found_prime == True :
        print ( "number ",i, " is prime" )
        found_prime = True

#Using for else
for i in range(2,101) :
    for j in range(2,int(i/2)+1) :
        if i % j == 0 :
            print ( i, " is not prime number")
            break
    else :
        print ( i, " is a prime number")
