

personas = []

personas.append(input("Digite su Nombre:"))

print(personas)

personas.append(input("Digite su Nombre:"))

print(personas)

nombre = input("Digite Nombre a Eliminar: ")

posicion = personas.index(nombre)

print("La posición de dato a eliminar es: ", posicion)

personas.remove(nombre)

print(personas)

nombre1 = input("Digite Nombre a Modificar: ")

personas.insert(0,nombre1)

print(personas)



