

numero = input("Digite Numero Para generar Tabla de Multiplicar: ")

for inicio in range(10):
    print(str(inicio), " * ", numero, " = ", end="")
    RES = inicio * float(numero)
    print(RES)