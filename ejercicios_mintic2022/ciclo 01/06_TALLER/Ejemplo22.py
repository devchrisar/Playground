
usuario_i = "52216"
clave_i = "61225"


usuario = input("Nombre de Usuario: ")
if usuario == usuario_i:
    contraseña = input("ingresa la contraseña: ")
    if contraseña == clave_i:
        print("inicio de sesion con exito")
    else:
        print("*** ERROR***")
else:
    print("***ERROR***")

capcha = 216
operacion = 1 
print(capcha, "+", operacion, "=" )  
capcha_e = int(input("Digite Capcha: "))

if capcha_e == 217:
    print("Sesión iniciada")
else:
    print("Error")    

