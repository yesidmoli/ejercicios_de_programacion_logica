"""Elabore un algoritmo que almacene 15 numeros en una lista. Imprimir el numero mayor y la posicion donde se encuentra"""

try:
	lista = []
	mayor = 0
	pos = 0

	rango = int(input("Ingrese el rango de la lista, recuerde que no debe pasar de 15 "))

	if rango < 0 or rango > 15:
		print("Se encuentra fuera del rango ")
	else:

		for i in range(rango):

			num = int(input("Ingrese un numero entero "))

			lista.append(num)

		print(lista)

		for j in range(len(lista)):
			num = lista[j]

			if num > mayor:
				mayor = num
				pos = j

		print(f" el numero mayor es: {mayor}")
		print(f"La posicion es: {pos}")


except ValueError:
	print("El numero ingresado debe ser numerico")