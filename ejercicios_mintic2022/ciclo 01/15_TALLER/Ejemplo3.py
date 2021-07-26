
archivo_externo = "C:/Users/Usuario/Documents/Taller_Archivos/personas.csv"
archivo_en_memoria = open(archivo_externo, 'a')

cedula = input("Digite Documento: ")
nombre = input("Digite Nombre: ")
apellido = input("Digite Apellido: ")
celular = input("Digite Celular: ")


archivo_en_memoria.write("\n" + cedula + "," + nombre + "," + apellido + "," + celular)



archivo_en_memoria.close()


