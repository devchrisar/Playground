# inclusive.py
# Ejercicio 1.29

# Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra. 
# Como primera aproximación, completá el siguiente código para reemplazar todas las letras 'o' que figuren 
# en el último o anteúltimo caracter de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' 
# pasaría a ser 'todes somes programadores'. Guardá tu código en el archivo inclusive.py
# 
# >>> frase = 'todos somos programadores'
# >>> palabras = frase.split()
# >>> for palabra in palabras:
#         if ?
#         ...
#     frase_t = ?
#     print(frase_t)
# 'todes somes programadores'
# >>>
# 

frase = 'Los hermanos sean unidos porque ésa es la ley primera'

palabras = frase.split()

frase_t = ""

for palabra in palabras:
    ultimo_segmento = palabra[-2:]
    
    if "a" in ultimo_segmento:
        ultimo_segmento = ultimo_segmento.replace("a", "e")
        palabra = palabra.replace(palabra[-2:], ultimo_segmento)
    if "o" in ultimo_segmento:
        ultimo_segmento = ultimo_segmento.replace("o", "e")
        palabra = palabra.replace(palabra[-2:], ultimo_segmento)
    
    frase_t += palabra + " "

print(frase_t)