import platform
import os
import time


def limpiador_pantalla():
    if os.name == 'nt' or os.name == 'ce' or os.name == 'dos':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')


coordenadas = []
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
                        if menu[opciones - 1] == "Cambiar contraseña":
                            clave_2 = (input("Digite la clave actual :"))
                            if clave == clave_2:
                                clave_2 = (input("Digite la nueva clave :"))
                                if clave != clave_2:
                                    clave = clave_2
                                else:
                                    print(
                                        "La nueva contraseña no puede ser igual a la anterior")
                                    time.sleep(2)
                            else:
                                print("Error")
                                exit()
                        elif menu[opciones - 1] == "Ingresar coordenadas actuales":
                            if len(coordenadas) == 0:
                                coordenadas = [[0] * 2 for i in range(3)]
                                for i in range(3):
                                    for j in range(2):
                                        try:
                                            if j == 0:
                                                coordenadas[i][j] = float(
                                                    input("Digite la latitud para la coordenada "+str(i + 1) + ": "))
                                                coordenadas[i][j] = round(
                                                    coordenadas[i][j], 3)
                                                if coordenadas[i][j] > 6.284 or coordenadas[i][j] < 6.077:
                                                    print("Error coordenada")
                                                    exit()
                                            else:
                                                coordenadas[i][j] = float(
                                                    input("Digite la longitud para la coordenada "+str(i + 1) + ": "))
                                                coordenadas[i][j] = round(
                                                    coordenadas[i][j], 3)
                                                if coordenadas[i][j] > -75.841 or coordenadas[i][j] < -76.049:
                                                    print("Error coordenada")
                                                    exit()
                                        except ValueError:
                                            print("Error")
                                            exit()
                            else:
                                for i in range(3):
                                    print(
                                        "coordenada [latitud,longitud] " + str(i + 1)+" :", coordenadas[i])
                                print("La coordenada " + str(coordenadas.index(
                                    max(coordenadas)) + 1) + " es la que esta ubicada más al sur")
                                latitudPromedio = 0
                                longitudPromedio = 0
                                for i in range(3):
                                    for j in range(2):
                                        if j == 0:
                                            latitudPromedio = latitudPromedio + \
                                                coordenadas[i][j]
                                        else:
                                            longitudPromedio = longitudPromedio + \
                                                coordenadas[i][j]
                                latitudPromedio /= 3
                                longitudPromedio /= 3
                                latitudPromedio = round(latitudPromedio, 3)
                                longitudPromedio = round(longitudPromedio, 3)
                                print("La coordenada promedio de todos los puntos [latitud,longitud] : [" + str(
                                    latitudPromedio) + "," + str(longitudPromedio) + "]")
                                time.sleep(2)
                                try:
                                    actualizarCoordenadas = int(input(
                                        "Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú :"))

                                    if actualizarCoordenadas >= 1 and actualizarCoordenadas <= 3:

                                        coordenadas[actualizarCoordenadas - 1][0] = round(float(
                                            input("Digite la latitud para la coordenada :" + str(actualizarCoordenadas))), 3)
                                        if coordenadas[int(actualizarCoordenadas) - 1][0] > 6.284 or coordenadas[actualizarCoordenadas - 1][0] < 6.077:
                                            print("Error coordenada")
                                            exit()

                                        coordenadas[actualizarCoordenadas - 1][1] = round(float(
                                            input("Digite la longitud para la coordenada :" + str(actualizarCoordenadas))), 3)
                                        if coordenadas[i][j] > -75.841 or coordenadas[i][j] < -76.049:
                                            print("Error coordenada")
                                            exit()
                                    elif actualizarCoordenadas == 0:
                                        pass
                                    else:
                                        print("Error actualización")
                                        exit()
                                except ValueError:
                                    print("Error actualización")
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
