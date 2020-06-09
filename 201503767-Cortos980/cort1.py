# CORTO 1 (SECUENCIA COLLATZ )

carne = 201503767 #numero de carne establecido

print(carne)

while carne != 1:                           #Mientras el numero sea diferente a 1
    if carne % 2 == 0:                      #condificinal de modulo para verificar si es un numero par     
        print("%d," % (carne), end = "")    #Organizacion de los datos 
        carne = carne / 2                   #como es un numero par se divide entre 2 
    else:                                   # sino es un numero par entonces
        print("%d," % (carne), end = "")    #Organizacion de los datos 
        carne = (carne * 3) + 1             #multiplicacion de numero par     
    if carne == 1:
        print("1")
    
        
