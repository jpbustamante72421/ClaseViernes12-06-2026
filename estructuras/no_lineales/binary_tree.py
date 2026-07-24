class NodeTree:
    def __init__(self, value):
        self.value = value  # valor almacenado
        self.left = None   # se inician sin hijos
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None   # raíz del árbol
    
    def insertar(self, value):
        self.root = self._insertar(self.root, value) # Recibe solamente el valor con el que se desea agregar
    
    def _insertar(self, node, value): # Permite desplazar por los nodos de todo el árbol 
        if node is None: # Si el árbol está vacío, el valor de self.root será None.
            return NodeTree(value)
        if value < node.value:
            node.left = self._insertar(node.left, value)
        elif value > node.value:
            node.right = self._insertar(node.right, value)
        else:
            print("El valor ya existe en el árbol.") # NO SE CREA UN NODO DUPLICADO.
        return node 
    
    def buscar(self, value):
        return self._buscar(self.root, value)
    
    def _buscar(self, node, value): # Comienza la búsqueda desde la raíz y se desplaza por los nodos
        if node is None:
            return False # El Nodo no existe en el árbol
        if value == node.value:
            return True # El nodo es igual al que se está buscando
        if value < node.value:
            return self._buscar(node.left, value) # si es menor, va hacia la izquierda
        return self._buscar(node.right, value) # si es mayor va hacia la derecha
    
    def preorden(self): # Raíz → Izquierda → Derecha
        self._preorden(self.root)
        print() # inicia el recorrido
    
    def _preorden(self, node):
        if node is not None: # Cuando el método llega a una posición vacía, deja de realizar llamadas.
            print(node.value, end=" ")  # Muestra el valor del nodo actual.
            self._preorden(node.left) # Recorre el subárbol izquierdo.
            self._preorden(node.right) # Recorre el subárbol derecho.
    
    def inorden(self): # Izquierda → Raíz → Derecha
        self._inorden(self.root)
        print() # inicia el recorrido
    
    def _inorden(self, node):
        if node is not None:
            self._inorden(node.left) # Recorre el subárbol izquierdo.
            print(node.value, end=" ") # Muestra el valor del nodo actual.
            self._inorden(node.right) # Recorre el subárbol derecho.

    def posorden(self):  # Izquierda → Derecha → Raíz
        self._posorden(self.root)
        print() # inicia el recorrido
        
    def _posorden(self, node):
        if node is not None:
            self._posorden(node.left) # Recorre el subárbol izquierdo.
            self._posorden(node.right) # Recorre el subárbol derecho.
            print(node.value, end=" ") # Muestra el valor del nodo actual.
    
    def contar(self):
        """
        Regresa la cantidad total de nodos existentes en el árbol.
        """
        return self._contar_recursivo(self.root)

    def _contar_recursivo(self, nodo):
        # Si el nodo es None, debe contar cero.
        if nodo is None:
            return 0
        
        # Si existe un nodo, cuenta 1 + los nodos de la izquierda + los nodos de la derecha.
        return 1 + self._contar_recursivo(nodo.left) + self._contar_recursivo(nodo.right)