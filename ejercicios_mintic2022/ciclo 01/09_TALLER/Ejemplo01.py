
import os

numero = True
A = input("HACER Division: ")
Resultado = (Numero1 ,"-", Numero2 , "=",Numero1 / Numero2)
while (numero == True) or (A == "SI"or "Si" or "si"or "sI"):
    print("1. Continuar")
    print("2. salir")
    opc = int(input("seleccione opcion: "))
    
    numero = numero +1
    
    if  opc == 1 :
        Numero1 = int(input("Escriba un numero: "))
        Numero2 = int(input("Escriba un numero: "))
        print(Resultado)
        A
    if  Resultado > 0:
        print(Resultado)   
    else:
        if opc == 2:
            print("SALIR")        
            break 
        else:
            if opc == 2:
                os.system("cls")  
    
                print("salir")