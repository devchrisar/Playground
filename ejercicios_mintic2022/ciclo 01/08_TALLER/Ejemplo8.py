
estado = True

while estado == True:
    print("1. Seguir Conectado")
    print("2. Salir")
   
    opc = int(input("Seleccione Opción: "))

    if opc == 1:
        print("Usted esta contento en el ciclo no quiere salir...!! ")
    else:
        if opc == 2:
            print("Usted se quiere Salir.. Hasta Pronto")    
            break
        else:
            print("Error")  

print("Lo esperamos Pronto..")  
    
    