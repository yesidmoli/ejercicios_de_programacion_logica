"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está 
el número cuya suma de dígitos sea la mayor."""


try:
    numeros = [] #creamos la lista para almacenar los numeros ingresados
    

    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):
        numeros.append(int(input("Ingrese un numero entero "))) #agregamos los numeros a la lista
    print(f"lista original {numeros}") 

    lista_suma = [] #inicializamos las variables 
    pos = 0
    mayor = 0

    for j in range(len(numeros)): #recorremos la lista 
        suma = 0
        num = numeros[j]
        while num > 0: #creamos un while para obtener los digitos de cada numero
            suma += num % 10
            num //= 10
        lista_suma.append(suma) #la suma la agregamos a la lista 
        
        if suma > mayor: #comparamos para saber cual suma es mayor 
            mayor = suma
            pos = j

    
    print(f"la suma de los digitos de los numeros ingresados son: {lista_suma}")
    print(f"El numero mayor de la suma de sus digitos ({mayor}) esta en la posicion {pos}")  #imprimimos resultado
    
except ValueError:
    print("El dato ingresado debe ser numerico")  
