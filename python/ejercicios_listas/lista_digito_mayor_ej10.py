"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones 
se encuentran los números con más de 3 dígitos."""

try:
	lista = [] #creamos la lista para almacenar los numeros ingresados
	posiciones = [] #creamos lista vacia para guardar las posiciones
	

	for i in range(10): #obtenemos los numeros 

		num = int(input("Ingrese un numero entero "))

		lista.append(num) #agregamos los numeros a la lista

	for j in range(len(lista)): #recorremos la lista para saber las posciones de los numeros con mas de 3 digitos

		
		if lista[j] > 99: #condicionamos para saber quienes tienen mayor digito

			posiciones.append(j) #los que cumplan la condicion agregamos la posicion a la lista





	print(lista)

	if len(posiciones) > 0: #condicionamos para saber si en la lista hay numeros con 3 digitos
		print(f"Los numeros con mas de 3 digitos estan en las posiciones: {posiciones}") #si se cumple imprimimos resultado
	else:
		print(" No se encontraron numeros mayores de 3 digitos") #si no se cumple


except ValueError:
	print("El dato ingresado debe ser numerico")