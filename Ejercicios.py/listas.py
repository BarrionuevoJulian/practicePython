mixta = [2,"chau",True]

mixta[0] = 3

print(mixta)

del mixta[0] #borrar

print(mixta)

#-----------------------------------------------------------------------------#

palabra = "continue"
lista = []
i = 0

while palabra != "stop":
    palabra = str(input("Ingrese un color a la vez, cuando termine ingrese 'stop': " ))
    lista.append(palabra)
    i+=1

del lista[i]

for lis in lista:
    print(lis)
