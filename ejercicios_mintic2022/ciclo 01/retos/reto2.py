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
    usuario = input("Digite el nombre de usuario : ")
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

            time.sleep(2)
            limpiador_pantalla()
            menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana",
                    "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión"]
            aumentador = 0
            while True:
                if aumentador >= 3:
                    limpiador_pantalla()
                    print("Error")
                    exit()
                for i in range(7):
                    print(str(i+1)+". ", menu[i])
                try:
                    opciones = int(input("Elija una opción: "))
                    if opciones < 1 or opciones > 7:
                        print("Error")
                        aumentador += 1
                        time.sleep(2)
                    elif opciones == 6:
                        try:
                            opciones_favorita = int(
                                input("Seleccione opción favorita: "))
                            aumentador = 0
                            if opciones_favorita < 1 or opciones_favorita > 5:
                                limpiador_pantalla()
                                print("Error")
                                exit()
                            else:
                                try:
                                    primer_digito = int(input(
                                        "Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es "))
                                    if primer_digito == 1:
                                        segundo_digito = int(input(
                                            "Para confirmar por favor responda: Me separaron de mi hermano siamés,antes era un ocho y ahora soy un… la respuesta es "))
                                        if segundo_digito == 6:
                                            opciones_favorita -= 1
                                            temporal = menu[opciones_favorita]
                                            menu.pop(opciones_favorita)
                                            menu.insert(0, temporal)
                                            limpiador_pantalla()
                                        else:
                                            print("Error")
                                    else:
                                        print("Error")
                                except ValueError:
                                    limpiador_pantalla()
                                    print("Error")
                                    exit()
                        except ValueError:
                            limpiador_pantalla()
                            print("Error")
                            exit()
                    elif opciones >= 1 and opciones <= 5:
                        print("Usted ha elegido la opción número " + str(opciones))
                        exit()
                    elif opciones == 7:
                        print("Hasta pronto")
                        exit()
                except ValueError:
                    print("Error")
                    aumentador += 1
                    time.sleep(2)

        else:
            limpiador_pantalla()
            print("Error")
    else:
        limpiador_pantalla()
        print("Error")
else:
    limpiador_pantalla()
    print("Error")
