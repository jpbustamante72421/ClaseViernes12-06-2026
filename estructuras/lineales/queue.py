class Node(object):
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self,valor):
        nuevo_nodo = Node(valor)
        if self.last is None:
            self.first=self.last=nuevo_nodo
        else:
            self.last.next=nuevo_nodo
            self.last=nuevo_nodo
    
    def dequeue(self):
        # Elimina el primer elemento que entró
        if self.isEmpty():
            return None
        temp = self.first
        self.first = temp.next
        if self.first is None:
            self.last = None
        return temp.valor

    def firstQueue(self):
        # Consulta el primer elemento sin eliminarlo
        return self.first.valor if self.first else None

    def lastQueue(self):
        # Consulta el último elemento sin eliminarlo
        return self.last.valor if self.last else None

    def printQueue(self):
        if self.isEmpty():
            print("Queue: Empty")
            return
        
        nodos = []
        actual = self.first
        while actual:
            nodos.append(str(actual.valor)) # Estandarizado a .valor
            actual = actual.next
        
        print("First -> " + " -> ".join(nodos) + " <- Last")
    
    def isEmpty(self):
        return self.first is None
 