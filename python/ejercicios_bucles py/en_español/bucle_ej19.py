"""Leer un número entero y determinar si es primo."""
try:
    num = int(input("Ingrese el  numero  "))
    

    for i in range(2,num +1): 

        if num % i != 0:
            print(f"El numero {num}  es primo")
            break
        else:
            print(f"El numero {num}  no es  primo")
            break
     

except ValueError:
    print("El dato ingresado debe ser numerico")