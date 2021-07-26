
PERSONAS = []
CELULAR = []
estado=""

while True:
    print("1. Agregar Contacto")
    print("2. Buscar")
    print("3. Listar")
    print("4. Salir")
    opc = int(input("Favor Seleccionar Opción: "))

    if opc == 1:
        nom = input("Digite su Nombre: ")
        PERSONAS.append(nom)
        cel = input("Digite su Numero de Celular: ")
        CELULAR.append(cel)
    
    if opc == 2:
        estado=""
        nom = input("Digite su Nombre")
        for z in range(0,len(PERSONAS)):
            if ( PERSONAS[z] == nom):
                print("Dato encontado: ", PERSONAS[z], "  El Movil es: ", CELULAR[z] )
                estado = "Encontrado"

        if estado == "":
            print("Contacto no encontrado...!!!")

    if opc == 3:
        print(PERSONAS)
        print(CELULAR)

    if opc == 4:
        print("Hasta pronto")
        break    





    
    
