

suma = 0
cant=3
#20
# cant = int(input("Digite la cantidad de edades a promediar: "))
for i in range(cant):
    edad = int(input("Digite la edad "))
    suma += edad     #  suma = suma + edad
promedad = suma / cant
print(promedad)