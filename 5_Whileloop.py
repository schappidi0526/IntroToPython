user_floor=6
current_floor=0
while user_floor!='exit':
    difference=user_floor-current_floor
    if difference>0:
        print ('Move up')
    elif difference<0:
        print ('Move down')
    elif difference==0:
        print('Open the door')
    current_floor=user_floor
    user_floor=input()
    if user_floor!='exit':
        user_floor=int(user_floor)