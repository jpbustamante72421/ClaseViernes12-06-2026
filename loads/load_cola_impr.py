import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import uic
from estructuras.aplicaciones.cola_impr import GestorImpresion

class VentanaImpresion(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Ruta absoluta para asegurar que cargue el archivo .ui
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ui_path = os.path.join(base_dir, "ui", "ColaImpresion.ui")
        
        uic.loadUi(ui_path, self)
        self.gestor = GestorImpresion()
        
        # Conexión de botones
        self.btnAgregar.clicked.connect(self.agregar_trabajo)
        self.btnImprimir.clicked.connect(self.procesar_trabajo)
        
        self.actualizar_interfaz()

    def agregar_trabajo(self):
        u = self.txtUsuario.text()
        d = self.txtDocumento.text()
        p = self.spinPaginas.value()
        
        if u and d:
            trabajo = self.gestor.agregar_trabajo(u, d, p)
            # Log de éxito
            self.txtLog.append(f"✅ Agregado: {d} (Usuario: {u})")
            
            # Limpiar campos para el siguiente
            self.txtUsuario.clear()
            self.txtDocumento.clear()
            self.spinPaginas.setValue(1)
            
            self.actualizar_interfaz()
        else:
            self.txtLog.append("⚠️ Error: Campos vacíos.")

    def procesar_trabajo(self):
        trabajo = self.gestor.procesar_siguiente()
        if trabajo:
            self.txtLog.append(f"🖨️ Procesando: {trabajo.documento} de {trabajo.usuario}")
        else:
            self.txtLog.append("⚠️ Advertencia: No hay trabajos en cola.")
            
        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        # Actualización de contadores
        cantidad = self.gestor.cola.size() if hasattr(self.gestor.cola, 'size') else 0
        self.lblTotal.setText(f"Pendientes: {cantidad}")
        
        # --- MEJORA: Mostrar usuario y documento al frente ---
        frente = self.gestor.consultar_frente()
        if frente is not None:
            # Se muestra el documento y el usuario en el label de frente
            texto_frente = f"Frente: {frente.documento} (Usuario: {frente.usuario})"
        else:
            texto_frente = "Frente: Vacío"
            
        self.lblFrente.setText(texto_frente)
        # ----------------------------------------------------
        
        # Actualización de tabla
        self.tblCola.setRowCount(0)
        items = []
        
        # Extraer todo para mostrar en tabla
        while not self.gestor.cola.isEmpty():
            items.append(self.gestor.cola.dequeue())
        
        # Llenar tabla y re-encolar
        for i, t in enumerate(items):
            self.tblCola.insertRow(i)
            self.tblCola.setItem(i, 0, QTableWidgetItem(str(t.consecutivo)))
            self.tblCola.setItem(i, 1, QTableWidgetItem(str(t.usuario)))
            self.tblCola.setItem(i, 2, QTableWidgetItem(str(t.documento)))
            self.tblCola.setItem(i, 3, QTableWidgetItem(str(t.paginas)))
            
            self.gestor.cola.enqueue(t)