"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones
están los números positivos. """

try:
    numeros = [] #creamos la lista para almacenar los numeros ingresados
    posiciones = []
    pos = 0
    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        numeros.append(int(input("Ingrese un numero entero "))) #solicitamos y agregamos los numeros  a la lista

        if numeros[i] > 0: #condicionamos para saber la posicion de los positivos
        	pos = i
        	posiciones.append(pos) #agregamos las posiciones a la lista

    print(f"lista original {numeros}")

    if len(posiciones) > 0: #si lo que estan el la lista de pos es mayor a 0
    	print(f"Los numeros enteros positivos se encuentran en las posiciones {posiciones}") #imprimimos
    else:
    	print("En la lista no hay numeros positivos") #de lo contrario
	
except ValueError:
    print("El dato ingresado debe ser numerico") 