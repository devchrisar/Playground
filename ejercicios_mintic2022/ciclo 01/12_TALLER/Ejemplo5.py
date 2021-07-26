
datos = []

datos.append("Heiver")
datos.append("Camila")
datos.append("Maria")
print(datos)

posicion = input("Digite Posicion que desea Eliminar:")

datos.pop(int(posicion))

print(datos)