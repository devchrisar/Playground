import platform
import os
import time


def limpiador_pantalla():
    if os.name == 'nt' or os.name == 'ce' or os.name == 'dos':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')


while True:
    limpiador_pantalla()
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    usuario = input('Digite el nombre de usuario :')
    if usuario != '':
        break

if usuario == '52216':
    clave = (input("Digite la contraseña :"))
    if clave == '61225':
        primer_operacion = str(usuario)[2:5]
        segunda_operacion = (2 * 2) - (6 % 5) - 2
        while True:
            try:
                captcha = int(input(primer_operacion + ' + ' +
                                    str(segunda_operacion) + "= "))
                break
            except ValueError:
                limpiador_pantalla()
                print("Error")
                exit()
        if captcha == (int(primer_operacion) + int(segunda_operacion)):
            limpiador_pantalla()
            print("Sesión iniciada")
        else:
            limpiador_pantalla()
            print("Error")
    else:
        limpiador_pantalla()
        print("Error")
else:
    limpiador_pantalla()
    print("Error")
