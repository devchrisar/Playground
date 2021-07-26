

opc = 0

while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opc = int(input("Digite Opción: "))

    if (opc >= 1 and opc < 5):
        Numero1 = float(input("Digite Numero1: "))
        Numero2 = float(input("Digite Numero2: "))
   
    if opc == 1:
        Res = Numero1 + Numero2

    else:
        if opc == 2:
            Res = Numero1 - Numero2
        else:
            if opc == 3:
                Res = Numero1 *  Numero2
            else:
                if opc == 4:
                    Res = Numero1 /  Numero2        
                else:
                    if opc == 5:
                        break
                    else:
                        print("Error")
    
    print("El resultado es: ", Res)

print("Hasta pronto")





    
    
    
    