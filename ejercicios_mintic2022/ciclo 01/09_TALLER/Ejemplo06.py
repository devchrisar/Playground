con = 0
Usuario = ""

while True:
    Usuario = input("Digite su Usuario: ")
    
    if con < 4:
        if Usuario == "123":
            print("Bienvenido......")
        else:
            con = con + 1    
    else:
        print("Se cuenta ha sido bloqueada")
        
    