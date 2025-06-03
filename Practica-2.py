class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        self.siguiente=None

class Lista:
    def __init__(self):
        self.lista=None
    
    def insertar(self,nombre,precio,cantidad):
        nuevo=Producto(nombre,precio,cantidad)
        nuevo.siguiente=self.lista
        self.lista=nuevo
    
    def buscarProductoMasVendido(self):
        nombre=""
        cantidad=0
        auxiliar=self.lista
        while auxiliar.siguiente is not None:
            if auxiliar.cantidad > cantidad:
                cantidad=auxiliar.cantidad
                nombre=auxiliar.nombre
            auxiliar=auxiliar.siguiente
        print(f"El producto mas vendido es {nombre}, con {cantidad} unidades")

    def mostrarVentas(self):
        auxiliar=self.lista
        while auxiliar is not None:
            print(f"{auxiliar.nombre}, {auxiliar.precio}, {auxiliar.cantidad}")
            auxiliar=auxiliar.siguiente
    
    def cargarProducto(self):
        nombre=""
        precio=""
        cantidad=""

        while nombre!="fin":
            #Nombre
            while True:
                nombre = input("Ingrese el nombre del producto: ")
                
                if nombre=="":
                    print("Debe ingresar un nombre: ")
                if nombre=="fin" or nombre!="":
                    break
            #Precio
            while True:
                try:
                    precio=int(input("ingrese el precio "))
                    if(precio>0):
                        break
                except ValueError:
                    print("Dato invalido")
            
            #Cantidad
            while True:
                try:
                    cantidad=int(input("Ingrese la cantidad: "))
                    if cantidad>0:
                        break
                except ValueError:
                    print("Dato invalido")
            if nombre!="fin":
                self.insertar(nombre,precio,cantidad)
        
        
        
        self.buscarProductoMasVendido()

