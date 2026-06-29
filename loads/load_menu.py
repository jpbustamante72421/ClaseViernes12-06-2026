from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from loads.load_lista_enlazada_simple import DialogoListaEnlazada
from loads.load_dialogo_pila import DialogoPilas 
from loads.load_conversion_fijainfija import VentanaConversion

class MenuListaEnlazada(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ListaEnlazada.ui", self) 

        self.Lista_Enlazada.triggered.connect(self.abrir_ventana_lista)
        self.actionPilas.triggered.connect(self.abrir_ventana_pilas)
        self.actionConversion.triggered.connect(self.procesar_conversion)

    def abrir_ventana_lista(self):
        self.ventana_lista = DialogoListaEnlazada()
        self.ventana_lista.exec_()

    def abrir_ventana_pilas(self):
        self.ventana_pilas = DialogoPilas()
        self.ventana_pilas.exec_()
    
    def procesar_conversion(self):
        self.conversor = VentanaConversion()
        self.conversor.exec_()