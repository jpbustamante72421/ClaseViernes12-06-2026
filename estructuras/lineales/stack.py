class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None  

    def push(self, dato):
        """Inserta un elemento en la parte superior (Top)"""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    def pop(self):
        """Elimina y retorna el elemento en la parte superior (Top)"""
        if not self.head:
            return None
        dato = self.head.dato
        self.head = self.head.next
        return dato

    def top(self):
        return self.head.dato if self.head else None

    def print_stack(self):
        if not self.head:
            print("Stack: Empty")
            return
        
        nodos = []
        actual = self.head
        while actual:
            nodos.append(str(actual.dato))
            actual = actual.next
        
        print("Top -> " + " -> ".join(nodos) + " -> Base")

    def is_empty(self):
        return self.head is None