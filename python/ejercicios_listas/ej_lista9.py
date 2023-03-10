"""Elabore un programa que almacene 15 elementos en una lista. en una lista A almacene los numeros pares de la lista original, 
y en una lista B almacene los numeros impares de la lista original """

try: #creamos las listas para almacenar los elementos
	lista =  []
	lista_a = []
	lista_b = []

	rango = int(input("Ingrese el rango de la lista, debe ser hasta 15 ")) #solicitamos el rango para la lista

	if rango < 0 or rango > 15: #comprobamos si el rango esta dentro de lo solicitado
		print("Se encuentra fuera del rango ")

	else:

		for i in range(rango): #recorremos el rango, para obtener los elementos de la lista

			num = int(input("Ingrese los numeros enteros "))
			lista.append(num) #agregamos los elementos a la lista


		for j in range(len(lista)): #recorremos la lista original, para obtener los pares e impares

			if lista[j] % 2 == 0: 
				
				lista_a.append(lista[j]) #si la condicion se cumple agreamos los numeros pares a la lista para impares
			else:
				lista_b.append(lista[j])  #si la condicion no se cumple agregamos los numros impares a la lista de impares


		print("numero pares", lista_a) #imprimimos las listas
		print("numero impares", lista_b)

	
except ValueError:
	print("El dato ingresado debe ser numerico")