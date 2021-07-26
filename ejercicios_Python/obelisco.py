# obelisco.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/01_Introduccion/06_CierreClase.md

# Ejercicio 1.4

grosor_billete = 0.11 * 0.001 # 0.11 mm en metros
altura_obelisco = 67.5         # altura en metros
num_billetes = 1
dia = 1

while num_billetes * grosor_billete <= altura_obelisco:
    print(dia, num_billetes, num_billetes * grosor_billete)
    #dia = dias + 1
    dia = dia + 1
    num_billetes = num_billetes * 2

print('Cantidad de días', dia)
print('Cantidad de billetes', num_billetes)
print('Altura final', num_billetes * grosor_billete)


# El error estaba en la linea 10, la variable "dias" no estaba declarada.
# Comenté esa linea y añadi la linea 11 para arreglarlo, poniendo la variable correspondiente en el contador: "dia".