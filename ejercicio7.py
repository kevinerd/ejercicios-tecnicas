valor1 = input("Ingrese un valor: ")
valor1 = float(valor1)
valor2 = input("Ingrese otro valor: ")
valor2 = float(valor2)
operacion = input("Seleccione una operación: 1-Sumar, 2-Restar, 3-Dividir, 4-Multiplicar: ")
if(operacion == "1"):
    print(valor1 + valor2)
elif(operacion == "2"):
    print(valor1 - valor2)
elif(operacion == "3"):
    print(valor1 / valor2)
elif(operacion == "4"):
    print(valor1 * valor2)
else:
    print("Operación incorrecta.")
