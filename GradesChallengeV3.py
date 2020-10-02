grades=[]

while True:
    print('Enter your choice ->')
    print('Enter the grades - 1')
    print('List the grades - 2')
    print('Delete grades from the list - 3')
    print('Update the grades from the list - 4')
    print('Clear grades - 5')
    print('Calculate the average of grades - 6')
    print('Exit the program - 7') 

    choice = input('-> ')
    #intchoice = print (int(choice))
    #print (intchoice)
    if not len(choice)==1 and choice.isnumeric:
        print('Enter a valid choice ')
        continue
    if int(choice) == 7:
            break
    if int(choice)==1:
        print('Enter grades. e to exit')
        while True:
            grade=input('->')
            if grade=='e':
                break
            else:
                grade= float(grade)
                grades.append(grade)
    if int(choice)==2:
        for grade in grades:
            print(grade)
    if int(choice)==3:
        for grade in grades:
            print(grade)
        index=int(input('Enter the index of grade you want to delete:'))
        if(index<len(grades)-1) and index>=0:
            grades.pop(index)
        else:
            print('Invalid index. Please enter valid index')
    if int(choice)==4:
        for grade in grades:
            print(grade)
        updateindex=int(input('Enter the index of grade you want to update:   e to exit'))
        
        if(updateindex<len(grades)-1) and updateindex>=0:
            updatevalue=float(input('Enter the value you want to enter in '+str(updateindex) +' index '))
            #below is what I had
            #grades.pop(updateindex)
            #grades.insert(updateindex,updatevalue)
            grades[updateindex]=updatevalue
    if int(choice)==5:
        grades.clear()
    if int(choice)==6:
        sum=0.0
        avg=0.0
        for grade in grades:
            print(grade)
            sum+=grade
            print('sum of grades is '+str(sum))
            avg=sum/(len(grades))
        print('average of grades is'+ str(avg))


            