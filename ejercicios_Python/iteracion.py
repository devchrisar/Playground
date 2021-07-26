# iteracion.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/01_Introduccion/04_Strings.md#ejercicio-118-geringoso-r%C3%BAstico

# Ejercicio 1.17


# Usá el comando for para iterar sobre los caracteres de una cadena.

# >>> cadena = "Ejemplo con for"
# >>> for c in cadena:
#         print('caracter:', c)
# # Mirá el output.
# 
# Modificá el código anterior de manera que dentro del ciclo el programa cuente cuántas letras "o" hay en la cadena.
# 
# Sugerencia: usá un contador como con los meses de la hipoteca.

cadena = "Ejemplo con for"

number_of_characters = 0

for c in cadena:
    if c.lower() == "o":
        number_of_characters += 1

print("El numero de 'o' es:", number_of_characters)

# Output:

# $ python iteracion.py 
# El numero de 'o' es: 3