"""Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los datos
almacenados múltiplos de 3.""" 

try:
    lista = [] #creamos la lista para almacenar los numeros ingresados
    lista_multi = [] #creamos una lista para almacenar los multiplos de 3
    
    #creamos un ciclo para obtener los 10 numeros
    for i in range(10):

        lista.append(int(input("Ingrese un numero entero "))) #solicitamos y agregamos los numeros  a la lista

        if lista[i] % 3 == 0: #condicionamos para saber cuales son los multiplos de 3

            lista_multi.append(lista[i]) #almacenamos los multiplos en una lista
    
    if len(lista_multi) > 0:

        #imprimimos  la lista de los multiplos de 3
        print(f"los datos que son multiplos de 3 son: {lista_multi}")
    else:
        print("No hay multiplos de 3")
 
except ValueError:
    print("El dato ingresado debe ser numerico") 