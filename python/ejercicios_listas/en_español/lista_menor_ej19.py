"""Leer 10 números enteros, almacenarlos en una lista y determinar cuál es el número
menor."""

try:
    numeros = [] #creamos la lista para almacenar los numeros ingresados
    

    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        numeros.append(int(input("Ingrese un numero entero "))) #solicitamos y agregamos los numeros  a la lista

    menor = numeros[0]   #inicializamos menor con los posicion 0 de la lista

    for i in range(len(numeros)): #recorremos la lista para determinar el numero menor

        if numeros[i] < menor: #condicionamos para saber cual es el menor
            menor = numeros[i]

    print(f"lista original {numeros}") 
    print(f"El numero menor de la lista es: {menor}") #imprimimos el numero menor
    
except ValueError:
    print("El dato ingresado debe ser numerico") 