"""Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros
comprendidos entre un dígito y otro."""

try:
	#capturamos los numeros
	num1 = int(input("Ingrese el primer  numero entero "))
	num2 = int(input("Ingrese el segundo numero entero "))
	
	print("Los enteros comprendidos entre {} y {} son: ".format(num1,num2))
	for i in range(num1,num2+1): #recorremos el ciclo dando los parametros que nos piden 

		

		print(i) #imprimimos resultado

except ValueError:
	print("El dato ingresado debe ser numerico")