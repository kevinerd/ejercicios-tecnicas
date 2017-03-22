bancos = input("Ingrese la cantidad de bancos: ")
bancos = int(bancos)

alumnos = input("Ingrese la cantidad de alumnos: ")
alumnos = int(alumnos)

faltante = alumnos - bancos
if(bancos<alumnos):
    print("Los bancos no son suficientes. Faltan " + str(faltante) + " bancos.")
else:
    print("Los bancos son suficientes.")

