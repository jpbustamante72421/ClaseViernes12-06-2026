import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPen, QBrush, QFont
from PyQt5.QtCore import Qt, QRectF

# Importa tus clases existentes
from estructuras.no_lineales.expression_tree import ExpressionTree

class ExpressionTreeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # Carga el archivo .ui que creamos
        loadUi("ui/ArbolExpresion.ui", self)
        
        self.tree = ExpressionTree()
        
        # Conectar el botón al evento de procesamiento automático
        self.btn_procesar.clicked.connect(self.procesar_expresion)
        self.lineEdit_expresion.returnPressed.connect(self.procesar_expresion)

    def procesar_expresion(self):
        texto = self.lineEdit_expresion.text().strip()
        if not texto:
            QMessageBox.warning(self, "Advertencia", "Por favor ingresa una expresión postfija.")
            return
        
        tokens = texto.split()
        try:
            # 1. Construir el árbol con tu lógica
            self.tree.build_expression_tree(tokens)
            
            # 2. Generar automáticamente todas las conversiones en los campos de texto
            self.lineEdit_pre.setText(self.obtener_recorrido_preorden())
            self.lineEdit_in.setText(self.obtener_recorrido_inorden())
            self.lineEdit_post.setText(self.obtener_recorrido_postorden())
            
            # 3. Dibujar automáticamente el árbol en grande dentro del QGraphicsView
            self.dibujar_arbol_grafico()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al procesar la expresión:\n{str(e)}")

    # Métodos auxiliares para capturar los strings de los recorridos
    def obtener_recorrido_preorden(self):
        resultado = []
        def _pre(node):
            if node:
                resultado.append(str(node.value))
                _pre(node.left)
                _pre(node.right)
        _pre(self.tree.root)
        return " ".join(resultado)

    def obtener_recorrido_inorden(self):
        resultado = []
        def _in(node):
            if node:
                _in(node.left)
                resultado.append(str(node.value))
                _in(node.right)
        _in(self.tree.root)
        return " ".join(resultado)

    def obtener_recorrido_postorden(self):
        resultado = []
        def _post(node):
            if node:
                _post(node.left)
                _post(node.right)
                resultado.append(str(node.value))
        _post(self.tree.root)
        return " ".join(resultado)

    def dibujar_arbol_grafico(self):
        from PyQt5.QtWidgets import QGraphicsScene
        
        scene = QGraphicsScene()
        self.graphicsView_tree.setScene(scene)
        
        if not self.tree.root:
            return

        # Parámetros visuales para nodos grandes y claros
        radio_nodo = 25
        nivel_altura = 70

        # Algoritmo para calcular posiciones (Coordenadas X, Y) basadas en un recorrido recursivo
        def calcular_posiciones(node, nivel=0, x_min=0, x_max=800):
            if not node:
                return {}
            
            posiciones = {}
            x_actual = (x_min + x_max) / 2
            y_actual = 40 + (nivel * nivel_altura)
            posiciones[node] = (x_actual, y_actual)
            
            # Dividir el espacio horizontal para los hijos izquierdo y derecho
            if node.left:
                posiciones.update(calcular_posiciones(node.left, nivel + 1, x_min, x_actual))
            if node.right:
                posiciones.update(calcular_posiciones(node.right, nivel + 1, x_actual, x_max))
                
            return posiciones

        pos_dict = calcular_posiciones(self.tree.root, nivel=0, x_min=0, x_max=900)

        # Dibujar líneas conectoras (aristas) primero para que queden por debajo de los nodos
        pen_linea = QPen(Qt.black, 2)
        def dibujar_conexiones(node):
            if not node:
                return
            x1, y1 = pos_dict[node]
            if node.left:
                x2, y2 = pos_dict[node.left]
                scene.addLine(x1, y1, x2, y2, pen_linea)
                dibujar_conexiones(node.left)
            if node.right:
                x2, y2 = pos_dict[node.right]
                scene.addLine(x1, y1, x2, y2, pen_linea)
                dibujar_conexiones(node.right)

        dibujar_conexiones(self.tree.root)

        # Dibujar los nodos en grande (círculos con texto centrado)
        brush_nodo = QBrush(Qt.lightGray)
        pen_nodo = QPen(Qt.darkBlue, 2)
        font_nodo = QFont("Arial", 11, QFont.Bold)

        for node, (x, y) in pos_dict.items():
            # Círculo del nodo
            scene.addEllipse(x - radio_nodo, y - radio_nodo, radio_nodo * 2, radio_nodo * 2, pen_nodo, brush_nodo)
            
            # Texto dentro del nodo
            text_item = scene.addText(str(node.value), font_nodo)
            text_rect = text_item.boundingRect()
            text_item.setPos(x - text_rect.width() / 2, y - text_rect.height() / 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ExpressionTreeGUI()
    ventana.show()
    sys.exit(app.exec_())