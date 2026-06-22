from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.lineales.lista_enlazada_simple import LinkedList

class DialogoListaEnlazada(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/insertarinicio.ui", self)
        
        # Inicializamos la lista de datos
        self.lista = LinkedList()

        # Conexiones
        self.btn_inicio.clicked.connect(self.insert_at_beginning)
        self.btn_final.clicked.connect(self.insert_at_end)
        self.btn_imprimir.clicked.connect(self.print_linked_list)
        self.btn_buscar.clicked.connect(self.search)
        self.btn_eliminar_ini.clicked.connect(self.delete_at_beginning)
        self.btn_eliminar_fin.clicked.connect(self.delete_at_end)

    def insert_at_beginning(self):
        dato = self.txt_dato.text()
        if dato:
            self.lista.insert_at_beginning(dato)
            self.txt_dato.clear()
            self.lbl_resultado.setText(self.lista.get_list())

    def insert_at_end(self):
        dato = self.txt_dato.text()
        if dato:
            self.lista.insert_at_end(dato)
            self.txt_dato.clear()
            self.lbl_resultado.setText(self.lista.get_list())

    def print_linked_list(self):
        self.lbl_resultado.setText(self.lista.get_list())

    def search(self):
        dato = self.txt_dato.text()
        if self.lista.search(dato):
            QMessageBox.information(self, "Búsqueda", f"Elemento {dato} encontrado.")
        else:
            QMessageBox.warning(self, "Búsqueda", f"Elemento {dato} no encontrado.")

    def delete_at_beginning(self):
        self.lista.delete_at_beginning()
        self.lbl_resultado.setText(self.lista.get_list())

    def delete_at_end(self):
        self.lista.delete_at_end()
        self.lbl_resultado.setText(self.lista.get_list())