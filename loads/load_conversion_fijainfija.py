from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.aplicaciones.fijainfija import InfijaAPosfija  # Importamos la clase que creamos antes

class VentanaConversion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/conversión_infija-posfija.ui", self) # Asegúrate de que este archivo exista
        self.pushButton.clicked.connect(self.ejecutar_logica)
        self.pushButton_2.clicked.connect(self.ejecutar_evaluacion)

    def ejecutar_logica(self):
        # 1. Obtener datos
        expresion = self.lineEdit.text()
        
        # 2. Usar la clase lógica que creamos antes
        conversor = InfijaAPosfija()
        resultado = conversor.convertir(expresion)
        
        # 3. Mostrar resultado
        self.label_2.setText(resultado)
    
    def ejecutar_evaluacion(self):
        # 1. Obtener datos
        expresion_posfija = self.label_2.text()
        
        # 2. Usar la clase lógica que creamos antes
        conversor = InfijaAPosfija()
        resultado = conversor.evaluar(expresion_posfija)
        
        # 3. Mostrar resultado
        self.label_3.setText(str(resultado))