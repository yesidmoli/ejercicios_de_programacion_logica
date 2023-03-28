"""leer dos numeros y mostrar todos los numeros terminados en 4 comprendidos entre ellos"""
try: 
	num1= int(input("Ingrese el primer numero entero  ")) #capturamos los dos numeros  
	num2= int(input("Ingrese el segundo numero  entero  ")) 

	for i in range(num1,num2+1): #recorremos para obtener los numeros comprendidos entre los dos rangos

		if i % 10 == 4: #comprobamos si los nuemeros terminan en 4

			print(i) #si la condicion se cumple imprimimos los numeros terminados en 4
			
except ValueError:
	print("El dato ingresado debe ser numerico")