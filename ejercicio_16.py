c = 0
nums = []
menor = 0

while(c<=9):
    nro = int(input("Ingrese un número para agregar a la lista: "))
    nums.append(nro)
    c = c + 1
    menor = nums[0]
for i in nums:
    if (i < menor):
        menor = i

print ("El número menor de la lista es: " + str(menor))
print ("La lista ingresada es: " + str (nums))
