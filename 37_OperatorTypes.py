#Compliment
print (~12)# this will print -13 because the binary number is same for 12 and -13

#bitwise operators->Works as binary numbers
#Bitwise AND
print (12 & 13)#12
"""it will print 12 as you need to check by bits of corresponding binary numbers and when
you say and those bits should be same comparing respective bits"""
#bitwise OR
print (12 | 13)# will print 13
#XOR-> if both numbers are different then it is '1'
print (12 ^ 13)# will print '1'
#right Shift-> this will shift binary decimals two places right(adding 00) which will give 5
a = 20
print (a >> 2)
#left shift--> this will shift binary decimals two places left(removing two bits from '.') which will give 5
b=12
print (b<<2)


# a=[1]
# b=a
# print (b)
# print (b[0])
# print (a[0])
# a[0]=0
# a.append(1)
# print (a)

# print (a[0])
# print (b[0])

a=[0]
b=a
a[0]=1

print (a)
print (b)
print (len(a))
print (len(b))

a=[1,2,3,4]
a1=a[-3:-2]
a2=a[2:3]
print (a1)
print (a2)

#Unaryoperator--we may also call it as negation operator

n=7
print (-n)

#Relational operators->'>,<,==<<=,>='

#logical operators->'and,or,NOT'
x=True
print (not x)
