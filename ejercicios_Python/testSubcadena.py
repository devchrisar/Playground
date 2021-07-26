# testSubcadena.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/01_Introduccion/04_Strings.md#ejercicio-118-geringoso-r%C3%BAstico

# Ejercicio 1.16

# Experimentá con el operador in para buscar subcadenas. En el intérprete interactivo probá estas operaciones:
# 
# >>> 'Naranja' in frutas
# ?
# >>> 'nana' in frutas
# True
# >>> 'Lima' in frutas
# ?
# >>>

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

'Naranja' in frutas

'nana' in frutas

'Lima' in frutas

# Q: ¿Por qué la verificación de 'nana' dió True?

# A: Porque nana está incluida en el string de la variable 'frutas', especificamente en la substring "Banana"