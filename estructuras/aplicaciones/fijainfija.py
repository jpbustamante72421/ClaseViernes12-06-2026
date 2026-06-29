''' 
Algoritmo de Conversión: Infija a Posfija

El algoritmo utiliza una **Pila (Stack)** para gestionar los operadores y paréntesis, manteniendo el orden de precedencia correcto.

1. **Operandos:** Se envían directamente a la cadena de resultado.
2. **Paréntesis '(':** Se apilan inmediatamente para marcar el inicio de un sub-bloque.
3. **Paréntesis ')':** Se desapilan todos los operadores de la pila hasta encontrar el '(' correspondiente, enviándolos al resultado.
4. **Operadores (+, -, *, /, $):** - Mientras el operador actual tenga menor o igual precedencia que el operador que está en el **top** de la pila, se desapila el contenido de la pila y se envía al resultado.
   - Finalmente, se apila el operador actual.
5. **Finalización:** Al terminar la expresión, se desapilan todos los operadores restantes en la pila hacia el resultado.
'''
# conversor.py
from estructuras.lineales.stack import Stack 
class InfijaAPosfija:
    def __init__(self):
        self.precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '$': 3}

    def convertir(self, expresion):
        pila = Stack()
        posfija = ""
        
        for conver in expresion:
            # Si es operando, añadir a la salida
            if conver.isalnum():
                posfija += conver
            # Si es paréntesis de apertura, pushear a la pila
            elif conver == '(':
                pila.push(conver)
            # Si es paréntesis de cierre, vaciar hasta encontrar apertura
            elif conver == ')':
                while not pila.is_empty() and pila.top() != '(':
                    posfija += pila.pop()
                pila.pop()  # Eliminar el '('
            # Si es operador
            else:
                while not pila.is_empty() and pila.top() != '(' and \
                      self.precedencia.get(pila.top(), 0) >= self.precedencia.get(conver, 0):
                    posfija += pila.pop()
                pila.push(conver)
        
        # Vaciar lo que quede en la pila
        while not pila.is_empty():
            posfija += pila.pop()
            
        return posfija