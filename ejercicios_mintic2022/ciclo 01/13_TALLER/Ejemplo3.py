ALUMNOS = []
NOTAS = []

for i in range(3):
    nombre = input("Digite Nombre: ")
    ALUMNOS.append(nombre)

    nota1 = input("Digite Nota 1:")
    nota2 = input("Digite Nota 2:")

    NOTAS.append([nota1,nota2])


print(ALUMNOS)
print(NOTAS)
    