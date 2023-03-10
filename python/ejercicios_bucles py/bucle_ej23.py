"""23.Leer un número entero y determinar si la suma de sus dígitos es también un número
primo."""

try: #capturamos el numero 
    num = int(input("Ingrese el  numero entero  "))
    suma = 0 #inicializamos la suma en 0
    

    while num != 0: #recorremos por medio de un ciclo para capturar los digitos
        digito = num % 10 
        suma += digito
        num //= 10

    print(f"La suma de los digitos del numero es: {suma}") 

    if suma % 2 != 0: #condicionamos para saber si es primo
        print("El resultado de la suma es un numero primo")
    else:
        print("El resultado de la suma no es un numero primo") #de lo contrario no es primo
     

except ValueError:
    print("El dato ingresado debe ser numerico")