"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
tienen, de los almacenados allí, menos de 3 dígitos. """

try:
	numeros = [] #creamos la lista para almacenar los numeros ingresados
	menores = [] #creamos lista vacia para guardar las posiciones
	cont = 0

	for i in range(10): #obtenemos los numeros 

		num = int(input("Ingrese un numero entero "))

		lista.append(numenros) #agregamos los numeros a la lista

	for j in range(len(numeros)): #recorremos la lista para saber  los numeros con menos de 3 digitos

		
		if numeros[j] < 100: #condicionamos para saber quienes tienen menor digito

			menores.append(numeros[j]) #los que cumplan la condicion agregamos la posicion a la lista
			cont += 1

	print(numeros)

	if len(menores) > 0: #condicionamos para saber si en la lista hay numeros menores de 3 digitos
		print(f"Los numeros con menos de 3 digitos son: {menores}") #si se cumple imprimimos resultado
		print(f"la lista tiene {cont} numeros con menos de 3 digitos")
	else:
		print(" No se encontraron numeros menores de 3 digitos") #si no se cumple


except ValueError:
	print("El dato ingresado debe ser numerico")