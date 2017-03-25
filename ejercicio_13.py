c = 0
num = []

while(c<=4):
    nro = int(input("Ingrese un numero: "))
    num.append(nro)
    c = c + 1

nro = 0

for i in num:
    nro = nro + i

promedio = nro / 5

print(promedio)
