

archivo_externo = "C:/Users/Usuario/Documents/Taller_Archivos/personas.csv"
archivo_en_memoria = open(archivo_externo)
contenido_archivo = archivo_en_memoria.read()

print("\n El contenido del Archivo:", archivo_externo , "\n")
print()
print(contenido_archivo)