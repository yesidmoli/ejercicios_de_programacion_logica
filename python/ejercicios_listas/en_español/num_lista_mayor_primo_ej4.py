"""Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está
el mayor número primo leído."""

try:
    #creamos una lista vacia
    numeros = []
    lista_primos = []

    #creamos dos variables para la posicion y el numero mayor primo inicializadas en 0
    mayor = 0
    pos = 0

    #creamos un ciclo para obtener los numeros y agregarlos en la lista

    for i in range(10):

        num = int(input("Ingrese un numero entero "))

        #agregamos a la lista los numeros obtenidos

        numeros.append(num)

    #creamos otro ciclo para obtener los numeros primos y agregarlos en otra lista

    for j in range(len(numeros)):

        num = numeros[j]

        if num %  2 != 0: #condicionamos para obtener los numeros primos 

            lista_primos.append(num) #agregamos a la lista los que sean primos


    """for k in range(len(lista_primos)): # creamos un ciclo para recorrer la lista de los primos y obtener el mayor

        num2 = lista_primos[k]

        if num2 > mayor:

            mayor = num2
            pos = j"""

    mayor = max(lista_primos)

    pos = lista_primos.index(mayor)

    print(f"lista original: {numeros}")
    print(f"lista primos {lista_primos}")
    print(f"El numero mayor primo que es {mayor} se encuentra en la posicion {pos}") #imprimimos resultados



except ValueError:
    print("El dato ingresado debe ser numerico")