import os


while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    try:
        opc = int(input("Favor selecciones Opción: "))
        if opc == 1:
            os.system("cls")
            print("Sumar")
        

        if opc == 2:
            os.system("cls")
            print("Restar")
        

        if opc == 3:
            os.system("cls")
            print("Hasta pronto....")
            break

        if opc < 1 or opc > 3:
            os.system("cls")
            print("Usted Selecciono una Opción erronea..")
    except:
        os.system("cls")
        print("Error en la Selección")
    finally:
        print("Tenga Cuidado con las Letras y Signos")    

    

    
                
   
                
    
    