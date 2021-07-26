import os

while True:
    
    print("")
    print("******************   MENU PRINCIPAL *****************")
    print("1. Seguir Conectado")
    print("2. Salir")
    print("*****************************************************")
   
    opc = int(input("Seleccione Opción: "))

    if opc == 1:
        os.system ("cls")
        print("Usted esta contento en el ciclo no quiere salir...!! ")
    else:
        if opc == 2:
            os.system ("cls")
            print("Usted se quiere Salir.. Hasta Pronto")    
            break
        else:
            os.system ("cls")
            print("Error")  
   
print("Lo esperamos Pronto..")  
    
    