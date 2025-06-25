usuarios={}

def validarNombreUsuario(nombre):
    if nombre in usuarios:
        print("Este nombre ya está en uso")
        return True
    else:
        return False

        
def validarSexo(sexo):
    if sexo != ("M" or "F"):
        print("Debe ingresar M o F solamente. Intente de nuevo.")
        return True
    else:
        return False
    
def validarContraseña(contraseña):
    if (len(contraseña)!=8):
        print("La contraseña debe tener un largo de 8 carácteres")
        return True
    numeros=''.join(filter(str.isdigit,contraseña))
    if numeros not in contraseña:
        print("La contraseña debe tener al menos un número")
        return True
    letras=''.join(filter(str.isalpha,contraseña))
    if letras not in contraseña:
        print("la contraseña debe tener al menos una letra")
        return True
    espacios=''.join(filter(str.isspace,contraseña))
    if espacios in contraseña:
        print("La contraseña no puede tener espacios")
        return True
    
def ingresarUsuario():
    while True:
        nombre=input("Ingrese su nombre de usuario: ").strip()
        error=validarNombreUsuario(nombre)
        if error:
            print("Error: ",error)
            continue
        else:
            break

    while True:
        sexo=str(input("Ingrese su sexo(F/M): ")).upper()
        error=validarSexo(sexo)
        if error:
            print("Error: ",error)
            continue
        else:
            break
    

    while True:
        contraseña=input("Ingrese una contraseña: ")
        error=validarContraseña(contraseña)
        if error:
            print("Error",error)
            continue
        else:
            usuarios[nombre]={'Sexo':sexo, 'Contraseña':contraseña}
            print("Usuario ingresado exitosamente")
            break

def buscarUsuario():
    buscar=input("ingrese el usuario a buscar: ")
    if buscar in usuarios:
        print (usuarios[buscar])
    else:
        print("Este usuario no existe")

def eliminarUsuario():
    eliminar=input("Ingrese el usuario a eliminar: ")
    if eliminar in usuarios:
        del eliminar
        print("Usuario Eliminado exitosamente")

def menu():
    while True:
        print("---MENU PRINCIPAL--- \n1.-Ingresar Usuario. \n2.-Buscar usuario. \n3.-Eliminar Usuario. \n4.-Salir")

        opcion=input("Ingrese opción: ")
        match opcion:
            case "1":
                ingresarUsuario()
            case "2":
                buscarUsuario()
            case "3":
                eliminarUsuario()
            case "4":
                break
            case TypeError:
                print("Debe ingresar una opcion válida.\n")
menu()