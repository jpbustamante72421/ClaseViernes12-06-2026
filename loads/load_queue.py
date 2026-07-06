from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.lineales.queue import Queue

class DialogoColas(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/queue.ui", self)

        self.cola = Queue()

        # Conexiones de botones
        self.btn_enqueue.clicked.connect(self.enqueue)
        self.btn_dequeue.clicked.connect(self.dequeue)
        self.btn_first.clicked.connect(self.first_queue)
        self.btn_last.clicked.connect(self.last_queue)
        self.btn_print.clicked.connect(self.print_queue)
    
    def enqueue(self):
        dato = self.txt_dato.text()
        if dato.strip(): # Validamos que no esté vacío
            self.cola.enqueue(dato)
            self.txt_dato.clear()
            self.print_queue() # Refrescamos la vista automáticamente
        else:
            QMessageBox.warning(self, "Error", "Ingrese un dato válido")

    def dequeue(self):
        eliminado = self.cola.dequeue()
        if eliminado:
            QMessageBox.information(self, "Éxito", f"Elemento eliminado: {eliminado}")
        else:
            QMessageBox.warning(self, "Error", "La cola está vacía")
        self.print_queue()

    def first_queue(self):
        first_val = self.cola.firstQueue()
        if first_val:
            QMessageBox.information(self, "First", f"El primer elemento es: {first_val}")
        else:
            QMessageBox.warning(self, "Error", "La cola está vacía")

    def last_queue(self):
        last_val = self.cola.lastQueue()
        if last_val:
            QMessageBox.information(self, "Last", f"El último elemento es: {last_val}")
        else:
            QMessageBox.warning(self, "Error", "La cola está vacía")

    def print_queue(self):
        nodos = []
        actual = self.cola.first
        while actual:
            nodos.append(str(actual.valor))
            actual = actual.next
        
        texto_visual = "First -> " + " -> ".join(nodos) + " <- Last" if nodos else "Cola vacía"
        self.lbl_resultado.setText(texto_visual)
