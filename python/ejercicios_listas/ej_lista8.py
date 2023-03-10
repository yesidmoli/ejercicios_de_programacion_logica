"""Almacenar en una lista 20 numeros enteros. imprimir cuantos numeros son impares"""

try:
	lista =  []
	conta = 0

	rango = int(input("Ingrese el rango de la lista, debe ser hasta 20 "))

	if rango < 0 or rango > 20:
		print("Se encuentra fuera del rango ")

	else:

		for i in range(rango):

			num = int(input("Ingrese los numeros enteros "))
			lista.append(num)


		for j in range(len(lista)):

			if lista[j] % 2 != 0:
				conta +=1


		print(f"La cantidad de numeros impares en la lista son: {conta}")

	
except ValueError:
	print("El dato ingresado debe ser numerico")