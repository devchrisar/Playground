
import os

print("Bienvenido al sistema de ubicacion para zonas publicas WIFI")

USUARIO_I = "52216"
CLAVE_I = "61225"

USUARIO_E = input("Nombre de  Usuario: ")
CLAVE_E = input("Contraseña: ")

if (USUARIO_I == USUARIO_E) and (CLAVE_I == CLAVE_E):
    print("")
    print("INICIO SESION CON EXITO")
else:
    print("ERROR DE USUARIO  O CLAVE....")
    os._exit(1)  

