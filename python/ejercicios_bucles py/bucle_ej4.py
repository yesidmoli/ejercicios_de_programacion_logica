"""leer dos numeros y mostrar todos los enteros comprendidos entre ellos"""
try: 
	num1= int(input("Ingrese el primer numero entero  ")) #capturamos los dos numeros  
	num2= int(input("Ingrese el segundo numero  entero  ")) 

	for i in range(num1,num2+1): #recorremos 

			print(i)
		

	

except ValueError:
	print("El dato ingresado debe ser numerico")