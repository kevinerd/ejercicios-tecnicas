user = input("Ingrese su usuario: ")

if(user == "admin"):
    clave = input("Ingrese su clave: ")
    if(clave == "admin17"):
        print("Bienvenido al sistema.")
    else:
        print("Clave incorrecta.")
else:
    print("Usuario incorrecto.")
