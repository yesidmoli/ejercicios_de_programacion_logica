"""Mostrar en pantalla los primeros 20 múltiplos de 3."""

try:
	
	print(f"Los primeros 20 multiplos de 3 son: ")

	for i in range(1, 20+1): #recorremos el ciclo dando los parametros 
			
			print(i*3) #imprimimos resultado

except ValueError:
	print("El dato ingresado debe ser numerico")