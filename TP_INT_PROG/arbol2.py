class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izquierda=None
        self.derecha=None
    

class ArbolBinario:
    def __init__(self):
        self.raiz=None

    def insertar(self,dato):
        if self.raiz==None:
            self.raiz=Nodo(dato)
        else:
            self.raiz=ArbolBinario.insertarRecursivo(self.raiz,dato)
    
    def mostrar(self):
        if self.raiz==None:
            print("Lista vacia!")
        else:
            mostrarInorder(self.raiz)
    #Inserta de forma recursiva.
    
    def insertarRecursivo(self, dato):
        #Si el dato nuevo es menor al dato del arbol existente, se prosigue hacia el nodo izquierdo
        if dato < self.dato:
            #si el nodo esta vacio, se crea un nodo nuevo y se apunta la referencia al mismo
            if self.izquierda is None:
                self.izquierda = Nodo(dato)
            else:
            #Si no esta vacio, se continua avanzando por la izquierda
                self.izquierda.insertarRecursivo(dato)
        #Si el dato nuevo es mayor al dato del nodo, se prosigue hacia el nodo derecho
        else:
            #Si esta vacio, se crea un nodo nuevo y se apunta la referencia al mismo
            if self.derecha is None:
                self.derecha = Nodo(dato)
            else:
            #Si no esta vacio, se continua avanzando por la derecha
                self.derecha.insertarRecursivo(dato)
