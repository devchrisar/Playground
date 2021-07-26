import csv

with open(r'C:\Users\chris\OneDrive\Escritorio\APPS\ejercicios_mintic2022\empleados.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineas = 0
    for row in csv_reader:
        if lineas == 0:
            print(f'Los nombres de las columnas son:  {", ".join(row)}')
            lineas += 1
        else:
            print(
                f'\t{row[0]} trabaja como {row[1]}, y nació el {row[2]} , de {row[3]}.')
            lineas += 1
    print(f' documento Procesado en {lineas} lineas.')
