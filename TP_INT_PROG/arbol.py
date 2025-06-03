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
            self.insertarRecursivo(self.raiz,dato)
    
    def mostrar(self):
        if self.raiz==None:
            print("Lista vacia!")
        else:
            self.mostrarInorderRec(self.raiz)
    #Inserta de forma recursiva.
    
    def insertarRecursivo(self,nodo,dato):
        #Si el dato nuevo es menor al dato del arbol existente, se prosigue hacia el nodo izquierdo
        if dato < nodo.dato:
            #si el nodo esta vacio, se crea un nodo nuevo y se apunta la referencia al mismo
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
            #Si no esta vacio, se continua avanzando por la izquierda
                self.insertarRecursivo(nodo.izquierda,dato)
        #Si el dato nuevo es mayor al dato del nodo, se prosigue hacia el nodo derecho
        else:
            #Si esta vacio, se crea un nodo nuevo y se apunta la referencia al mismo
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
            #Si no esta vacio, se continua avanzando por la derecha
                self.insertarRecursivo(nodo.derecha,dato)

    def mostrarInorderRec(self,nodo):
        if nodo.izquierda!=None:
            self.mostrarInorderRec(nodo.izquierda)
        print(nodo.dato)
        if nodo.derecha!=None:
            self.mostrarInorderRec(nodo.derecha)