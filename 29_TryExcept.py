age=21
try:
    #age=age+"1"
    age = age/0
# except ZeroDivisionError:
#     print('cannot divide an integer by 0')
except SyntaxError:
    print('Somethind is wrong in the syntax')
except TypeError:
    print('cannot add integer with a string')
except KeyError:
    print('There is no valid key in dictionary')
# except Exception as e:
#     print (e)
except :#producing generic error
    print('This the generic error')
finally:
    print ('Exiting the program')