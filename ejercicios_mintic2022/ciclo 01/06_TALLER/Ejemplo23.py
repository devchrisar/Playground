
while True:
    print("Bienvenido al sistema de ubicacion para zonas publicas WIFI")
    usuario = input("digite el nombre de usuario: ")
    if usuario!="":
        break
if usuario == "52216":
    contraseña = (input("digite la contraseña : "))
    if contraseña == "61225":
        primer_termino = str(usuario)[2:5]
        segundo_termino = ((4 * 4) - (10 - 1) - ( 6- 1))
        while True:
            try:
                captcha = int(input(primer_termino + " + " + str(segundo_termino) + " = ", ))
                break
            except ValueError:
                print(" ERROR ")
                exit()
        if captcha == (int(primer_termino) + int(segundo_termino)):
            print( " sesion iniciada ")
        else:
             print(" ERROR ")
    else:
        print(" ERROR ")
else:
    print(" ERROR ")