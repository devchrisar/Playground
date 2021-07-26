import os

print("Bienvenido al sistema de ubicacion para zonas publicas WIFI")
USUARIO_I = "52216"
USUARIO_E = input("Nombre de  Usuario: ")
if (USUARIO_I == USUARIO_E):
    print("")
    print("")
else:
    print("ERROR USUARIO....")
    os._exit(1)  

USUARIO_II = "61225"
USUARIO_EE = input("Contraseña: ")

if (USUARIO_II == USUARIO_EE):
    print("")
    print("INICIO SESION CON EXITO")
else:
    print("ERROR DE CLAVE.....")
    os._exit(1)
    