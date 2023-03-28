"""leer un numero entero y mostrar todos los divisores exactos del numero comprendidos entre 1 y el numero leido"""
try: 
	num = int(input("Ingrese un numero entero  ")) #capturamos el numero 

	for i in range(1,num+1): #recorremos el numero ingresado

		if num % i == 0: #condicionamos para obtener los divisores exactos

			print(i)
		

	

except ValueError:
	print("El dato ingresado debe ser numerico")