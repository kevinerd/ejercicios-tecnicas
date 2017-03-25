moneda = input("¿A qué moneda desea convertir? dolar/euro: ")
if(moneda == "dolar"):
    valor = input("Ingrese el valor deseado: ")
    valor = float(valor)
    dolar = valor * 15.60
    print(dolar)
elif(moneda == "euro"):
    valor = input("Ingrese el valor deseado: ")
    valor = float(valor)
    euro = valor * 17.90
    print(euro)
else:
    print("Acción incorrecta.")
