"""6. Leer dos números enteros y almacenar en una lista los 10 primeros números primos
comprendidos entre el menor y el mayor. Luego mostrarlos en pantalla."""


try:
	primos = [] #creamos la lista vacia
	cont = 0

	num1 = int(input("Ingrese el primer numero a buscar los numeros primos ")) # Leer dos números enteros
	num2 = int(input("Ingrese el segundo numero hasta donde se calculara el numero primo "))

	if num1 < num2: # Encontrar el número menor y mayor
		menor = num1
		mayor = num2
	else:
		menor = num2
		mayor = num1


	# Encontrar los números primos entre el menor y el mayor
	for i in range(menor, mayor +1):

		if i > 1:

			for j in range(2, i):

				if ( i % j)  == 0:
					

			else:

				primos.append(i)
				if len(primos) == 10:
					break


	print(primos)  #Mostrar los números primos encontrados
	

except ValueError:
	print("El dato debe ser numerico")

