
num= int(input("introduce un numero"))

def division(num):
    if num == 0:
        return 1
    else:
        return num * division(num-1)
    
print(division(num))
    
