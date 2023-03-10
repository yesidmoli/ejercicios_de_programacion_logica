"""elabore un algoritmo que almacene en una lista 10 numeros enteros. imprima la lista"""


try:
	lista = [] #definimos la lista

	for i in range(10): #creamos un ciclo para definir el rango de la lista
		num = int(input("Ingrese 10 numeros enteros "))

		lista.append(num) #agregamos a la lista los numeros ingresados por el usuario


	print(lista) #imprimos la lista

except ValueError:
	print("error")
