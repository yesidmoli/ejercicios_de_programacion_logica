try:
    numeros = [] # creamos una lista vacía para almacenar los números ingresados

    # creamos un ciclo para obtener 10 números 
    for i in range(10):
        # solicitamos al usuario un número entero y lo agregamos a la lista
        numeros.append(int(input("Ingrese un numero entero ")))

    menor = numeros[0]
    pos = 0

    # recorremos la lista de números
    for i in range(len(numeros)):
        cont_multi = 0 # inicializamos un contador 
        # creamos otro ciclo para verificar si i es divisible entre algún número menor a él mismo
        for j in range(2, (numeros[i] // 2) + 1):

            if numeros[i] % j  == 0: # si i es divisible, incrementamos el contador
                cont_multi += 1

        if cont_multi == 0: # si no se encontraron divisores distintos a 1 y a sí mismo, entonces i es primo
            if numeros[i] < menor:
                
                menor = numeros[i] # si es el primer número primo o es menor que el menor encontrado hasta ahora
                pos = i # lo almacenamos como el nuevo menor número primo y guardamos su posición

    # imprimimos la lista original 
    print(f"lista original {numeros}") 

    if menor == numeros[0]: #si no se encuentran nuemero primos menores y menor sigue siendo lo mismo
        print("No se encontraron números primos en la lista.")
    else:
        print(f"el numero menor primo es: {menor}") #si se encuentran imprimimos el menor y la posicion
        print(f"el numero menor primo esta en la posicion: {pos}")
except ValueError:
     print("El dato ingresado debe ser numerico")

