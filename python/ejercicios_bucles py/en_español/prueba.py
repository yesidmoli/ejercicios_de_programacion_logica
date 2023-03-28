
num = int(input("Ingresa un numero de 3 cifras "))

if num <= -999 and num >= -100:
	print("fuera del rango")
	
else:
	print("el ultimo digito del numero es: ", (num % 10))
