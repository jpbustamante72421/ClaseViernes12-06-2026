from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.lineales.stack import Stack

class DialogoPilas(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/pilas.ui", self)

        self.pila = Stack()

        # Conexiones de botones
        self.btn_push.clicked.connect(self.push)
        self.btn_pop.clicked.connect(self.pop)
        self.btn_top.clicked.connect(self.top_of_stack)
        self.btn_print.clicked.connect(self.print_stack)
    
    def push(self):
        dato = self.txt_dato.text()
        if dato.strip(): # Validamos que no esté vacío
            self.pila.push(dato)
            self.txt_dato.clear()
            self.print_stack() # Refrescamos la vista automáticamente
        else:
            QMessageBox.warning(self, "Error", "Ingrese un dato válido")

    def pop(self):
        eliminado = self.pila.pop()
        if eliminado:
            QMessageBox.information(self, "Éxito", f"Elemento eliminado: {eliminado}")
        else:
            QMessageBox.warning(self, "Error", "La pila está vacía")
        self.print_stack()

    def top_of_stack(self):
        top_val = self.pila.top()
        if top_val:
            QMessageBox.information(self, "Top", f"El elemento en el tope es: {top_val}")
        else:
            QMessageBox.warning(self, "Error", "La pila está vacía")

    def print_stack(self):
        nodos = []
        actual = self.pila.head
        while actual:
            nodos.append(str(actual.dato))
            actual = actual.next
        
        texto_visual = "Top -> " + " -> ".join(nodos) + " -> Base" if nodos else "Pila vacía"
        self.txt_pila.setText(texto_visual)