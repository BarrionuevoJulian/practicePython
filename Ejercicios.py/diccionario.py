person = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "telefono": None,
}

person["nombre"] = input("Ingrese su nombre: ")
person["edad"] = input("Ingrese su edad: ")
person["direccion"] = input("Ingrese su direccion: ")
person["telefono"] = input("Ingrese su telefono: ")
 
print("\nSu numero de nombre es",person["nombre"],"edad",person["edad"],"dirreccion",person["direccion"],"y telefono",person["telefono"])