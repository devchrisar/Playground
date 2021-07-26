import platform
import os
import time
import math


def limpiador_pantalla():
    if os.name == 'nt' or os.name == 'ce' or os.name == 'dos':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')


def mostrar_coordenadas_frecuentes(matriz):
    for i in range(len(matriz)):
        print("coordenada [latitud,longitud] " + str(i + 1)+" :", matriz[i])


def distancia_zonas(zonas, puntos):
    latitud1 = math.radians(puntos[0])
    longitud1 = math.radians(puntos[1])
    # radio de la tierra
    R_earth = 6372.795477598
    for i in range(len(zonas)):
        latitud2 = math.radians(zonas[i][0])
        longitud2 = math.radians(zonas[i][1])
        delta_longitude = longitud2 - longitud1
        # operacion matemática para sacar la distancia
        distancia = (math.acos(math.sin(latitud1) * math.sin(latitud2) + math.cos(
            latitud1) * math.cos(latitud2) * math.cos(delta_longitude))) * R_earth
        # hago la conversion de kilometros a metros
        distancia *= 1000
        #  .redondeo el valor y le elimino 3 decimales
        distancia = round(distancia, 3)
        # añado esta información a la lista de zonas
        zonas[i].append(distancia)
    # orden lista menos a mas
    for i in range(len(zonas) - 1):
        for j in range(i + 1, len(zonas)):
            if zonas[i][3] > zonas[j][3]:
                distancia_temporal = zonas[i]
                zonas[i] = zonas[j]
                zonas[j] = distancia_temporal
    return(zonas[:2])  # devuelve las 2 distancias menores


def ordenar_vector(vector):
    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i][2] > vector[j][2]:
                usuarios_promedio = vector[i]
                vector[i] = vector[j]
                vector[j] = usuarios_promedio
    return(vector)


def definir_zonas():
    zonasWifi = [[6.124, -75.946, 1035], [6.125, -75.966, 109],
                 [6.135, -75.976, 31], [6.144, -75.836, 151]]
    validaZonas = 0
    for i in range(4):
        for j in range(2):
            if j == 0:
                if zonasWifi[i][j] > 6.284 or zonasWifi[i][j] < 6.077:
                    print("La latitud de la coordenada ", i + 1,
                          " No esta dentro de los limites estipulados")
                    validaZonas = 1
            else:
                if zonasWifi[i][j] > -75.841 or zonasWifi[i][j] < -76.049:
                    print("La longitud de la coordenada ", i + 1,
                          " No esta dentro de los limites estipulados")
                    validaZonas = 1
    if validaZonas == 0:
        print("Las coordenadas cumplen con los limites estipulados")
    return(zonasWifi)
# !Easter Egg retos


def mostrar_hemisferio(latitud):
    limpiador_pantalla()
    if latitud > 0:
        print("Usted está en hemisferio norte")
    elif latitud < 0:
        print("Usted está en hemisferio sur")
    else:
        print("No sabemos donde te encuentras, por favor llame al 911 de inmediato")
    time.sleep(2)


def calcular_promedio_latitudes():
    try:
        cantidad_latitudes = int(
            input("Favor digite la cantidad de latitudes a ingresar: "))
        if cantidad_latitudes > 0:
            promedio = 0
            try:
                for i in range(cantidad_latitudes):
                    promedio = promedio + \
                        float(input("Digite la latitud # " + str(i + 1) + " : "))
            except ValueError:
                print("valor invalido para latitud")
                exit()
            promedio = promedio / cantidad_latitudes
            promedio = round(promedio, 3)
            print("El promedio de las latitudes ingresadas es: ", promedio)
            time.sleep(2)
        else:
            print("El valor ingresado debe ser mayor a 0")
            time.sleep(2)
    except ValueError:
        print("No a ingresado un valor correcto")
        time.sleep(2)


def calcular_zona_horaria():
    limpiador_pantalla()
    try:
        longitud = float(input(
            "Escribe una la coordenada de una longitud en Sudamérica y te diré su huso horario: "))
        if longitud >= -81.296 and longitud <= -67.401:
            print("El huso horario es -5")
            time.sleep(2)
        elif longitud >= -67.402 and longitud <= -54.316:
            print("El huso horario es -4")
            time.sleep(2)
        elif longitud > -54.316 and longitud <= -35.833:
            print("El huso horario es -3")
            time.sleep(2)
        else:
            print(
                "la longitud no a podido ser identificada o no se encuentra en Sudamérica")
            time.sleep(2)
        limpiador_pantalla()
    except ValueError:
        print("No ingresaste la longitud en un formato adecuado")
        time.sleep(2)


V_promMoto = 19.44  # m/s
V_promAuto = 20.83  # m/s
coordenadas = []
actualLocation = []
zonasWifi = definir_zonas()
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
                    if opciones < 1 or opciones > 7 and opciones != 2021 and opciones != 2022:  # prueba extra 1.2 reto 4
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
                        #! reto 3
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
                                    time.sleep(2)
                                    exit()
                            #!fin reto 3
                            # * reto 4
                        elif menu[opciones - 1] == "Ubicar zona wifi más cercana":
                            #zonasWifi = definir_zonas()
                            limpiador_pantalla()
                            if len(coordenadas) == 0:
                                print("Error sin registro de coordenadas")
                                time.sleep(2)
                                exit()
                            mostrar_coordenadas_frecuentes(coordenadas)
                            try:
                                sub_menuZona = int(input(
                                    "Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: "))
                                if sub_menuZona >= 1 and sub_menuZona <= 3:
                                    cordistancia = distancia_zonas(
                                        zonasWifi, coordenadas[sub_menuZona - 1])
                                    actualLocation = coordenadas[sub_menuZona - 1].copy()
                                    cordistancia = ordenar_vector(cordistancia)
                                    print(
                                        "Zonas Wifi mas cercanas con menos usuarios")
                                    for i in range(len(cordistancia)):
                                        print("La zona Wifi", i + 1, "ubicada en [", cordistancia[i][:2], "] a ",
                                              cordistancia[i][3], " metros , tiene en promedio", cordistancia[i][2], " usuarios")
                                    try:
                                        guia = "Para llegar a la zona Wifi dirigirse"
                                        indicacion = int(
                                            input("Elija 1 o 2 para recibir indicaciones de llegada: "))
                                        if indicacion >= 1 and indicacion <= 2:
                                            if coordenadas[sub_menuZona - 1][1] < cordistancia[indicacion - 1][1]:
                                                guia = guia + " primero al oriente"
                                            elif coordenadas[sub_menuZona - 1][1] > cordistancia[indicacion - 1][1]:
                                                guia = guia + " occidente"
                                            if coordenadas[sub_menuZona - 1][0] < cordistancia[indicacion - 1][0]:
                                                guia = guia + " y luego hacia el norte"
                                            elif coordenadas[sub_menuZona - 1][0] > cordistancia[indicacion - 1][0]:
                                                guia = guia + " y luego hacia el sur"
                                            tiempoAuto = cordistancia[indicacion -
                                                                      1][3] / V_promAuto
                                            tiempoMoto = cordistancia[indicacion -
                                                                      1][3] / V_promMoto
                                            tiempoAuto = round(
                                                tiempoAuto / 60, 2)
                                            tiempoMoto = round(
                                                tiempoMoto / 60, 2)
                                            print(guia)
                                            print("Tiempo estimado en auto",
                                                  tiempoAuto, "minutos")
                                            print("Tiempo estimado en moto",
                                                  tiempoMoto, "minutos")
                                            time.sleep(2)
                                            while True:
                                                salirOpcion = input(
                                                    "Presione 0 para salir: ")
                                                if salirOpcion == "0":
                                                    break
                                        else:
                                            print("Error zona wifi")
                                            time.sleep(2)
                                            exit()
                                    except ValueError:
                                        print("Error zona wifi")
                                        time.sleep(2)
                                        exit()
                                else:
                                    print("Error ubicación")
                                    time.sleep(2)
                                    exit()
                            except ValueError:
                                print("Error ubicación")
                                time.sleep(2)
                                exit()

                            # * fin reto 4
                            # todo reto 5
                        elif menu[opciones - 1] == "Guardar archivo con ubicación cercana":
                            if len(coordenadas) == 0:
                                print("Error de alistamiento")
                                time.sleep(2)
                                exit()
                            if len(actualLocation) == 0:
                                print("Error de alistamiento")
                                time.sleep(2)
                                exit()
                            diccionario_wifi = {"actual": actualLocation, "zonawifi1": [
                                cordistancia[0][0:3]], "recorrido": [cordistancia[0][3], "mediotransporte", tiempoAuto]}
                            print(diccionario_wifi)
                            while True:
                                opcion_menuTosave = input(
                                    "Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal: ")
                                if opcion_menuTosave == "1":
                                    try:
                                        archivo = open(
                                            r'C:\Users\chris\OneDrive\Escritorio\APPS\ejercicios_mintic2022\retos\diccionarioWifi.txt', "w")
                                        archivo.write(str(diccionario_wifi))
                                        print("Exportando archivo")
                                        time.sleep(2)
                                        exit()
                                    except IOError:
                                        print("Exportando archivo")
                                        time.sleep(2)
                                        exit()
                                elif opcion_menuTosave == "0":
                                    break
                    elif menu[opciones - 1] == "Actualizar registros de zonas wifi desde archivo":
                        try:
                            archivo = open(
                                r'C:\Users\chris\OneDrive\Escritorio\APPS\ejercicios_mintic2022\retos\actualizaZonas.txt')
                            indice = 0
                            for i in archivo.readlines():
                                zonasWifi[indice] = i.strip().split(',')
                                zonasWifi[indice][0] = float(
                                    zonasWifi[indice][0])
                                zonasWifi[indice][1] = float(
                                    zonasWifi[indice][1])
                                zonasWifi[indice][2] = int(
                                    zonasWifi[indice][2])
                                indice += 1
                            print(
                                "Las siguientes zonas wifis fueron actualizadas :")
                            print(zonasWifi)
                            while True:
                                opcion_menuToupdate = input(
                                    "Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: ")
                                if opcion_menuToupdate == "0":
                                    break
                        except ValueError:
                            while True:
                                if opcion_menuToupdate == "0":
                                    break
                            # todo fin reto 5

                    elif opciones == 7:
                        print("Hasta pronto")
                        exit()
                        #! prueba extra 1.2 reto 4
                    elif opciones == 2021:
                        while True:
                            try:
                                latitud_hemisferio = float(
                                    input("Dame una latitud  y te diré cual hemisferio es… : "))
                                mostrar_hemisferio(latitud_hemisferio)
                                break
                            except ValueError:
                                print(
                                    "Por favor Digite valores validos para la latitud")
                    elif opciones == 2022:
                        calcular_zona_horaria()
                except ValueError:
                    print("Error")
                    aumentador += 1
                    time.sleep(2)

        else:
            limpiador_pantalla()
            print("Error")
    elif clave == "m1s10nt1c":
        calcular_promedio_latitudes()
    else:
        limpiador_pantalla()
        print("Error")
        # prueba extra 1.1 reto 4
elif usuario == "Tripulante2022":
    print("Este fue mi primer programa y vamos por más")
    exit()
else:
    limpiador_pantalla()
    print("Error")
