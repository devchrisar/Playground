

suma = 0
cant = int(input("Digite Cuantas personas quiere que atienda: "))
#20
copia = ""

for i in range(1,cant+1):
    nombre = input(str(i) + ".  Digite su Nombre: ")
    copia = copia + nombre + "\n"
    edad = int(input(str(i) + ". Digite la edad:  "))
    suma += edad     #  suma = suma + edad
promedad = suma / cant
print(promedad)
print("")
print(copia)
