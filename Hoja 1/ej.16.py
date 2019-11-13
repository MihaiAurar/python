array=[0] *20

for i in range(20):
    array[i]=int(input("escribe de nuevo  "))

    
res=0

for a in array:
    res = res + array[a]

rest = res/20

print(rest)


        
