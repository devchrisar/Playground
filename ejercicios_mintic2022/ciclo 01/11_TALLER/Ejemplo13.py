
personas = []

while True:
    print("1. Agregar")
    print("2. Listar")
    print("3. Salir")

    opc = int(input("Seleccione Opción: "))

    if opc == 1:
        personas.append(input("Digite su Nombre: "))
    if opc == 2:
        print(personas)    
    if opc==3:
        break    