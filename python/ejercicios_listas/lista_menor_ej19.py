"""Leer 10 números enteros, almacenarlos en una lista y determinar cuál es el número
menor."""

try:
    lista = [] #creamos la lista para almacenar los numeros ingresados
    

    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        lista.append(int(input("Ingrese un numero entero "))) #solicitamos y agregamos los numeros  a la lista

    menor = lista[0]   #inicializamos menor con los posicion 0 de la lista

    for i in range(len(lista)): #recorremos la lista para determinar el numero menor

        if lista[i] < menor: #condicionamos para saber cual es el menor
            menor = lista[i]

    print(f"lista original {lista}") 
    print(f"El numero menor de la lista es: {menor}") #imprimimos el numero menor
    
except ValueError:
    print("El dato ingresado debe ser numerico") 