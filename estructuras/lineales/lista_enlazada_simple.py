from estructuras.lineales.nodo import Node

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    def insert_at_end(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.head:
            self.head = nuevo_nodo
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo_nodo

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head: return
        if not self.head.next:
            self.head = None
            return
        actual = self.head
        while actual.next.next:
            actual = actual.next
        actual.next = None

    def search(self, dato):
        actual = self.head
        while actual:
            if str(actual.dato) == str(dato):
                return True
            actual = actual.next
        return False

    def get_list(self):
        """Genera el formato: Head -> 1 -> 2 -> 3 -> Tail"""
        nodos = []
        actual = self.head
        while actual:
            nodos.append(str(actual.dato))
            actual = actual.next
        
        if not nodos:
            return "Head -> None"
        
        return "Head -> " + " -> ".join(nodos) + " -> Tail"