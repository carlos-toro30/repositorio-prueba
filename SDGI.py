lista_productos=[]
#producto={"nombre:":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
#cdoigo tiene que tener 3 validaciiones
#el codigo debe tener un minimo de 5 caracteres
#codigo debe tener al menos 3 mayusculas
#codigo debe tener al menos 1 numero

opcion="0"

"""
sacar finciones del while [x]
Cambiar las listas para crear el producto por un diccionario[]
agregar un codigo al diccionario de producto[]
agregar una lisat para almacenar los diccionarios[]
modificar las funciones para que utilicen la nueva estructura de diccionarios[]
agregar las funciones faltantes:
    actualizar cantidad/precio[]
    mostrar inventario completo[]
    eliminar producto[]
"""

def validarCodigo(codigo):
    contador_mayusculas=0
    contador_numeros=0
    for l in str(codigo):
        if l.isupper():
            contador_mayusculas+=1
        if l.isnumeric():
            contador_numeros+=1
    
    if contador_mayusculas<2:
        print("EL codigo debe tener almenos 2 mayusculas")
        return False
    elif contador_numeros ==0:
        print("El codigo debe tener almenos un numero")
        return False
    elif len(codigo) <5:
        print("El codigo debe tener al menos 5 caracteres")
        return False
    else:
        return True

def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ")
    while True:
        codigo=input("Ingrese el codigo para el producto: ")
        if validarCodigo(codigo)==True:
            print("Codigo correcto")
            break
        else:
            print("EL codigo es incorrecto, debe volver a ingresarlo")

    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        
        if stock<0 or precio <0:
            raise ValueError
            
        else:
            producto=[nombre,precio,stock,codigo]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")

def guardarProducto(nombre,precio,stock,codigo):
    #producto={"nombre:":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    productoBuscado=buscarProducto(codigo)
    if productoBuscado!=None:
        print("Ese producto ya fue registrado")
        return False
    
    producto={"nombre:":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    lista_productos.append(producto)
    return True
      

def buscarProducto(codigo):
    for producto in lista_productos:
      if codigo==producto["codigo"]:
          return producto 
      
    return None
   

def mostrarProducto(codigo):
    productoBuscado=buscarProducto(codigo)
    if productoBuscado!=None:
        print("-"*60)
        print(f"cod: {productoBuscado["codigo"]} \tnombre: {productoBuscado["nombre"]} \tprecio: ${productoBuscado["precio"]} \tstock: {productoBuscado["cantidad"]}")
        print("-"*60)
        return [nombre,precio,stock]
    print("No existe un producto con ese nombre")

while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")


    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)