"""Leer 10 números enteros, almacenarlos en una lista y determinar si el promedio entero
de estos datos está almacenado en la lista. """


try:
    numeros = [] #creamos la lista para almacenar los numeros ingresados
    
    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        lista.append(int(input("Ingrese un numero entero "))) #solicitamos y agregamos los numeros  a la lista

    #creamos dos variables para sacar el promedio
    promedio = 0
    suma = 0
    #recorremos la lista para sacar el promedio
    for j in range(len(numeros)):

        suma += numeros[j]
        promedio = suma // len(numeros)

    print(f"Lista orinigal {numeros}") 

    if promedio == numeros[j]: #condicionamos para saber si el promedio esta en la lista
    	print(f"El promedio que es: {promedio} se encuentra en la lista") #si, si imprimimos
    else:
    	print(f"El promedio que es: {promedio} no se encuentra en la lista") #de lo contrario
    	
   
except ValueError:
    print("El dato ingresado debe ser numerico")