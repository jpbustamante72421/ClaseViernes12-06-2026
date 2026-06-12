from estructuras.lineales.nodo import Node
class Linkedlist: 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self,data):
        #Paso número 1: Crear un nuevo nodo con el dato a insertar
        new_node = Node(data)
        #Paso número 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            #Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            #Paso número 3: Si la lista no está vacía, el nuevo nodo apunta a la cabeza actual de la lista
            new_node.next = self.head
            #Paso número 4: El nuevo nodo se convierte en la nueva cabeza de la lista
            self.head = new_node    

    def print_linked_list(self):
        temp = self.head
        print("Head -> ", end="")
        while temp is not None:
            print(temp.data,"->", end="")
            temp = temp.next
        print("<- Tail")