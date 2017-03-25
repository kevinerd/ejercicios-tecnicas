usuario = input("Ingrese su usuario: ")
if(usuario == "admin"):
    clave = input("Ingrese su contraseña: ")
    if(clave == "admin"):
        print("Bienvenido Administrador.")
    else:
        print("Clave incorrecta.")
elif(usuario == "operador"):
    clave = input("Ingrese su contraseña: ")
    if(clave == "operador"):
        print("Bienvenido Operador.")
    else:
        print("Clave incorrecta.")
else:
    print("Usuario desconocido.")
