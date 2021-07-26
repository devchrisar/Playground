import os

personas = []

while True:
    print("1. Agregar")
    print("2. Listar")
    print("3. Eliminar")
    print("4. Salir")

    opc = int(input("Seleccione Opción: "))

    if opc == 1:
        os.system("CLS")
        personas.append(input("Digite su Nombre: "))
        
    if opc == 2:
        os.system("CLS")    
        print(personas)
        
    if opc == 3:
        os.system("CLS")
        nom_buscar = input("Digite Nombre a Eliminar: ") 
        personas.remove(nom_buscar)
        

    if opc==4:
        break  
