"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces se repite
el promedio entero de los datos dentro de la lista. """

try:
    lista = [] #creamos la lista para almacenar los numeros ingresados
    cont = 0
    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        lista.append(int(input("Ingrese un numero entero "))) #solicitamos y agregamos los numeros  a la lista

    #creamos dos variables para sacar el promedio
    promedio = 0
    suma = 0
    
    #recorremos la lista para sacar el promedio
    for j in range(len(lista)):

        suma += lista[j]
        promedio = suma // len(lista)

    print(f"Lista original {lista}") 

    if promedio == lista[j]: #condicionamos para saber si el promedio esta en la lista
        print(f"El promedio de la lista que es: {promedio} se encuentra en la lista") #si si imprimimos

        for k in range(len(lista)): #recorremos de nuevo la lista para comparar cuantas veces se repite el promedio

            if lista[k] == promedio:
                cont += 1

        print(f"El promedio en la lista se repite {cont} veces") #imprimimos las veces que se repite
	
    else:
        print(f"El promedio que es: {promedio} no se encuentra en la lista") #de lo contrario   

except ValueError:
    print("El dato ingresado debe ser numerico")
