"""5. Almacenar en una lista de 10 posiciones los 10 primeros números primos comprendidos
entre 100 y 300. Luego mostrarlos en pantalla."""

try:

	numeros = []
	cont = 0

	for i in range(100,300):
		
		if i % 2 != 0:

			numeros.append(i)
			cont += 1

			if cont == 10:
				break
			

	print(numeros)

except ValueError: 
	print("EL dato ingresado debe ser numerico")