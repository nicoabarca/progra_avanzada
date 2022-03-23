from random import randint
from time import sleep
from pedido import Pedido
from shopper import Shopper
from threading import Thread


class DCComidApp(Thread):

    def __init__(self, shoppers, tiendas, pedidos):
        # NO MODIFICAR
        super().__init__()
        self.shoppers = shoppers
        self.pedidos = pedidos
        self.tiendas = tiendas

    def obtener_shopper(self):
        # Completar
        for shopper in self.shoppers:
            if shopper.ocupado == False:
                return shopper
        print("Todos los Shoppers estan ocupados")
        Shopper().evento_disponible.wait()
        Shopper().evento_disponible.clear()
        print("Se ha desoscupado un Shopper")
        self.obtener_shopper()

    def run(self):
        # Completar
        while len(self.pedidos) != 0:
            pedido = self.pedidos.pop(0)
            tienda_del_pedido = self.tiendas[pedido[1]]
            pedido_actual = Pedido(pedido[0], pedido[1], pedido[2])
            shopper = self.obtener_shopper()
            shopper.asignar_pedido(pedido_actual)
            tienda_del_pedido.ingresar_pedido(pedido_actual, shopper)
            
            trafico_de_red = randint(1, 5)
            sleep(trafico_de_red)



if __name__ == '__main__':
    pass
