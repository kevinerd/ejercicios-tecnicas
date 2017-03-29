c = 0
nros = []
menor = 0

while(c<=9):
    nro = int(input("Ingrese un número para agregar a la lista: "))
    nros.append(nro)
    c = c + 1
    menor = nros[0]
for i in nums:
    if (i < menor):
        menor = i

print ("El número menor de la lista es: " + str(menor))
print ("La lista ingresada es: " + str (nums))
