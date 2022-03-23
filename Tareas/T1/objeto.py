from abc import ABC, abstractmethod
import parametros as p

class Objeto(ABC):
    def __init__(self, nombre, tipo, peso):
        super().__init__()
        self.nombre = nombre
        self.tipo = tipo
        self.peso = int(peso)

    @abstractmethod
    def entregar_beneficio(self, tributo):
        """
        Método que entrega un beneficio al tributo
        dependiendo de que tipo de objeto ocupe.
        """
        pass

    def __repr__(self):
        return f"{self.nombre}({self.tipo})"


class ObjetoConsumible(Objeto):
    def __init__(self, nombre, tipo, peso):
        super().__init__(nombre, tipo, peso)

    def entregar_beneficio(self, tributo):
        """
        Aumenta la energía del tributo y se imprime
        en pantalla cuanto ganó.
        """
        aumento = p.AUMENTAR_ENERGIA
        tributo.energia += aumento

        print(f"\n{tributo.nombre} ha ganado {aumento} de energía por comer {self.nombre}\n")    

class ObjetoArma(Objeto):
    def __init__(self, nombre, tipo, peso): 
        super().__init__(nombre, tipo, peso)

    def entregar_beneficio(self, tributo, arena):
        """
        Aumenta la fuerza del tributo y se imprime
        en pantalla cuanto ganó.
        """
        fuerza = tributo.fuerza * (p.PONDERADOR_AUMENTAR_FUERZA * arena.riesgo + 1)
        tributo.fuerza += int(fuerza)

        print(f"\n{tributo.nombre} ha ganado {int(fuerza)} de fuerza por usar {self.nombre}\n")

class ObjetoEspecial(Objeto):
    def __init__(self, nombre, tipo, peso): 
        super().__init__(nombre, tipo, peso)

    def entregar_beneficio(self, tributo, arena):
        """
        Aumenta la fuerza, energía, agilidad e ingenio 
        del tributo y se imprime en pantalla cuanto ganó.
        """
        fuerza_ganada = tributo.fuerza * (p.PONDERADOR_AUMENTAR_FUERZA * arena.riesgo + 1)
        tributo.fuerza += int(fuerza_ganada)
        tributo.energia += p.AUMENTAR_ENERGIA
        tributo.agilidad += p.AUMENTAR_AGILIDAD
        tributo.ingenio += p.AUMENTAR_INGENIO

        print(f"\n{tributo.nombre} ha recibido lo siguiente por ocupar {self.nombre}:")
        print(f"{int(fuerza_ganada)} de fuerza.")
        print(f"{p.AUMENTAR_ENERGIA} de energía.")
        print(f"{p.AUMENTAR_AGILIDAD} de agilidad.")
        print(f"{p.AUMENTAR_INGENIO} de ingenio.\n")
