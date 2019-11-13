print('edad del usuario')


edad= int(input('que edad tienes  '))

print('cumpleaños')
cumple= int(input('dia cumple  '))
cumple2= int(input('mes cumple  '))


print('fecha actual  ')
dia= int(input('dia  '))
mes= int(input('mes  '))
año= int(input('año' ))

resta = año - edad 

if cumple >= dia & cumple2 >= mes:
    print(resta)
else:
    print(resta-1)
    



