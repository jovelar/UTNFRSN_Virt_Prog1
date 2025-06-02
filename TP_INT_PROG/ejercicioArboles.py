import arbol

arbolNuevo = arbol.NodoArbol(0)
arbolNuevo.insertarRecursivo(4000)
arbolNuevo.insertarRecursivo(5)
arbolNuevo.insertarRecursivo(9)
arbolNuevo.insertarRecursivo(21)
arbolNuevo.insertarRecursivo(60)

print("INORDER")
arbolNuevo.mostrarInorderRec()
print("POSTORDER")
arbolNuevo.mostrarPostOrderRec()
print("PREORDER")
arbolNuevo.mostrarPreOrderRec()
print("INVERTIDO")
arbolNuevo.mostrarInvertido()