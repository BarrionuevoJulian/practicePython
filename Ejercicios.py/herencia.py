class Animal: 
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        pass

class Gato(Animal):
    def hablar(self):
        return "Miau"

class Perro(Animal):
    def hablar(self):
        return "Guau"

gato = Gato("Felix")
perro = Perro("Odie")

print(f"{gato.nombre} dice: {gato.hablar()}")
print(f"{perro.nombre} dice: {perro.hablar()}")
    
    
