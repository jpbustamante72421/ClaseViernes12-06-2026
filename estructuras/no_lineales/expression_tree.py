from estructuras.lineales.stack import Stack

class NodeExpression:
    def __init__(self, value):
        self.value = value  # valor almacenado
        self.left = None   # se inician sin hijos
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_expression_tree(self, tokens, operadores_validos={'+', '-', '*', '/', '^'}):
        """
        Construye el árbol de expresión a partir de una lista de tokens en postfijo
        y almacena la raíz en self.root.
        """
        pila = Stack()
        
        for token in tokens:
            if token in operadores_validos:
                right_node = pila.pop()
                left_node = pila.pop()
                
                operator_node = NodeExpression(value=token)
                operator_node.left = left_node
                operator_node.right = right_node
                
                pila.push(operator_node)
            else:
                operand_node = NodeExpression(value=token)
                pila.push(operand_node)
                
        self.root = pila.pop()

    # Métodos de recorrido recursivos
    def preorden(self):
        def _preorden(node):
            if node:
                print(node.value, end=" ")
                _preorden(node.left)
                _preorden(node.right)
        
        if not self.root:
            raise Exception("El árbol está vacío.")
        _preorden(self.root)
        print()

    def inorden(self):
        def _inorden(node):
            if node:
                _inorden(node.left)
                print(node.value, end=" ")
                _inorden(node.right)
        
        if not self.root:
            raise Exception("El árbol está vacío.")
        _inorden(self.root)
        print()

    def posorden(self):
        def _posorden(node):
            if node:
                _posorden(node.left)
                _posorden(node.right)
                print(node.value, end=" ")
        
        if not self.root:
            raise Exception("El árbol está vacío.")
        _posorden(self.root)
        print()