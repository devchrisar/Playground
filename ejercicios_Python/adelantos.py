# adelantos.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/01_Introduccion/03_Numeros.md#ejercicio-111-bonus

# Ejercicio 1.8

# Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
# Modificá el programa ("hipoteca.py") para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.
# Cuando lo corras, este nuevo programa debería dar un pago total de 929965.62 en 342 meses.



saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mesAdelanto = 12
contadorMeses = 0

while saldo > 0:
    if mesAdelanto >= 1:
        saldo = saldo * (1+tasa/12) - pago_mensual - 1000
        total_pagado = total_pagado + pago_mensual + 1000  
        mesAdelanto -= 1
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    contadorMeses += 1

print('Total pagado', round(total_pagado, 2), "en un total de ", contadorMeses, "meses")

# Output:
# "Total pagado 929965.62 en un total de  342 meses"