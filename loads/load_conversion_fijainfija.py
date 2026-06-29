from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.aplicaciones.fijainfija import InfijaAPosfija  # Importamos la clase que creamos antes

class VentanaConversion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/conversión_infija-posfija.ui", self) # Asegúrate de que este archivo exista
        self.pushButton.clicked.connect(self.ejecutar_logica)

    def ejecutar_logica(self):
        # 1. Obtener datos
        expresion = self.lineEdit.text()
        
        # 2. Usar la clase lógica que creamos antes
        conversor = InfijaAPosfija()
        resultado = conversor.convertir(expresion)
        
        # 3. Mostrar resultado
        self.label_2.setText(resultado)