import os

opciones = ["1. Sumar", "2. Restar", "3. Multiplicar", "4. Dividir", "5. Salir"]

#global NUMERO1, NUMERO2

NUMERO1 = 2
NUMERO2 = 2

def Solicitar_datos(NUMERO1, NUMERO2):
   
    NUMERO1 = int(input("Digite Numero 1: "))
    NUMERO2 = int(input("Digite Numero 2: "))
    print("EL VALOR DE NUMERO1 ES: ", NUMERO1)
    print("EL VALOR DE NUMERO2 ES: ", NUMERO2)
    



def Sumar(A, B):
    R = A + B
    print("El valor de A ES: ", A)
    print("El valor de B ES: ", B)
    

    return R

def Restar(A, B):
    R = A - B
    return R

def Multiplicar(A,B):
    R = A * B
    return R

def Dividir(X, Y):
    R = X / Y
    return R    


while True:
    
    for i in range(len(opciones)):
        print(opciones[i])
    
    opcion = int(input("Digite Opción: "))

    

    if opcion == 1:
        os.system("cls")
        #Solicitar_datos(0,0)
        NUMERO1 = int(input("Digite Numero 1: "))
        NUMERO2 = int(input("Digite Numero 2: "))
        Z = Sumar(NUMERO1, NUMERO2)

    if opcion == 2:
        os.system("cls")
        #Solicitar_datos()
        NUMERO1 = int(input("Digite Numero 1: "))
        NUMERO2 = int(input("Digite Numero 2: "))
        Z = Restar(NUMERO1, NUMERO2)    

    if opcion == 3:
        os.system("cls")
        #Solicitar_datos()
        NUMERO1 = int(input("Digite Numero 1: "))
        NUMERO2 = int(input("Digite Numero 2: "))
        Z = Multiplicar(NUMERO1, NUMERO2)    
        
    if opcion == 4:
        os.system("cls")
        #Solicitar_datos()
        NUMERO1 = int(input("Digite Numero 1: "))
        NUMERO2 = int(input("Digite Numero 2: "))
        Z =Dividir(NUMERO1, NUMERO2) 
    
    

    if opcion == 5:
        break
    
    
    print("El resultado de Operación es: ", Z)