año=int(input("introduce un año"))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("es bisiesto")
        else:
            print(" es año no bisiesto")
    else:
        print("es bisieto")
else:
    print("no es año bisieto")
