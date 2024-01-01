def calculadora(num1,num2,opera):
    match opera:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "/":
            return num1 / num2
        case "*":
            return num1 * num2
        case _:
            return "Operacion no valida"

numero1 = int(input("Ingrese el primer numero: "))
form = str(input("Ingrese la operacion a ejercitar: "))
numero2 = int(input("Ingrese el segundo numero: "))

while form == "/" and numero2 == 0:
    numero2 = int(input("Ingrese nuevmente un segundo numero, no puede ser cero: "))

print(calculadora(numero1,numero2,form))
