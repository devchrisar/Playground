males = int(input("Por favor indique cuantos hombres: "))
female = int(input("Por favor indique cuantas mujeres: "))
totalStudents = males + female
for i in range(totalStudents):
    malePercentage = males / totalStudents
    femalePercentage = female / totalStudents

print("Hay un total de " + str(totalStudents) + " personas " +
      format(malePercentage, ".0%") + " de ellos son hombres y " +
      format(femalePercentage, ".0%") + "  son mujeres")
