valor_compra = input("Ingrese el total de la compra: $")
valor_compra = int(valor_compra)

tipo_compra = input("¿Qué método de pago utilizará? contado/tarjeta: ")

if(tipo_compra == 'contado'):
  print("La operación tiene un descuento del 10%. El nuevo valor total es: $" + str((valor_compra * 8) / 100) )
else:
    print("La operación no tiene descuento.")
