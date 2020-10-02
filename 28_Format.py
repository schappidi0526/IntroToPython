#Format

text='Satish is {} years old'
text_1 = text.format(2)
print (text_1)

text_2='{} is a {} company'.format('ajaytech','software')

print (text_2)

text_3='{1} is a {0} company'.format('software','ajaytech')
print (text_3)


text_4='{Name} is a {group} company'.format(group='software',Name='ajaytech')
print (text_4)

#Format in indentation
population = {'India' :  13000000,
                'China': 14000000,
                'US' : 300000}

for key in population:
    print (key,population[key])
    print ("{:<10} - {:>10}".format(key,population[key]))

india='The population of india is {:,}'.format(136764748)

print(india)