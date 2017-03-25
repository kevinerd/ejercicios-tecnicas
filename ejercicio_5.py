n1 = input("Ingrese la nota 1: ")
n2 = input("Ingrese la nota 2: ")
n3 = input("Ingrese la nota 3: ")
n4 = input("Ingrese la nota 4: ")
n5 = input("Ingrese la nota 5: ")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)

total = n1 + n2 + n3 + n4 + n5
promedio = total / 5

if(promedio > 7):
    print("Alumno aprobado.")
else:
    print("Alumno reprobado.")
