
def DIFERENCIA_DIA(DA, DN):
    DD = DA - DN
    return DD

def DIFERENCIA_MES(MA,MN):
    MM = MA - MN
    return MM    

def DIFERENCIA_ANO(AA,AN):
    AA = AA - AN
    return AA

AA = int(input("Digite Año Actual: "))
MA = int(input("Digite Mes Actual: "))
DA = int(input("Digite Dia Actual: "))

AN = int(input("Digite Año Nacimiento: "))
MN = int(input("Digite Mes Nacimiento: "))
DN = int(input("Digite Dia Nacimiento: "))


DIAS = DIFERENCIA_DIA(DA, DN)
MESES = DIFERENCIA_MES(MA,MN)
ANO = DIFERENCIA_ANO(AA,AN)

print("Usted hoy tiene: ", ANO, " ", MESES, " Meses y ", DIAS, " dias")


