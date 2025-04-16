#Actividad 8

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class ListaEnlazada:
    def __init__(self):
        self.lista=None

    def insertarAlPrincipio(self,dato):
        nuevo=Nodo(dato)
        nuevo.siguiente=self.lista
        self.lista=nuevo
    
    def insertarAlFinal(self,dato):
        nuevo=Nodo(dato)
        if self.lista==None:
            self.lista=nuevo
        else:
            iterador=self.lista
            while iterador.siguiente is not None:
                iterador=iterador.siguiente
            iterador.siguiente=nuevo

    def mostrar(self):
        if self.lista is not None:
            iterador=self.lista
            while iterador:
                print(iterador.dato)
                iterador=iterador.siguiente
        else:
            print("Lista Vacia!")

def Actividad8():
    listaSemana=ListaEnlazada()
    listaSemana.insertarAlPrincipio('Lunes')
    listaSemana.insertarAlPrincipio('Martes')
    listaSemana.insertarAlPrincipio('Miercoles')
    listaSemana.insertarAlPrincipio('Jueves')
    listaSemana.insertarAlPrincipio('Viernes')

    listaSemana.mostrar()


#Actividad 9

def invertirLista(lista):
    listaInvertida=ListaEnlazada()
    iterador=lista.lista

    while iterador:
        listaInvertida.insertarAlPrincipio(iterador.dato)
        iterador=iterador.siguiente
    return listaInvertida

def Actividad9():
    listaSemana=ListaEnlazada()
    listaSemana.insertarAlPrincipio('Lunes')
    listaSemana.insertarAlPrincipio('Martes')
    listaSemana.insertarAlPrincipio('Miercoles')
    listaSemana.insertarAlPrincipio('Jueves')
    listaSemana.insertarAlPrincipio('Viernes')

    listaInvertida=invertirLista(listaSemana)

    listaInvertida.mostrar()

Actividad9()