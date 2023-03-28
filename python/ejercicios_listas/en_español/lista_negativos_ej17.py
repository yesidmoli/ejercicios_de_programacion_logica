"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
negativos hay."""

try:
    numeros = [] #creamos la lista para almacenar los numeros ingresados
    cont = 0
    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        numeros.append(int(input("Ingrese un numero entero "))) #solicitamos y agregamos los numeros  a la lista

        if numeros[i] < 0:
        	cont += 1

    if cont > 0:
    	print(f"En la lista hay {cont} numero(s) negativos")
    else:
    	print("Todos los numeros ingresados son positivos ")
	
except ValueError:
    print("El dato ingresado debe ser numerico") 