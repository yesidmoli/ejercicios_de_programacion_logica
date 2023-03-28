"""Elabore un programa que permita almacenar en una lista los 100 primeros numeros pares. La lista debe iniciar en 2"""

try:
	lista =  []


	for i in range(2, 200+1, 2):

		lista.append(i)

	print(f"Los 100 primeros numeros pares son: {lista} = A una longitud de", len(lista))

	
except ValueError:
	print("El dato ingresado debe ser numerico")