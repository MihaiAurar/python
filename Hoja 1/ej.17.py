   

def mifuncion(numero):
    contador=0
    for i in range(1,numero+1):
        if numero%i==0:
            contador = contador+1
    if contador>2:
        print(numero, "no es primo")
    else:
        print(numero, "es primo")

for i in range(1,54):
    mifuncion(i)


        
