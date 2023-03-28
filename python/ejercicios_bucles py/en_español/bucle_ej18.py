""" Leer dos números entero y mostrar todos los múltiplos de 5 comprendidos entre el
menor y el mayor."""

try:
    num1 = int(input("Ingrese el primer numero  "))
    num2 = int(input("Ingrese el segundo numero  "))
    
    if num1 < num2:

        for i in range(num1, num2+1): #recorremos el ciclo dando los parametros 
            print(i*5)

    elif num2 < num1:
        for i in range(num2, num1+1): #recorremos el ciclo dando los parametros 
            print(i*5)

    else:
        print("Los dos valores son iguales")
     

except ValueError:
    print("El dato ingresado debe ser numerico")