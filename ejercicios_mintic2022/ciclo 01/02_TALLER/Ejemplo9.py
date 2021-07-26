
archivo_externo = "ejemplo.txt"
buscar = input("Digite Nombre a Borrar: ")
copia_archivo = open(archivo_externo, "r")
datos = copia_archivo.readlines()
print(datos)

copia2 = open(archivo_externo, "w")

control=""
for linea in datos:
    if buscar in linea:
        control = "Encontrado"
    else:
         copia2.write(linea)  
print(control)


