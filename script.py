print("Hola aprendiendo python")
nombre = "Lucas"
nombre:str = "Lucas"
print("Hola mi nombre es" + nombre)
apellido = "Osejo"
print(f"Soy {nombre} y mi apellido es {apellido}")
edad = 22
ciudad = "Bogotá"
tengo_carnet: bool = True

print(type(edad))
print(type(ciudad))
print(type(tengo_carnet))

print(nombre.upper())
print(apellido.lower())
print(len(nombre))
print(nombre[0])
print(apellido[-1])

persona = {
"nombre": "Lucas",
"edad": 22,
"ciudad": "Bogotá",
"solterx": True
}
print(persona["nombre"])

print(persona)

compra = ["pan", "leche", "huevos"]
compra.append("frutas")
compra.insert(1, "verduras")
compra.pop(-1)
print(compra)

culpable: bool = False
if culpable == True:
    print("Eres culpable")
else:
    print("No es culpable")

