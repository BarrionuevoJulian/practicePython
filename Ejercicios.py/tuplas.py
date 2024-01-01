verduleria = ("banana","cereza","manzana")
yes = False

fruta = str(input("Ingrese su fruta: "))

for frut in verduleria:
    if fruta == frut:
        yes = True
    
if yes:
    print("La palabra está en la tupla.")
else: 
    print("La palabra no está en la tupla.")