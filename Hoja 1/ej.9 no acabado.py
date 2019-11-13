



usuario = input('normal/inversa')


print('conversion normal')

hora= int(input('Escribe una hora  '))

print('conversor')
minutos= 60
segundos= 3600


resultado =  (minutos / hora) * segundos


if usuario == "normal":
    print(resultado)


print('conversion inversa')


hora1= int(input('Escribe una hora  '))

print('conversor')
minutos1= 60
segundos1= 3600


resultado1 =  (hora1 * minutos1 ) * segundos1


if usuario == "inversa":
    print(resultado1)
