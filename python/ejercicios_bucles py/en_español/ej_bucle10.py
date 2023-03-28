"""utilice un programa utilizando ciclos anidados que imprima las siguientes parejas
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
3 0
3 1
3 2
4 0
4 1
4 2"""
try:

    for i in range(0, 5):
        for j in range(0, 3):
            print(i, j)

except:
    print("Ha ocurrido un error")