from threading import Thread, Lock
from time import sleep
from random import randint


class Tienda(Thread):
    def __init__(self, nombre):
        # NO MODIFICAR
        super().__init__()
        self.nombre = nombre
        self.cola_pedidos = []
        self.abierta = True
        # COMPLETAR DESDE AQUI
        self.daemon = True
        self.lock = Lock()

    def ingresar_pedido(self, pedido, shopper):
        # Completar
        with self.lock:
            self.cola_pedidos.append((pedido, shopper))
        
    def preparar_pedido(self, pedido):
        # Completar
        tiempo_espera = randint(1, 10)
        print(f"El {pedido.id_} se demorará {tiempo_espera} en prepararse")
        sleep(tiempo_espera)
        print("Su pedido ya esta preparado")

    def run(self):
        # Completar
        while self.abierta:
            with self.lock:
                if len(self.cola_pedidos) != 0:
                #Este pedido es la tupla (pedido, shopper)
                    pedido = self.cola_pedidos.pop(0)
                    self.preparar_pedido(pedido[0])
                    pedido[0].evento_pedido_listo.set()
                    pedido[0].evento_llego_repartidor.wait()
                    pedido[0].evento_llego_repartidor.clear()
                    print("El pedido ha sido retirado")
                    print(f"Quedan {len(self.cola_pedidos)} por entregar")

                # elif len(self.cola_pedidos) == 0:
                #     break

                else:
                    tiempo_descanso = randint(1, 5)
                    print(f"La tienda {self.nombre} se tomara un descanso de {tiempo_descanso}")
                    sleep(tiempo_descanso)