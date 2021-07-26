import os
import time

hora=0
minutos=0

while hora <= 24:  #0 1 2 3 .........23, 24
    hora = hora + 1
    if hora==3:
        break
    while minutos < 60:
        minutos = minutos + 1
        print("Hora: ", hora, " : minutos: ", minutos)
        time.sleep()
        os.system("cls")
    minutos = 0

