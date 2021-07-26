
SavedUser="123"
SavedPasword=123
con_usua = 0

print("Bienvenido")
while True:
    if con_usua < 3:
        if input("Ingrese su usuario: ")==SavedUser:
            
            while True:
                if int(input("Ingrese su contraseña: "))==SavedPasword:
                    print("Sesión iniciada")
                    break
                else:
                    print("Contraseña incorrecta, intente de nuevo")
        else:
            print("Usuario incorrecto, intente de nuevo")
            con_usua = con_usua + 1
    else:
        print("Usuario Bloqueado...")
        break        
