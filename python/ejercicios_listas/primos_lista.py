try:
    #creamos una lista vacia
    lista = []

    #creamos dos variables para la posicion y el numero mayor primo inicializadas en 0
    mayor = 0
    pos = 0
    aux = 0
    num = 0

    #creamos un ciclo para obtener los numeros y agregarlos en la lista

    for i in range(10):

        num = int(input("Ingrese un numero entero "))

        #agregamos a la lista los numeros obtenidos

        lista.append(num)

    #creamos otro ciclo para obtener los numeros primos 

    for j in range(len(lista)):

        num = lista[j]
        cont = 0


        for k in range(2, ((num // 2) +1)): 

            if num % k == 0:
                cont += 1

        if cont == 0:
            aux = num
            pos = j
            if aux > mayor:
                mayor = aux
                posicion = pos



    print(f"lista original: {lista}")
    print(f"El numero mayor primo que es {mayor} se encuentra en la posicion {posicion}") #imprimimos resultados



except ValueError:
    print("El dato ingresado debe ser numerico")