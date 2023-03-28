"""Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3."""
try:
	suma = 0
	print(f"Los primeros 20 multiplos de 3 son: ")

	"""for i in range(1, 20+1): #recorremos el ciclo dando los parametros 

		suma += i * 3


			
	print(suma) #imprimimos resultado"""

	for i in range(1, 60+1): #recorremos el ciclo dando los parametros 

		if i % 3 == 0:

			suma += i 

			print(i)


			
	print(f" La suma de los multiplos es: {suma}") #imprimimos resultado

except ValueError:
	print("El dato ingresado debe ser numerico")