"""Crear un programa que almacene 10 numeros enteros en una lista y que los muestre en otra lista en orden inverso"""

try:
	lista =  []
	lista_inversa = []
	

	rango = int(input("Ingrese el rango de la lista, recuerde que no debe pasar de 10 "))

	if rango < 0 or rango > 10:
		print("Se encuentra fuera del rango ")

	else:

		for i in range(rango):

			num = int(input("Ingrese  numeros enteros "))

			lista.append(num)

		for i in reversed(lista):

			lista_inversa.append(i)

		print(f" Orden ingresado {lista}")
		print(f" Orden inverso {lista_inversa}")



except ValueError:
	print("El dato ingresado debe ser numerico")


