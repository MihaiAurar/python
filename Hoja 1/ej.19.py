   

numero = int(input("escribe un numero"))


resultado={}

for i in range (numero, numero +1):
    resultado[i]=(i*(i+1)/2)
    

for i in resultado:
    print (resultado [i] )
