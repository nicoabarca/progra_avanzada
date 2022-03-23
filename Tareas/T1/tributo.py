import parametros as p

class Tributo():
    def __init__(self, nombre, distrito, edad, vida, energia, 
                agilidad, fuerza, ingenio, popularidad):
        self.nombre = nombre
        self.distrito = distrito
        self.edad = int(edad)
        self.agilidad = int(agilidad)
        self.fuerza = int(fuerza)
        self.ingenio = int(ingenio)
        self.mochila = []
        self.peso = 0
        self.__esta_vivo = True
        self.__vida = int(vida) 
        self.__energia = int(energia) 
        self.__popularidad = int(popularidad) 

    @property
    def esta_vivo(self):
        return self.__esta_vivo

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if 1 <= valor <= 100:
            self.__vida = valor
        else:
            self.__vida = 0
            self.morir()

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        if 1 <= valor <= 100:
            self.__energia = valor
        elif valor > 100:
            self.__energia = 100
        else:
            self.__energia = 0

    @property
    def popularidad(self):
        return self.__popularidad

    def morir(self):
        """
        Cambia el valor del atributo esta_vivo a False.
        """
        self.__esta_vivo = False

    def __repr__(self):
        return f"{self.nombre} | {self.distrito} | {str(self.edad)}"

    def atacar(self, tributo_atacado):
        """
        Este método retorna True si el tributo jugador le hace daño
        al tributo atacado y se imprime el resultado de este ataque,
        en caso de que el tributo jugador no tenga energía para atacar
        retorna False y se imprime en pantalla que falta energía.
        """
        if self.__energia >= p.ENERGIA_ATACAR:
            self.__energia -= p.ENERGIA_ATACAR
            parte_dano = ((60 * self.fuerza) + (40 * self.agilidad) +
             (40 * self.ingenio) - (30 * self.peso))/ self.edad

            dano = min(90, max(5, parte_dano))

            tributo_atacado.vida -= int(dano)

            if not tributo_atacado.esta_vivo:
                self.__popularidad += p.POPULARIDAD_ATACAR
                print(f"\n{self.nombre} mató a {tributo_atacado.nombre}.\n")
                print(f"{self.nombre} ganó {p.POPULARIDAD_ATACAR} de popularidad.\n")
            else:
                print(f"\n{self.nombre} le hizo {int(dano)} de daño a {tributo_atacado.nombre}.\n")
            print(f"{self.nombre} tiene aún {self.__energia} de energía.\n")
            return True
        return False

    def accion_heroica(self):
        """
        Este método retorna True si el tributo jugador puede hacer
        una acción heroíca y se aplican los beneficios de esta. En
        caso de que el tributo jugador no pueda hacer una acción heroica
        se retorna False. Para los dos casos se imprime en pantalla el resultado.
        """
        if self.__energia >= p.ENERGIA_ACCION_HEROICA:
            self.__energia -= p.ENERGIA_ACCION_HEROICA
            self.__popularidad += p.POPULARIDAD_ACCION_HEROICA
            print(f"\n{self.nombre} ganó {p.POPULARIDAD_ACCION_HEROICA} de popularidad.")
            print(f"{self.nombre} tiene aún {self.__energia} de energía.\n")
            return True
        return False

    def utilizar_objeto(self, objeto, arena): 
        """
        Este método recibe un objeto como paramétro, el cuál ocupa
        y se elimina de la mochila de este.
        """
        if objeto.tipo == "consumible":
            objeto.entregar_beneficio(self)
        else:
            objeto.entregar_beneficio(self, arena)
        self.mochila.remove(objeto)
        self.peso -= objeto.peso

    def pedir_objeto(self, objeto): 
        """
        Retorna True si el tributo jugador pudo pedir un objeto a los 
        patrocinadores y este se agrega a la mochila. En caso contrario
        retorna False y no se agrega el objeto a la mochila.
        """
        if self.__popularidad >= (p.POPULARIDAD_PEDIR + p.COSTO_OBJETO):
            self.__popularidad -= (p.POPULARIDAD_PEDIR + p.COSTO_OBJETO)
            self.peso += objeto.peso
            self.mochila.append(objeto)
            print(f"\n{self.nombre} ha recibido el objeto: {objeto.nombre} ({objeto.tipo})\n")
            return True
        return False

    def hacerse_bolita(self):
        """
        Método que suma energía al atributo de energía del tributo
        """
        self.__energia += p.ENERGIA_BOLITA
        print(f"\n{self.nombre} ha ganado {p.ENERGIA_BOLITA} de energía por hacerse bolita.\n")

    def atacar_tributos_enemigos(self, tributo_atacado):
        """
        Método que resta vida al tributo atacado pero no
        le resta energia al tributo atacante. Se imprime
        el resultado de esta interacción.
        """
        parte_dano = ((60 * self.fuerza) + (40 * self.agilidad) +
             (40 * self.ingenio) - (30 * self.peso))/ self.edad

        dano = min(90, max(5, parte_dano))

        tributo_atacado.vida -= int(dano)

        if not tributo_atacado.esta_vivo:
                print(f"{self.nombre} mató a {tributo_atacado.nombre}.")

        else:
                print(f"{self.nombre} le hizo {int(dano)} de daño a {tributo_atacado.nombre}.")





