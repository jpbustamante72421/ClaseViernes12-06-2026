
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from loads.load_lista_enlazada_simple import DialogoListaEnlazada

class MenuListaEnlazada(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ListaEnlazada.ui", self) 

        self.Lista_Enlazada.triggered.connect(self.abrir_ventana_lista)

    def abrir_ventana_lista(self):
        from loads.load_lista_enlazada_simple import DialogoListaEnlazada
        self.ventana_secundaria = DialogoListaEnlazada()
        self.ventana_secundaria.show()