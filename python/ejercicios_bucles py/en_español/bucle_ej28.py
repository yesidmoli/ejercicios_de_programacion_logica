"""Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos
primos."""

try:
    num1 = int(input("Ingrese el primer numero entero "))
    num2 = int(input("Ingrese el segundo numero entero "))
    contador_1 = 0
    contador_2 = 0


    while num1  != 0:
        digito_1 = num1 % 10
        num1 //= 10
        contador_1 += 1

       
    while num2 != 0:
        digito_2 = num2 % 10
        num2 //= 10
        contador_2 += 1

    if contador_1 > contador_2 :
        print("El primero numero tien mas digitos que el segundo numero")
   
    elif contador_2 > contador_1:
         print("El segundo numero tiene mas digitos que el primer numero ")

    else:
        print("lo dos numero tienen la misma cantidad de digitos ")

                  

except ValueError:
    print("El dato ingresado debe ser numerico")