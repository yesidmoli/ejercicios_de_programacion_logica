"""Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el
promedio entero de los datos de la lista. """

try:
    lista = [] #creamos la lista para almacenar los numeros ingresados
    
    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        lista.append(int(input("Ingrese un numero entero "))) #agregamos los numeros ingresados a la lista

    #creamos dos variables para sacar el promedio
    promedio = 0
    suma = 0
    #recorremos la lista para sacar el promedio
    for j in range(len(lista)):

        suma += lista[j]
        promedio = suma // len(lista)

    print(f"Lista orinigal {lista}") 
    print(f"El promedio de los enteros de la lista es: {promedio} ") #imprimimos el promedio de los numeros enteros



except ValueError:
    print("El dato ingresado debe ser numerico")