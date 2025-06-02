
opcion=8

def menu():
    opcion=0
    while True:
        print("1- Agregar producto ")
        print("2- Eliminar producto ")
        print("3- Deshacer ultima accion ")
        print("4- Mostrar lista actual ")
        print("5- Salir ")
        try:
            opcion=int(input("Ingrese una opcion"))
            if( 0 < opcion <6):
                break
        except ValueError:
            print("Opcio invalida!")
    return opcion


arreglo=[]
undo=[]
while True:
    accion=menu()
    match accion:
        case 1:
            pNuevo=input("Ingrese un nuevo producto ")
            undo=arreglo.copy()
            arreglo.append(pNuevo)
        case 2:
            aEliminar=input("Ingrese el elemento a eliminar ")
            try:
                arreglo.remove(aEliminar)
            except ValueError:
                print("El dato no existe")
            else:
                print("Dato elininado")
        case 3:
            print("Deshaciendo la ultima accion")
            arreglo=undo.copy()
        case 4:
            for item in arreglo:
                print(item)
        case 5:
            break



