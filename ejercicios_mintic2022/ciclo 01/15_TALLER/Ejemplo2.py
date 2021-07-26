

archivo_externo = "C:/Users/Usuario/Documents/Taller_Archivos/personas.csv"
archivo_en_memoria = open(archivo_externo)

contenido_archivo = archivo_en_memoria.readlines()

for fila in contenido_archivo:
    print(fila)