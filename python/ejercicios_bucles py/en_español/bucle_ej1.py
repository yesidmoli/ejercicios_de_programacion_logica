"""leer un numero entero mostrar todos los enteros comprendido entre 1 y el numero leido"""

try: 
	num = int(input("Ingrese un numero entero  ")) #capturamos el numero 

	for i in range(1,num+1,1): #recorremos el numero ingresado

		print(i) #imprimimos
except ValueError:
	print("error")
