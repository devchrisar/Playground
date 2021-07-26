# esfera.py

# Ejercicio 1.13

# En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py que le pida al usuario que 
# ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma. 
# Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.
# 
# Finalmente, ejecutá el programa desde la línea de comandos para responder ¿cuál es el volumen de una esfera de radio 6? Debería darte 904.7786842338603.

import math

r = float(input("Ingresar el radio de una esfera: "))

pi = math.pi

volumen = 4/3 * pi * (r ** 3)

print("El volumen es " + str(volumen))

# Output:

# Ingresar el radio de una esfera: 6
# El volumen es 904.7786842338603