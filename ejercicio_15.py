c = 0
nums = []
mayor = 0

while(c<=9):
    nro = int(input("Ingrese un número para agregar a la lista: "))
    nums.append(nro)
    c = c + 1

for n in nums:
    if (n > mayor):
        mayor = n

print ("La lista ingresada es: " + str (nums))
print ("El número mayor de la lista es: " + str(mayor))
