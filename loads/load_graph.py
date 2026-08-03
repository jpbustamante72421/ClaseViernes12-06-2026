import math
import os
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QGraphicsEllipseItem,
    QGraphicsLineItem,
    QGraphicsScene,
    QGraphicsTextItem,
    QMessageBox,
    QTableWidgetItem,
    QWidget,
)

from estructuras.no_lineales.graph import Graph


class GraphWindow(QWidget):
    """Ventana y controlador integral para la gestión de Grafos No Dirigidos en PyQt5."""

    def __init__(self):
        super().__init__()
        
        # Carga del archivo .ui utilizando uic de PyQt5
        ui_path = os.path.join(os.path.dirname(__file__), "../ui/grafo.ui")
        if os.path.exists(ui_path):
            uic.loadUi(ui_path, self)
        
        self.graph = Graph()  # Instancia de la estructura lógica del grafo[cite: 1]
        self.graph_scene = QGraphicsScene(self)

        # Inicialización de interfaces, eventos y vista del grafo
        self.configure_graph_interface()
        self.configure_graph_events()
        self.update_graph_view()

    def configure_graph_interface(self):
        if hasattr(self, "tblAdjacencyMatrix"):
            self.tblAdjacencyMatrix.setEditTriggers(
                QAbstractItemView.NoEditTriggers
            )
        if hasattr(self, "tblEdges"):
            self.tblEdges.setEditTriggers(
                QAbstractItemView.NoEditTriggers
            )
            self.tblEdges.setColumnCount(2)
            self.tblEdges.setHorizontalHeaderLabels([
                "Vértice 1",
                "Vértice 2"
            ])
        if hasattr(self, "txtAdjacencyList"):
            self.txtAdjacencyList.setReadOnly(True)
            
        if hasattr(self, "graphicsViewGraph"):
            self.graphicsViewGraph.setScene(self.graph_scene)
            self.graphicsViewGraph.setRenderHint(
                QPainter.Antialiasing
            )
            self.graphicsViewGraph.setAlignment(
                Qt.AlignCenter
            )

    def configure_graph_events(self):
        if hasattr(self, "btnAddVertex"):
            self.btnAddVertex.clicked.connect(self.add_vertex)
        if hasattr(self, "btnDeleteVertex"):
            self.btnDeleteVertex.clicked.connect(self.delete_vertex)
        if hasattr(self, "btnAddEdge"):
            self.btnAddEdge.clicked.connect(self.add_edge)
        if hasattr(self, "btnDeleteEdge"):
            self.btnDeleteEdge.clicked.connect(self.delete_edge)
        if hasattr(self, "btnClearGraph"):
            self.btnClearGraph.clicked.connect(self.clear_graph)
        if hasattr(self, "btnRedrawGraph"):
            self.btnRedrawGraph.clicked.connect(self.draw_graph)
        if hasattr(self, "txtVertex"):
            self.txtVertex.returnPressed.connect(self.add_vertex)

    def add_vertex(self):
        vertex = self.txtVertex.text()
        try:
            was_added = self.graph.add_vertex(vertex)
            if not was_added:
                QMessageBox.information(
                    self,
                    "Vértice existente",
                    "El vértice ya se encuentra registrado."
                )
                return
            self.txtVertex.clear()
            self.txtVertex.setFocus()
            self.update_graph_view()
        except ValueError as error:
            QMessageBox.warning(
                self,
                "No fue posible agregar el vértice",
                str(error)
            )

    def delete_vertex(self):
        vertex = self.cmbVertex.currentText()
        if not vertex:
            QMessageBox.warning(
                self,
                "Dato requerido",
                "Seleccione el vértice que desea eliminar."
            )
            return
        response = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Desea eliminar el vértice {vertex}?\n\nTambién se eliminarán todos sus arcos.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if response != QMessageBox.Yes:
            return
        self.graph.remove_vertex(vertex)
        self.update_graph_view()

    def add_edge(self):
        vertex1 = self.cmbOrigin.currentText()
        vertex2 = self.cmbDestination.currentText()
        if not vertex1 or not vertex2:
            QMessageBox.warning(
                self,
                "Datos requeridos",
                "Seleccione los dos vértices del arco."
            )
            return
        try:
            was_added = self.graph.add_edge(vertex1, vertex2)
            if not was_added:
                QMessageBox.information(
                    self,
                    "Arco existente",
                    f"El arco entre {vertex1} y {vertex2} ya existe."
                )
                return
            self.update_graph_view()
        except ValueError as error:
            QMessageBox.warning(
                self,
                "No fue posible agregar el arco",
                str(error)
            )

    def delete_edge(self):
        vertex1 = self.cmbOrigin.currentText()
        vertex2 = self.cmbDestination.currentText()
        if not vertex1 or not vertex2:
            QMessageBox.warning(
                self,
                "Datos requeridos",
                "Seleccione los dos vértices del arco."
            )
            return
        was_removed = self.graph.remove_edge(vertex1, vertex2)
        if not was_removed:
            QMessageBox.warning(
                self,
                "Arco inexistente",
                f"No existe un arco entre {vertex1} y {vertex2}."
            )
            return
        self.update_graph_view()

    def update_graph_view(self):
        self.update_vertex_comboboxes()
        self.update_adjacency_matrix()
        self.update_adjacency_list()
        self.update_edge_list()
        self.draw_graph()
        self.update_graph_status()
        self.update_graph_controls()

    def update_vertex_comboboxes(self):
        if not hasattr(self, "cmbVertex"):
            return
        vertices = self.graph.get_vertices()
        selected_vertex = self.cmbVertex.currentText()
        selected_vertex1 = self.cmbOrigin.currentText()
        selected_vertex2 = self.cmbDestination.currentText()

        self.cmbVertex.clear()
        self.cmbOrigin.clear()
        self.cmbDestination.clear()

        self.cmbVertex.addItems(vertices)
        self.cmbOrigin.addItems(vertices)
        self.cmbDestination.addItems(vertices)

        if selected_vertex in vertices:
            self.cmbVertex.setCurrentText(selected_vertex)
        if selected_vertex1 in vertices:
            self.cmbOrigin.setCurrentText(selected_vertex1)
        if selected_vertex2 in vertices:
            self.cmbDestination.setCurrentText(selected_vertex2)

    def update_adjacency_matrix(self):
        if not hasattr(self, "tblAdjacencyMatrix"):
            return
        vertices, matrix = self.graph.get_adjacency_matrix()
        size = len(vertices)
        self.tblAdjacencyMatrix.clear()
        self.tblAdjacencyMatrix.setRowCount(size)
        self.tblAdjacencyMatrix.setColumnCount(size)
        self.tblAdjacencyMatrix.setHorizontalHeaderLabels(vertices)
        self.tblAdjacencyMatrix.setVerticalHeaderLabels(vertices)

        for row_index, row in enumerate(matrix):
            for column_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(int(Qt.AlignCenter))
                self.tblAdjacencyMatrix.setItem(
                    row_index,
                    column_index,
                    item
                )
        self.tblAdjacencyMatrix.resizeColumnsToContents()
        self.tblAdjacencyMatrix.resizeRowsToContents()

    def update_adjacency_list(self):
        if not hasattr(self, "txtAdjacencyList"):
            return
        adjacency_list = self.graph.get_adjacency_list()
        lines = []
        for vertex, adjacent_vertices in adjacency_list.items():
            if adjacent_vertices:
                adjacent_text = ", ".join(adjacent_vertices)
            else:
                adjacent_text = "Sin conexiones"
            lines.append(f"{vertex}: {adjacent_text}")
        self.txtAdjacencyList.setPlainText("\n".join(lines))

    def update_edge_list(self):
        if not hasattr(self, "tblEdges"):
            return
        edges = self.graph.get_edges()
        self.tblEdges.clearContents()
        self.tblEdges.setRowCount(len(edges))
        self.tblEdges.setColumnCount(2)
        self.tblEdges.setHorizontalHeaderLabels([
            "Vértice 1",
            "Vértice 2"
        ])

        for row_index, edge in enumerate(edges):
            vertex1, vertex2 = edge
            item_vertex1 = QTableWidgetItem(vertex1)
            item_vertex2 = QTableWidgetItem(vertex2)
            item_vertex1.setTextAlignment(int(Qt.AlignCenter))
            item_vertex2.setTextAlignment(int(Qt.AlignCenter))
            self.tblEdges.setItem(row_index, 0, item_vertex1)
            self.tblEdges.setItem(row_index, 1, item_vertex2)

        self.tblEdges.resizeColumnsToContents()
        self.tblEdges.resizeRowsToContents()

    def draw_graph(self):
        """Dibuja el grafo dentro del QGraphicsView con distribución circular[cite: 1]."""
        if not hasattr(self, "graphicsViewGraph"):
            return
        self.graph_scene.clear()
        vertices = self.graph.get_vertices()
        edges = self.graph.get_edges()
        scene_width = 700
        scene_height = 500
        self.graph_scene.setSceneRect(0, 0, scene_width, scene_height)

        if not vertices:
            self.draw_empty_graph_message(scene_width, scene_height)
            return

        center_x = scene_width / 2
        center_y = scene_height / 2
        vertex_radius = 25
        layout_radius = min(scene_width, scene_height) / 2 - 70

        vertex_positions = {}
        if len(vertices) == 1:
            vertex_positions[vertices[0]] = (center_x, center_y)
        else:
            angle_step = (2 * math.pi) / len(vertices)
            for index, vertex in enumerate(vertices):
                angle = -math.pi / 2 + index * angle_step
                x = center_x + layout_radius * math.cos(angle)
                y = center_y + layout_radius * math.sin(angle)
                vertex_positions[vertex] = (x, y)

        self.draw_graph_edges(edges, vertex_positions)
        self.draw_graph_vertices(vertices, vertex_positions, vertex_radius)
        self.graphicsViewGraph.fitInView(
            self.graph_scene.sceneRect(),
            Qt.KeepAspectRatio
        )

    def draw_graph_edges(self, edges, vertex_positions):
        edge_pen = QPen(QColor(90, 90, 90))
        edge_pen.setWidth(2)
        for vertex1, vertex2 in edges:
            x1, y1 = vertex_positions[vertex1]
            x2, y2 = vertex_positions[vertex2]
            line = QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(edge_pen)
            line.setZValue(0)
            self.graph_scene.addItem(line)

    def draw_graph_vertices(
        self,
        vertices,
        vertex_positions,
        vertex_radius
    ):
        vertex_pen = QPen(QColor(30, 80, 140))
        vertex_pen.setWidth(2)
        vertex_brush = QBrush(QColor(210, 230, 250))

        for vertex in vertices:
            center_x, center_y = vertex_positions[vertex]
            circle = QGraphicsEllipseItem(
                center_x - vertex_radius,
                center_y - vertex_radius,
                vertex_radius * 2,
                vertex_radius * 2
            )
            circle.setPen(vertex_pen)
            circle.setBrush(vertex_brush)
            circle.setZValue(1)
            self.graph_scene.addItem(circle)

            text_item = QGraphicsTextItem(vertex)
            font = QFont()
            font.setBold(True)
            font.setPointSize(11)
            text_item.setFont(font)
            text_item.setDefaultTextColor(QColor(20, 20, 20))
            text_rectangle = text_item.boundingRect()
            text_item.setPos(
                center_x - text_rectangle.width() / 2,
                center_y - text_rectangle.height() / 2
            )
            text_item.setZValue(2)
            self.graph_scene.addItem(text_item)

    def draw_empty_graph_message(self, scene_width, scene_height):
        text_item = QGraphicsTextItem(
            "El grafo no contiene vértices."
        )
        font = QFont()
        font.setPointSize(14)
        text_item.setFont(font)
        text_item.setDefaultTextColor(QColor(100, 100, 100))
        text_rectangle = text_item.boundingRect()
        text_item.setPos(
            (scene_width - text_rectangle.width()) / 2,
            (scene_height - text_rectangle.height()) / 2
        )
        self.graph_scene.addItem(text_item)
        self.graphicsViewGraph.fitInView(
            self.graph_scene.sceneRect(),
            Qt.KeepAspectRatio
        )

    def update_graph_status(self):
        if hasattr(self, "lblGraphStatus"):
            vertex_count = self.graph.vertex_count()
            edge_count = self.graph.edge_count()
            self.lblGraphStatus.setText(
                f"Vértices: {vertex_count} | Arcos: {edge_count}"
            )

    def update_graph_controls(self):
        vertex_count = self.graph.vertex_count()
        edge_count = self.graph.edge_count()
        has_vertices = vertex_count > 0
        has_enough_vertices = vertex_count >= 2
        has_edges = edge_count > 0

        if hasattr(self, "cmbVertex"):
            self.cmbVertex.setEnabled(has_vertices)
        if hasattr(self, "btnDeleteVertex"):
            self.btnDeleteVertex.setEnabled(has_vertices)
        if hasattr(self, "cmbOrigin"):
            self.cmbOrigin.setEnabled(has_vertices)
        if hasattr(self, "cmbDestination"):
            self.cmbDestination.setEnabled(has_vertices)
        if hasattr(self, "btnAddEdge"):
            self.btnAddEdge.setEnabled(has_enough_vertices)
        if hasattr(self, "btnDeleteEdge"):
            self.btnDeleteEdge.setEnabled(has_edges)
        if hasattr(self, "btnClearGraph"):
            self.btnClearGraph.setEnabled(has_vertices)
        if hasattr(self, "btnRedrawGraph"):
            self.btnRedrawGraph.setEnabled(has_vertices)

    def clear_graph(self):
        if self.graph.is_empty():
            QMessageBox.information(
                self,
                "Grafo vacío",
                "El grafo no contiene elementos."
            )
            return
        response = QMessageBox.question(
            self,
            "Limpiar grafo",
            "¿Desea eliminar todos los vértices y arcos?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if response != QMessageBox.Yes:
            return
        self.graph.clear()
        self.update_graph_view()