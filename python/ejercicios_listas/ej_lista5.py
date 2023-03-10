"""Elabore un algoritmo que almacene 20 numeros en una lista. imprima la sumatoria de los numeros de la lista"""
try:
	lista =  []
	suma = 0


	rango = int(input("Ingrese el rango de la lista, recuerde que no debe pasar de 20 "))

	if rango < 0 or rango > 20:
		print("Se encuentra fuera del rango ")

	else:

		for i in range(rango):

			num = int(input("Ingrese numeros enteros "))

			lista.append(num)

		for j in range(len(lista)):

			suma += lista [j]

		print(f"La lista original es: {lista}")
		print(f"La sumatoria de la lista es: {suma}")

	



except ValueError:
	print("El dato ingresado debe ser numerico")