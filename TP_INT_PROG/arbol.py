#Arbol Binario
class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

    #Inserta de forma recursiva.
    def insertarRecursivo(self, dato):
        #Si el dato nuevo es menor al dato del arbol existente, se prosigue hacia el nodo izquierdo
        if dato < self.dato:
            #si el nodo esta vacio, se crea un nodo nuevo y se apunta la referencia al mismo
            if self.izquierda is None:
                self.izquierda = NodoArbol(dato)
            else:
            #Si no esta vacio, se continua avanzando por la izquierda
                self.izquierda.insertarRecursivo(dato)
        #Si el dato nuevo es mayor al dato del nodo, se prosigue hacia el nodo derecho
        else:
            #Si esta vacio, se crea un nodo nuevo y se apunta la referencia al mismo
            if self.derecha is None:
                self.derecha = NodoArbol(dato)
            else:
            #Si no esta vacio, se continua avanzando por la derecha
                self.derecha.insertarRecursivo(dato)
    
    #Muestra Ordenado
    def mostrarInorderRec(self):
        if self.izquierda!=None:
            self.izquierda.mostrarInorderRec()
        print(self.dato)
        if self.derecha!=None:
            self.derecha.mostrarInorderRec()
    
    #Muestra antes de avanzar. La lista se muestra como fue cargada
    def mostrarPreOrderRec(self):
        print(self.dato)
        if self.izquierda!=None:
            self.izquierda.mostrarPreOrderRec()
        if self.derecha!=None:
            self.derecha.mostrarPreOrderRec()
    
    #Muestra la lista invertida a como fue cargada
    def mostrarPostOrderRec(self):
        if self.izquierda!=None:
            self.izquierda.mostrarPostOrderRec()
        if self.derecha!=None:
            self.derecha.mostrarPostOrderRec()
        print(self.dato)

        #Muestra Ordenado
    def mostrarInvertido(self):        
        if self.derecha!=None:
            self.derecha.mostrarInvertido()
        print(self.dato)
        if self.izquierda!=None:
            self.izquierda.mostrarInvertido()