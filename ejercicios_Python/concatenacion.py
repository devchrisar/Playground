# concatenacion.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/01_Introduccion/04_Strings.md#ejercicio-118-geringoso-r%C3%BAstico

# Ejercicio 1.15

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

# que quede 'Manzana,Naranja,Mandarina,Banana,Kiwi,Pera'.

frutas += ",Pera"

print(frutas)

# Agregá 'Melón'` al principio de la cadena:

frutas = "Melón," + frutas

print(frutas)