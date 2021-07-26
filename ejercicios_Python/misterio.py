# misterio.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/01_Introduccion/03_Numeros.md#ejercicio-111-bonus

# Ejercicio 1.12

# Las funciones int() y float() pueden usarse para convertir números. Por ejemplo,
# 
# >>> int("123")
# 123
# >>> float("1.23")
# 1.23
# >>>
# 
# Con esto en mente, ¿podrías explicar el siguiente comportamiento?
# 
# >>> bool("False")
# True
# >>>



################

# Rta: bool("False") devuelve True porque la string tiene contenido, no importa su valor. Si fuera una string vacia ("") y se intentara castear o convertir a bool entonces el valor booleano seria False. 
 
# >>> bool("") 
# False
# >>> bool("True") 
# True