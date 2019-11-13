print('conversor de moneda')

cash= int(input('introduce una cantidad'))
dinero = input('euro/dolar')

euro = 1.15

dolar = 2


resultado = cash * euro

resultado2 = cash * dolar

if dinero == "euro":
    print(resultado)

elif dinero == "dolar":
    print(resultado2)
