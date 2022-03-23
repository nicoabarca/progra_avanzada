import random
from ambiente import AmbienteBosque, AmbientePlaya
import parametros as p

class Arena:
    def __init__(self, nombre, dificultad, riesgo):
        self.nombre = nombre
        self.dificultad = dificultad
        self.riesgo = float(riesgo)
        self.jugador = None 
        self.tributos = [] 
        self.ambientes = [] 
        self.objetos = [] 
        self.ambiente_actual = None

    def __repr__(self):
        return f"{self.nombre} | Dificultad: {self.dificultad} | Riesgo: {self.riesgo}"


    def ejecutar_evento(self):
        """
        Le resta cierta cantidad de vida a los tributos, en base al daño del evento
        y el ambiente actual. El evento sucede solo si se cumple la condición
        inicial.
        """
        posibilidad = random.uniform(0,1)
        if posibilidad >= p.PROBABILIDAD_EVENTO: #OCURRE EVENTO
            ambiente_actual = self.ambiente_actual
            evento_actual = random.choice(ambiente_actual.eventos)
            dano_por_evento = ambiente_actual.calcular_dano(evento_actual[1])
            print(f"\n({evento_actual[0]}) hizo {dano_por_evento} de daño a los tributos.")
            self.jugador.vida -= dano_por_evento
            for tributo in self.tributos:
                tributo.vida -= dano_por_evento
            
        else: #NO OCURRE EVENTO
            print("\nNo hubo evento")

    def encuentros(self, tributo, tributos_enemigos):
        """
        Imprime en pantalla los encuentros entre tributos durante una 
        simulación de hora y resta a la vida de los tributos atacados
        el daño hecho por el tributo atacante.
        """
        print("Encuentros entre tributos:")
        print("-------------------------")
        tributos_vivos = list(filter(lambda tributo: tributo.esta_vivo, tributos_enemigos))
        num_encuentros = int((self.riesgo * (len(tributos_vivos) + 1)) // 2)
        for _ in range(num_encuentros):
            
            tributos_vivos = list(filter(lambda tributo: tributo.esta_vivo, tributos_enemigos))
            tributos_vivos.append(tributo)

            tributo_atacante = random.choice(tributos_vivos)
            while tributo_atacante == tributo:
                tributo_atacante = random.choice(tributos_vivos)

            tributo_atacado = random.choice(tributos_vivos)
            while tributo_atacado == tributo_atacante:
                tributo_atacado = random.choice(tributos_vivos)

            tributo_atacante.atacar_tributos_enemigos(tributo_atacado)

    def cambio_ambiente_actual(self):
        """
        Método encargado de cambiar el ambiente luego de una 
        simulación de hora
        """
        if isinstance(self.ambiente_actual, AmbienteBosque):
            self.ambiente_actual = self.ambientes[1]
        elif isinstance(self.ambiente_actual, AmbientePlaya):
            self.ambiente_actual = self.ambientes[2]
        else:
            self.ambiente_actual = self.ambientes[0]

    def ambiente_proximo(self):
        """
        Método encargado de retornar el nombre del próximo 
        ambiente de la arena.
        """
        if isinstance(self.ambiente_actual, AmbienteBosque):
            return self.ambientes[1].nombre
        elif isinstance(self.ambiente_actual, AmbientePlaya):
            return self.ambientes[2].nombre
        else:
            return self.ambientes[0].nombre

                

