from threading import Thread, Event
from time import sleep
from random import randint


class Shopper(Thread):

    evento_disponible = Event()

    def __init__(self, nombre, velocidad):
        # No Modificar
        super().__init__()
        self.posicion = 0
        self.distancia_tienda = 0
        self.distancia_destino = 0
        self.pedido_actual = None
        self.termino_jornada = False
        # COMPLETAR DESDE AQUI
        self.nombre = nombre
        self.velocidad = velocidad

    @property
    def ocupado(self):
        # No Modificar
        if self.pedido_actual:
            return True
        return False

    def asignar_pedido(self, pedido):
        # No Modificar
        print(f"Asignando pedido {pedido.id_} a {self.nombre}...")
        self.distancia_tienda = randint(1, 10)
        self.distancia_destino = self.distancia_tienda +\
            pedido.distancia_destino
        self.pedido_actual = pedido
        self.posicion = 0
        print(f"El pedido {pedido.id_} fue asignado a {self.nombre}")

    def avanzar(self):
        # Completar
        self.posicion += 1
        sleep( 1 / self.velocidad )
        print(f"Shopper {self.nombre} avanzo a la posicion {self.posicion}")

    def run(self):
        # Completar 
        while not self.termino_jornada or self.ocupado:
            if self.ocupado:
                for _ in range(self.distancia_tienda + 1):
                    self.avanzar()

                self.posicion = 0

                print("El Shopper ha llegado a la Tienda")

            #DUDA ACA CON LOS EVENTOS ?????
                self.pedido_actual.evento_llego_repartidor.set()
                self.pedido_actual.evento_pedido_listo.wait()
                self.pedido_actual.evento_pedido_listo.clear()

                for _ in range(self.distancia_destino + 1):
                    self.avanzar()
            
                print(f"El Shopper {self.nombre} ha llegado a su destino")
                self.pedido_actual.entregado = True  
                self.evento_disponible.set()
                self.posicion = 0
                self.pedido_actual = None


if __name__ == "__main__":
    pass
