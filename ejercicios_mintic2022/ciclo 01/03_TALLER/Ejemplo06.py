opcion = 0
estado = 0

while True:
    print("1. Opcion")
    print("2. Opcion")
    print("3. Salir")
    opcion = int(input("Digite Opcion: ") )

    if opcion == 1:

        print("El usuario marco opción 1")

    if opcion == 2:
        if estado==0:
            print("Puede Continuar")
        else:
            print("No digito coordenadas no puede continuar")
            break    
    
    if opcion == 3:
        break

    