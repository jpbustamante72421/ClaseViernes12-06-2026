from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.aplicaciones.banco import Banco

class DialogoBanco(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/bancoQueue.ui", self)
        self.banco = Banco()

        self.pushButton.clicked.connect(self.agregar_cliente)
        self.pushButton_2.clicked.connect(self.atender_cliente)
        self.pushButton_3.clicked.connect(self.cerrar_banco)

    def agregar_cliente(self):
        cliente = self.banco.agregar_cliente()
        if cliente:
            self.lineEdit.setText(str(cliente.turno))
            self.actualizar_cola()
        else:
            QMessageBox.warning(self, "Aviso", "El banco ya está cerrado para nuevos clientes.")

    def atender_cliente(self):
        cliente, espera = self.banco.atender_cliente()
        if cliente:
            m, s = divmod(int(espera.total_seconds()), 60)
            self.label_4.setText(f"Atendiendo Turno: {cliente.turno}\nEspera: {m}m {s}s")
        else:
            self.label_4.setText("No hay clientes en espera.")
        self.actualizar_cola()

    def actualizar_cola(self):
        actual = self.banco.cola_clientes.first
        if not actual:
            self.label_3.setText("No hay clientes en espera.")
        else:
            texto_lista = "Clientes en espera:\n"
            while actual:
                texto_lista += f"Turno {actual.valor.turno} - Ingresó: {actual.valor.hora_entrada.strftime('%H:%M:%S')}\n"
                actual = actual.next
            self.label_3.setText(texto_lista)

    def cerrar_banco(self):
        # 1. Bloqueamos nuevos ingresos
        self.banco.cerrar_banco()
        
        # 2. Verificamos si aún hay clientes para poder cerrar la ventana
        if not self.banco.cola_clientes.isEmpty():
            QMessageBox.information(self, "Cierre", "Se ha bloqueado la entrada.\nSiga atendiendo a los clientes restantes.")
        else:
            # Si ya no hay clientes, mostramos el reporte final
            total = self.banco.clientes_atendidos
            promedio = (self.banco.tiempo_total_espera.total_seconds() / total) if total > 0 else 0
            m, s = divmod(int(promedio), 60)
            QMessageBox.information(self, "Cierre", f"Banco finalizado.\nAtendidos: {total}\nPromedio: {m}m {s}s")
            self.close()