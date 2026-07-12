import datetime
from estructuras.lineales.queue import Queue

class Cliente:
    def __init__(self, turno):
        self.turno = turno
        self.hora_entrada = datetime.datetime.now()

    def tiempo_espera(self):
        return datetime.datetime.now() - self.hora_entrada

class Banco:
    def __init__(self):
        self.cola_clientes = Queue()
        self.turno_actual = 1
        self.clientes_atendidos = 0
        self.tiempo_total_espera = datetime.timedelta()
        self.banco_abierto = True

    def agregar_cliente(self):
        if not self.banco_abierto:
            return None
        cliente = Cliente(self.turno_actual)
        self.cola_clientes.enqueue(cliente)
        self.turno_actual += 1
        return cliente

    def atender_cliente(self):
        if not self.cola_clientes.isEmpty():
            cliente = self.cola_clientes.dequeue()
            espera = cliente.tiempo_espera()
            self.clientes_atendidos += 1
            self.tiempo_total_espera += espera
            return cliente, espera
        return None, None

    def cerrar_banco(self):
        # Bloqueamos ingresos sin importar si hay gente en cola
        self.banco_abierto = False
        # Retornamos True siempre, porque el banco ya está en "modo cierre"
        return True