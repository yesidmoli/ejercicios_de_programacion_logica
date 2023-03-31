"""Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está
el mayor número primo leído."""

try:
    #creamos una losta vacia
    numeros = []

    #creamos dos variables para la posicion y el numero mayor primo inicializadas en 0
    mayor = 0
    pos = 0

    #creamos un ciclo para obtener los numeros y agregarlos en la lista

    for i in range(10+1):

        num = int(input("Ingrese un numero entero "))

        #agregamos a la lista los numeros obtenidos

        numeros.append(num)

    #creamos otro ciclo para obtener la posicion del numero mayor primo

    for j in range(len(numeros)):

        num = numeros[j]

        if num % 2 != 0: #condicionamos para obtener el mayor numero primo
            mayor = num
            pos = j

    print(numeros)
    print(f"El numero mayor primo que es {mayor} se encuentra en la posicion {pos}") #imprimimos resultados



except Exception as e:
    print("El dato ingresado debe ser numerico")