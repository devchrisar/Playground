
SavedUser = "123"
SavedPasword = 123
UserCon = 0
PassCon = 0
print("Bienvenido")
print("")
while True:
    if UserCon < 3:
        if input("Ingrese su usuario: ")==SavedUser:
            while True:
                if PassCon < 3:  
                    if int(input("Ingrese su contraseña: "))==SavedPasword:
                        print("Sesión iniciada")
                        break
                    else:
                        print("Contraseña incorrecta")
                        PassCon = PassCon + 1
                else:
                    print("Usuario y contraseña bloqueados, favor comunicarse con soporte.")
                    break
            break    
        else:  
            print("Usuario incorrecto") 
            UserCon = UserCon + 1
    else:    
        print("Usuario Bloqueado")
        break
    