# geringoso.py

# Ejercicio 1.18

# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
# 
# >>> cadena = 'Geringoso'
# >>> capadepenapa = ''
# >>> for c in cadena:
#         ?
# >>> capadepenapa
# Geperipingoposopo
# 
# Podés probar tu código cambiando la cadena inicial por otra palabra, como 'apa' o 'boligoma'.

cadena = 'Geringoso'
capadepenapa = ''

vocales = "aeiou"

for c in cadena:
    if c in vocales:
        capadepenapa += c + "p" + c 
    else:
        capadepenapa += c

print(capadepenapa)

# Output

# $ python geringoso.py 
# Geperipingoposopo