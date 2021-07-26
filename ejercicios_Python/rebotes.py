# rebotes.py
# Archivo de ejemplo
# Ejercicio

# Ejercicio 1.5

altura = 100
rebotes = 10
count = 1

# Version sin round() con 4 digitos

#while rebotes >= count:
#    altura *= 3/5
#    print(count, altura)
#    count += 1

# Version con round() con 4 digitos

while rebotes >= count:
    altura *= 3/5
    print(count, round(altura, 4))
    count += 1