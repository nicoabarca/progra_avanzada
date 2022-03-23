from PyQt5.QtCore import QObject, QPoint, pyqtSignal, QTimer, QThread, QRect
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from random import randint, choice

import os
import parametros as p

class LogicaJuego(QObject):
    senal_iniciar_rana = pyqtSignal()
    senal_iniciar_autos = pyqtSignal(list)
    senal_iniciar_troncos = pyqtSignal(list)
    senal_mover_autos = pyqtSignal(list)
    senal_mover_troncos = pyqtSignal(list)
    senal_mostrar_objeto = pyqtSignal(object)
    senal_eliminar_objeto = pyqtSignal(int) 
    senal_rana_en_tronco = pyqtSignal(int)
    senal_reiniciar_rana = pyqtSignal()
    senal_ir_postnivel = pyqtSignal(dict)
    senal_cerrar_juego = pyqtSignal()
    senal_actualizar_datos = pyqtSignal(dict)
    
    def __init__(self, rana, vidas, duracion_ronda, monedas, velocidad_troncos, velocidad_autos):
        super().__init__()

        self.rana = rana #objeto Rana
        self.vidas = vidas
        self.duracion_ronda = duracion_ronda
        self.monedas = monedas
        self.velocidad_troncos = velocidad_troncos
        self.velocidad_autos = velocidad_autos

        self.nombre = None
        self.puntaje_total = 0
        self.puntaje_nivel = 0
        self.tiempo = self.duracion_ronda
        self.nivel_actual = 1
        self.lista_autos = None
        self.lista_troncos = None
        self.lista_objetos = None
        self.lista_objetos_activos = []

        self.instanciar_timer()
    #Actualiza los valores del juego segun el nuevo nivel
    def valores_nuevo_nivel(self):
        self.duracion_ronda -= p.PONDERADOR_DIFICULTAD * self.duracion_ronda
        self.velocidad_troncos = int(self.velocidad_troncos * (2 / (1 + p.PONDERADOR_DIFICULTAD)))
        self.velocidad_autos = int(self.velocidad_autos * (2 / (1 + p.PONDERADOR_DIFICULTAD)))
        self.puntaje_nivel = 0
        self.tiempo = self.duracion_ronda
        self.nivel_actual += 1
        self.lista_objetos_activos = []
        self.senal_actualizar_datos.emit(self.datos_juego_actual())
        self.rana.reiniciar_posicion()
        self.senal_reiniciar_rana.emit()
    #Crea una lista de objetos Autos, con ciertos parametros iniciales
    def crear_autos(self):
        lista_autos = []
        pos_y_carreteras = [260, 300, 340, 620, 660, 700]
        for i in range(6): #son 6 autos
            if i % 2 == 0:
                lista_autos.append(Auto(-80, pos_y_carreteras[i], "right", self.velocidad_autos))
            else:
                lista_autos.append(Auto(1200, pos_y_carreteras[i], "left", self.velocidad_autos))
        self.senal_iniciar_autos.emit(lista_autos)
        self.lista_autos = lista_autos
    #Crea una lista de objetos Troncoes, con ciertos parametros iniciales
    def crear_troncos(self):
        lista_troncos = []
        pos_y_rio = [440, 480, 520]
        for i in range(3): #son 3 troncos
            if i % 2 == 0:
                lista_troncos.append(Tronco(-80, pos_y_rio[i], "right", self.velocidad_troncos))
            else:
                lista_troncos.append(Tronco(1200, pos_y_rio[i], "left", self.velocidad_troncos))
        self.senal_iniciar_troncos.emit(lista_troncos)
        self.lista_troncos = lista_troncos
    #Crea los Objetos especiales
    def crear_objetos(self):
        self.lista_objetos = [
            Objeto("calavera"), Objeto("corazon"), Objeto("moneda"), Objeto("reloj")
            ]
    #Se encarga de hacer aparecer los Qrect de los objetos y su sprite en el frontend
    def mostrar_objeto_aleatorio(self):
        objeto_elegido = choice(self.lista_objetos)
        objeto_elegido.posicion_aleatoria()
        self.lista_objetos_activos.append(objeto_elegido)
        self.senal_mostrar_objeto.emit(objeto_elegido)
    #Mueve el Qrect de los autos y los actualiza en el frontend
    def mover_autos(self):
        for auto in self.lista_autos:
            auto.mover()
        self.senal_mover_autos.emit(self.lista_autos)
    #Mueve el Qrect de los troncos y los actualiza en el frontend
    def mover_troncos(self):
        for tronco in self.lista_troncos:
            tronco.mover()
        self.senal_mover_troncos.emit(self.lista_troncos)
    #Detiene el timer
    def detener_juego(self):
        self.timer.stop()
    #Inicicia (o reanuda) el timer
    def reanudar_juego(self):
        self.timer.start()
    #Checkea si la rana choco con un objeto especial (medio buggeado) Retorna bool
    def colision_con_objetos(self):
        colisiona = False
        for (index, objeto) in enumerate(self.lista_objetos_activos):
            if self.rana.hitbox.intersects(objeto.hitbox):
                objeto.accion(self)
                objeto.eliminarse()
                self.lista_objetos_activos.pop(index)
                self.senal_eliminar_objeto.emit(index)
                colisiona = True
                break
        return colisiona
    #Checkea si la rana choco con uno de los bordes del mapa, Retorna bool
    def colision_con_bordes(self):
        colisiona = False
        if not (p.MIN_X <= self.rana.pos_x <= p.MAX_X - p.WIDTH_RANA):
            colisiona = True

        if not (p.MIN_Y <= self.rana.pos_y <= p.MAX_Y - p.HEIGHT_RANA):
            colisiona = True
        return colisiona
    #Checkea si la rana choco con uno de los autos del mapa, Retorna bool
    def colision_con_autos(self):
        colisiona = False
        for auto in self.lista_autos:
            if self.rana.hitbox.intersects(auto.hitbox):
                colisiona = True
        return colisiona
    #Checkea si la rana choco con uno de los troncos del mapa, Retorna bool
    #No pude lograr hacer que la rana se muriera si choca con el agua 
    def colision_con_troncos(self): 
        colisiona = False
        rio = QRect(20, 440, 1160, 120) 
        for tronco in self.lista_troncos:
            tronco_en_rio = rio.intersected(tronco.hitbox)
            rana_en_rio = 440 <= self.rana.hitbox.y() <= 560
            if self.rana.hitbox.intersects(tronco_en_rio):
                self.rana.hitbox.translate(tronco.direccion_int * tronco.velocidad, 0)
                self.senal_rana_en_tronco.emit(tronco.direccion_int)
            elif not self.rana.hitbox.intersects(tronco_en_rio):
                if rana_en_rio:
                    colisiona = True
        return colisiona
    #Retorna un diccionario de los atributos que se envian para ser actualizados en el frontend
    def datos_juego_actual(self):
        datos = {
            "nombre": str(self.nombre),
            'duracion': str(self.duracion_ronda),
            "nivel_actual" : str(self.nivel_actual),
            "vidas": str(self.vidas),
            "tiempo": str(self.tiempo),
            "monedas": str(self.monedas),
            "puntaje_total": str(self.puntaje_total),
            "puntaje_nivel": str(self.puntaje_nivel),
            "velocidad_auto": self.velocidad_autos,
            "velocidad_tronco": self.velocidad_troncos
        }
        return datos
    #Checkea si la rana llego al final
    def llegar_al_final(self):
        final = QRect(20, 210, 1160, 10)
        return self.rana.hitbox.intersects(final)
    #Calcula el puntaje que gano el jugador en el nivel
    def calculo_puntaje(self):
        self.puntaje_nivel = int((self.vidas * 100 + self.tiempo * 50) * self.nivel_actual)
        self.puntaje_total += self.puntaje_nivel
        print(self.puntaje_nivel)
        print(self.puntaje_total)
    #Instancia el timer
    def instanciar_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick)
        self.timer.setInterval(100)
        self.subtick = 0
    #Iniciar el timer, lo cual comienza el juego
    def iniciar_juego(self, nombre_usuario):
        self.nombre = nombre_usuario
        self.crear_troncos()
        self.crear_autos()
        self.crear_objetos()
        self.senal_iniciar_rana.emit()
        self.timer.start()
    #Ticks del timer (hace funcionar el juego)
    #Aca se checkean condiciones de termino, perdidas de vida
    #Se actualizan datos
    def timer_tick(self):
        self.tiempo -= 0.1
        self.subtick += 1
        if self.subtick == p.TIEMPO_OBJETOS: 
            self.mostrar_objeto_aleatorio()
            self.subtick = 0

        self.mover_autos()
        self.mover_troncos()
        
        choca_con_borde = self.colision_con_bordes()
        choca_con_auto = self.colision_con_autos()
        # choca_con_tronco = self.colision_con_troncos()
        choca_con_objeto = self.colision_con_objetos()
        if choca_con_borde or choca_con_auto:
            self.vidas -= 1
            print("La rana ha chocado con un borde o auto")
            self.rana.reiniciar_posicion()
            self.senal_reiniciar_rana.emit()
        elif choca_con_objeto:
            print("choco con un objeto")
        #CONDICIONES DE TERMINO DEL JUEGO
        if self.vidas == 0 or self.tiempo <= 0:
            datos = self.datos_juego_actual()
            self.timer.stop()
            self.senal_ir_postnivel.emit(datos)
            self.senal_cerrar_juego.emit()

        if self.llegar_al_final():
            self.timer.stop()
            self.calculo_puntaje()
            datos_con_puntajes = self.datos_juego_actual()
            self.senal_ir_postnivel.emit(datos_con_puntajes)
            self.senal_cerrar_juego.emit()

        #ACTUALIZACION DE DATOS DEL FRONTEND
        else:
            datos = self.datos_juego_actual()
            self.senal_actualizar_datos.emit(datos)

class Rana(QObject):

    def __init__(self):
        super().__init__()
        self.pos_x = 600         
        self.pos_y = 750
        self.hitbox = QRect(self.pos_x, self.pos_y, p.WIDTH_RANA, p.HEIGHT_RANA)
    #Actualiza la posicion del Qrect de la Rana
    def nueva_posicion_rana(self, lista_pos_rana): 
        self.hitbox.moveTo(lista_pos_rana[0], lista_pos_rana[1]) 
        self.pos_x, self.pos_y = self.hitbox.x(), self.hitbox.y()
    #Si la rana muere, se reinicia su posicion a la inicial
    def reiniciar_posicion(self):
        self.hitbox.moveTo(600, 750)
        self.pos_x, self.pos_y = self.hitbox.x(), self.hitbox.y()
        

class Auto(QObject):
    def __init__(self, pos_inicial_x, pos_inicial_y, direccion, velocidad):
        super().__init__()
        self.pos_inicial_x = pos_inicial_x
        self.pos_inicial_y = pos_inicial_y
        self.direccion = direccion 
        self.velocidad = velocidad
        self.hitbox = QRect(self.pos_inicial_x, self.pos_inicial_y, p.WIDTH_AUTO, p.HEIGHT_AUTO)
        self.sprite = None
    #Le asigna un int al atributo direccion (str)
    @property
    def direccion_int(self):
        return 1 if self.direccion == "right" else -1
    #Retorna las coordenadas x e y del Qrect del Auto
    @property
    def posicion(self):
        return self.hitbox.getCoords()[:2]
    #Funcion que se llama en el frontend para inicializar el sprite del Auto
    def inicializar_sprite(self, contexto):
        self.sprite = QLabel(contexto)
        self.sprite.setScaledContents(True)
        self.sprite.setGeometry(
            self.pos_inicial_x, self.pos_inicial_y, p.WIDTH_AUTO, p.HEIGHT_AUTO
            )
        self.sprite.setStyleSheet("border:1px solid black")
        if self.direccion == "right":
            self.sprite.setPixmap(QPixmap(p.RUTA_AUTO_RIGHT))
        else:
            self.sprite.setPixmap(QPixmap(p.RUTA_AUTO_LEFT))
        self.sprite.show()
    #Mueve el auto (se mueve gracias a los ticks del timer)
    def mover(self):
        if -80 <= self.posicion[0] <= 1200:
            self.hitbox.translate(self.direccion_int * self.velocidad, 0)
        else:
            self.reiniciar_posicion()
    #Cuando el auto sale de pantalla, vuelve a su posicion inicial
    def reiniciar_posicion(self):
        self.hitbox.moveTo(self.pos_inicial_x, self.pos_inicial_y)
        
class Tronco(QObject):
    def __init__(self, pos_inicial_x, pos_inicial_y, direccion, velocidad):
        super().__init__()
        self.pos_inicial_x = pos_inicial_x
        self.pos_inicial_y = pos_inicial_y
        self.direccion = direccion 
        self.velocidad = velocidad
        self.hitbox = QRect(
            self.pos_inicial_x, self.pos_inicial_y, p.WIDTH_TRONCO, p.HEIGHT_TRONCO
            )
        self.sprite = None
    #Le asigna un int al atributo direccion (str)
    @property
    def direccion_int(self):
        return 1 if self.direccion == "right" else -1
    #Retorna las coordenadas x e y del Qrect del Tronco
    @property
    def posicion(self):
        return self.hitbox.getCoords()[:2]
    #Funcion que se llama en el frontend para inicializar el sprite del Tronco
    def inicializar_sprite(self, contexto):
        self.sprite = QLabel(contexto)
        self.sprite.setScaledContents(True)
        self.sprite.setGeometry(
            self.pos_inicial_x, self.pos_inicial_y, p.WIDTH_TRONCO, p.HEIGHT_TRONCO
            )
        self.sprite.setPixmap(QPixmap(p.RUTA_TRONCO))
        self.sprite.setStyleSheet("border:1px solid black")
        self.sprite.show()
    #Mueve el auto (se mueve gracias a los ticks del timer)
    def mover(self):
        if -80 <= self.posicion[0] <= 1200:
            self.hitbox.translate(self.direccion_int * self.velocidad, 0)
        else:
            self.reiniciar_posicion()
    #Cuando el tronco sale de pantalla, vuelve a su posicion inicial
    def reiniciar_posicion(self):
        self.hitbox.moveTo(self.pos_inicial_x, self.pos_inicial_y)

class Objeto(QObject):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo  #"calavera", "corazon", "moneda", "reloj"
    #Genera un Qrect del objeto en una posicion aleatoria del mapa
    def posicion_aleatoria(self):
        self.pos_x = randint(p.MIN_X, p.MAX_X - 40)
        self.pos_y = randint(p.MIN_Y + 40, p.MAX_Y - 40)
        if 440 <= self.pos_y <= 660:
            self.pos_y += 50 #este if esta por si el objeto cae en el rio
        self.hitbox = QRect(self.pos_x, self.pos_y, p.WIDTH_OBJETO, p.HEIGHT_OBJETO)
    #Funcion que se llama en el frontend para inicializar el sprite del Objeto
    def inicializar_sprite(self, contexto):
        self.sprite = QLabel(contexto)
        self.sprite.setScaledContents(True)
        self.sprite.setGeometry(self.pos_x, self.pos_y, p.WIDTH_OBJETO, p.HEIGHT_OBJETO)
        self.sprite.setPixmap(QPixmap(os.path.join(p.RUTA_OBJETO, f"{self.tipo}.png")))
        self.sprite.show()
    #Al intersectar con la rana, el objeto se elimina
    def eliminarse(self):
        self.hitbox.setWidth(0)
        self.hitbox.setHeight(0)
    #Este metodo provoca los cambios en la logica del juego al tomar un objeto
    def accion(self, contexto):
        if self.tipo == "calavera":
            for tronco in contexto.lista_troncos:
                tronco.velocidad += 0.05 * tronco.velocidad
        elif self.tipo == "corazon":
            contexto.vidas += 1
        elif self.tipo == "moneda":
            contexto.monedas += 1
        elif self.tipo == "reloj":
            adicional = 10 * int(contexto.tiempo / contexto.duracion_ronda)
            contexto.tiempo += adicional