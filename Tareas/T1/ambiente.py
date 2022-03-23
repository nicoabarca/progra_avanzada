from abc import ABC, abstractmethod
import parametros as p

class Ambiente(ABC):
    def __init__(self, nombre, eventos):
        self.nombre = nombre
        self.eventos = eventos

    @abstractmethod
    def calcular_dano(self):
        """
        Calcula el daño hecho por el evento del ambiente.
        """
        pass

    def __repr__(self):
        return f"Ambiente: {self.nombre} | Eventos :{self.eventos}"

class AmbientePlaya(Ambiente):
    def __init__(self, nombre, eventos):
        super().__init__(nombre, eventos)
        
    def calcular_dano(self, dano_evento):
        """
        Calcula el daño hecho por un evento del ambiente playa.
        """
        parte_dano = (0.4 * p.HUMEDAD_PLAYA + 
        0.2 * p.VELOCIDAD_VIENTOS_PLAYA + 
        int(dano_evento)) / 5

        dano = max(5, int(parte_dano))

        return dano

class AmbienteMontana(Ambiente):
    def __init__(self, nombre, eventos):
        super().__init__(nombre, eventos)

    def calcular_dano(self, dano_evento):
        """
        Calcula el daño hecho por el evento del ambiente montaña.
        """
        parte_dano = (0.1 * p.PRECIPITACIONES_MONTANA + 
        0.3 * p.NUBOSIDAD_MONTANA + 
        int(dano_evento)) / 5

        dano = max(5, int(parte_dano))

        return dano

class AmbienteBosque(Ambiente):
    def __init__(self, nombre, eventos):
        super().__init__(nombre, eventos)

    def calcular_dano(self, dano_evento):
        """
        Calcula el daño hecho por el evento del ambiente bosque.
        """
        parte_dano = (0.2 * p.VELOCIDAD_VIENTOS_BOSQUE + 
        0.1 * p.PRECIPITACIONES_MONTANA + 
        int(dano_evento)) / 5

        dano = max (5, int(parte_dano))

        return dano
