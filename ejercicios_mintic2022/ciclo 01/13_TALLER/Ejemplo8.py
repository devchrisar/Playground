

ESTUDIANTES = []


def Persona(nombre1,apellido1):
    ESTUDIANTES.append([nombre1,apellido1])


for i in range(1,3):
    nombre = input("Digite su Nombre: ")
    apellido = input("Digite se Apellido: ")
    Persona(nombre, apellido)

print(ESTUDIANTES)