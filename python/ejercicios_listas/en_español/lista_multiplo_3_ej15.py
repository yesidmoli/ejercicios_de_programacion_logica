"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántos datos
almacenados son múltiplos de 3."""

try:
    numeros = [] #creamos la lista para almacenar los numeros ingresados
    cont = 0
    
    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        numeros.append(int(input("Ingrese un numero entero "))) #solicitamos y agregamos los numeros  a la lista

        if numeros[i] % 3 == 0: #condicionamos para saber cuales numeros son multiplos de 3
        	cont += 1 #contamos cauntos son

    print(f"En la lista hay {cont} datos que son multiplos de 3")
 
except ValueError:
    print("El dato ingresado debe ser numerico") 