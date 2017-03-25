frase = input("Ingrese una frase: ")

vocales = 0
for l in frase:
    if(l in ("a", "e", "i", "o", "u")):
        vocales += 1
vocales = str(vocales)
print("Hay " + vocales + " vocales en la frase ingresada.")
