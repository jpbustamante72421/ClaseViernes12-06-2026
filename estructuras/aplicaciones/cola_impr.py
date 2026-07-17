from estructuras.lineales.queue import Queue

class TrabajoImpresion:
    def __init__(self, usuario, documento, paginas, consecutivo):
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas
        self.consecutivo = consecutivo

class GestorImpresion:
    def __init__(self):
        self.cola = Queue()
        self.contador = 1

    def agregar_trabajo(self, usuario, documento, paginas):
        trabajo = TrabajoImpresion(usuario, documento, paginas, self.contador)
        self.cola.enqueue(trabajo)
        self.contador += 1
        return trabajo

    def procesar_siguiente(self):
        return self.cola.dequeue() if not self.cola.isEmpty() else None

    def consultar_frente(self):
        # Nota: Asegúrate de que tu clase Queue tenga 'front()' o 'peek()'
        return self.cola.firstQueue() if hasattr(self.cola, 'firstQueue') else None