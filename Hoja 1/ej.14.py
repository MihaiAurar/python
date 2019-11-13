
esc = int(input("escribe un numero"))

def abs(esc):
    if esc < 0:
       return esc * -1
    elif esc > 0:
       return esc

    else:
       return 0

print(abs(esc))
