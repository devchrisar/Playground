
PERSONAS = [    # COL 0     COL1       COL2
              ["HEIVER", "MARYBEL", "ALEJANDRO"],   # FILA 0
              ["CLAUDIA", "LILIANA", "LEIDY"]       # FILA 1
           ]

for fila in range(0,2):
    for col in range(0,3):
        print(PERSONAS[fila][col], end=" ")
    print("")    