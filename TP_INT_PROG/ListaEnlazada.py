class NodoLista:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class Lista:
    def __init__(self):
        self.lista=None
    
    def insertar(self,dato):
        self.insertarOrdenadoRec(self.lista,dato)

    def insertarOrdenadoRec(nodo,dato):
        if nodo.lista==None:
            nodo.lista=NodoLista(dato)
        else:
            if nodo.lista.dato>dato:
                nuevoNodo=NodoLista(dato)
                #Apuntamos el nodo al siguiente del nodo actual, para poder insertar el nuevo en el medio
                nuevoNodo.siguiente=self.lista.siguiente
                #Apuntamos el nodo actual siguiente al nodo nuevo
                nodo.lista.siguiente=nuevoNodo
            else:
                nodo.insertarOrdenadoRec(nodo.lista.siguiente,dato)