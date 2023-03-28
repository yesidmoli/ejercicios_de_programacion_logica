"""Elabore un algoritmo que almacene 10 numeros enteros en una lista, y en otra lista almacene el cubo de los numeros
de las primera lista"""


try:
	lista =  []
	lista_cubo = []
	cubo = 0


	rango = int(input("Ingrese el rango de la lista, recuerde que no debe pasar de 10 "))

	if rango < 0 or rango > 10:
		print("Se encuentra fuera del rango ")

	else:

		for i in range(rango):

			num = int(input("Ingrese 10 numeros enteros "))

			lista.append(num)

		for j in range(len(lista)):

			cubo = lista[j] **3 
		

			lista_cubo.append(cubo)

		print(f"La lista :{lista} elevado al cubo es: ")
		print(lista_cubo)


except ValueError:
	print("El dato ingresado debe ser numerico")


