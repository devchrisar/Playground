
numeros = [0,0,0,0,0,0]

for i in range(0,6):
    numeros[i] = input( "ingrese el numero para la posción: " + str(i) + " : ")

print("")
print("Terminamos Proceso de Cargue de Datos")
print("")
print("")

print("***************Lista de Datos Guardados ********************")
for m in range(5,-1,-1):        
    print (numeros[m])