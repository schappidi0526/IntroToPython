# #How many days till my next birthday
# from datetime import date,timedelta
# birthday=date(1988,8,17)
# print (birthday)
# today=date.today()

# print (today)

# birthday=birthday.replace(year=today.year)
# print (birthday)
# if birthday>today:
#     day=birthday-today
#     print('My upcoming birthday is in '+str(day) +'days')
# else:
#     birthday=birthday.replace(year=today.year+1)
#     day=birthday-today
#     print('My upcoming birthday is in '+str(day) +'days')

from datetime import date,timedelta,datetime
birthdate='1988-11-17'

#Convert birthdate to date
dobirthdate=datetime.strptime(birthdate,'%Y-%m-%d')
today=datetime.today()
print (today)

#Get year from today
tyear=today.year
print (tyear)

#replace the year from birthdate
Ubirthdate=dobirthdate.replace(year=tyear)
print (Ubirthdate)

if Ubirthdate<today:
    Ubirthdate1=Ubirthdate.replace(year=tyear+1)
    #strftime formats a date into a string
    strubirthdate1=Ubirthdate1.strftime('%Y-%m-%d')
    daydiff=Ubirthdate1-today
    print ('Days to my upcming birthday are' + str(daydiff)+' and the next birthday is'+strubirthdate1)
else:
    daydiff=Ubirthdate-today
    strubirthdate=Ubirthdate.strftime('%Y-%m-%d')
    print ('Days to my upcoming birthday are' + str(daydiff)+' and the next birthday is'+strubirthdate)