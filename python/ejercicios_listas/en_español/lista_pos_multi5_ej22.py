"""Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los números
múltiplos de 5 y en qué posiciones están."""


try:
    numeros = [] #creamos la lista para almacenar los numeros ingresados
    posiciones = []
    

    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):
        numeros.append(int(input("Ingrese un numero entero "))) #agregamos los numeros a la lista

    for i in range(len(numeros)): #recorremos la lista 
        if numeros[i] % 5 == 0: #condicionamo spara saber cuales numeros son multiplos de 5
            posiciones.append(i) #los que cumplan la condicion los agregamos a otra lista

    if len(posiciones) > 0: #condicionamos para saber si en la lista hay numeros

        print(f"lista original {numeros}")
        print(f"Los multiplos de 5 se encuentran en las posiciones {posiciones}") #imprimimos posiciones
    else:
        print("No hay multiplos de 5") #de lo contrario 
   
except ValueError:
    print("El dato ingresado debe ser numerico") 