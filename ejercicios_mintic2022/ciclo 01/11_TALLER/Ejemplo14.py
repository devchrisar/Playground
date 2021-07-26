
datos = ["Heiver","Sandra","Paola","Diego"]

for i in range(0,4):
    print(datos[i] , end="-")
    

datos.remove("Sandra")
print()
print("*********** Resultado Final ***********")
print(datos)