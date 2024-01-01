from ast import match_case
from re import Match


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola me llamo {self.nombre}, tengo {self.edad} años")

persona1 = Persona("Julián", 19)

persona1.saludar()

# Calculadora

class calculadora:
    def sumar(self, num1, num2):
        return num1 + num2
    def resta(self, num1, num2):
        return num1 - num2
    def division(self, num1, num2):
        if (num2 == 0): 
            print("Error no se puede dividir entre cero")
        else:
            return num1 / num2
    def multiplicar(self, num1, num2):
        return num1 * num2
    
# num1 = float(input("Ingrese el primer numero"))
# num2 = float(input("Ingrese el segundo numero"))
# num3 = float(input("Ingrese la operación"))

calc = calculadora()

# Contador de palabras

class ContadorPalabras:
    def __init__(self):
        self.conteo = 0  
    def contar(self, texto):
        palabras = texto.split()
        self.conteo += len(palabras)
    def obtener_contador(self):
        return self.conteo
# transfiero la clase a una variable, e inicializo con valor cero
tuki = ContadorPalabras() 
cadenaTexto = "lorem im pues apien ekfnl"

tuki.contar(cadenaTexto)
conteo = tuki.obtener_contador()
print(f"cantidad de palabra de la cadena es {conteo}")





        
