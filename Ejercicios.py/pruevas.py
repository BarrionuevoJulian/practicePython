# Programa que ingresas la cantidad de colores que necesitas en ves de tener ya la lista
# Para terminar de agrear colores, solo ponga la palabra "stop"

lista = [0]

palabra = "hola"

for lis in lista:
    palabra = str(input("Ingrese un color a la vez, cuando termine ingrese 'stop': "))
    if palabra == "stop":break
    lista.append(palabra)

del lista[0]

for li in lista:
    print(li)
