"""Elabore un programa que permita almacenar en 2 listas de 5 posiciones numeros enteros, en una tercera lista almacenar
la multiplicacion de los numeros de las dos listas. tenga en cuenta que se multiplican solo los numeros
que se encuentran en la misma posicion"""

try:
	lista_1 =  []
	lista_2 =  []
	lista_3 = []
	multiplicacion = 0

	rango = int(input("Ingrese el rango de la lista, debe ser hasta 5 "))

	if rango < 0 or rango > 5:
		print("Se encuentra fuera del rango ")

	else:

		for i in range(rango):

			num = int(input("Ingrese el numero entero para la lista 1 "))

			lista_1.append(num)

		print(lista_1)
		print("*****************************")


		for j in range(rango):

			num2 = int(input("Ingrese el numero entero para la lista 2 "))

			lista_2.append(num2)

		print(lista_2)
		print("*****************************")


		for k in range(len(lista_1)):

			multiplicacion = lista_1 [k] * lista_2[k]

			lista_3.append(multiplicacion)

		print(f"**************************************************  {lista_1}")
		print(f"**************************************************  {lista_2}")
		print(f"El resultado de la multiplicacion de las listas es: {lista_3}")


	
except ValueError:
	print("El dato ingresado debe ser numerico")