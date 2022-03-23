import sys
from PyQt5.QtWidgets import QApplication

from backend.logica_inicio import LogicaInicio
from backend.logica_postnivel import LogicaPostNivel
from backend.logica_ranking import LogicaRanking
from backend.logica_juego import LogicaJuego
from backend.logica_juego import Rana
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_postnivel import VentanaPostNivel
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_juego import VentanaJuego

import parametros as p

if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    #Instanciacion de ventanas
    ventana_inicio = VentanaInicio()
    ventana_ranking = VentanaRanking()
    ventana_juego = VentanaJuego()
    ventana_postnivel = VentanaPostNivel()

    #Instanciacion de la lógica
    logica_inicio = LogicaInicio()
    logica_ranking = LogicaRanking()
    rana = Rana()
    logica_juego = LogicaJuego(
        rana, 
        p.VIDAS_INICIO, 
        p.DURACION_RONDA_INICIAL, 
        p.CANTIDAD_MONEDAS, 
        p.VELOCIDAD_TRONCOS, 
        p.VELOCIDAD_AUTOS
        )
    logica_postnivel = LogicaPostNivel()

    #***Conexion de señales***

    #Ventana de Inicio
    #ABRE VENTANA DE RANKING DESDE VENTANA DE INICIO
    ventana_inicio.senal_enviar_ranking.connect(
        logica_inicio.abrir_ranking
    )
    logica_inicio.senal_abrir_ranking.connect(
        ventana_ranking.mostrar
    )
    #OBTENER LISTA DE MEJORES PUNTAJES (Al apretar Ver Ranking)
    logica_inicio.senal_abrir_ranking.connect(
        logica_ranking.mandar_puntajes
    )
    logica_ranking.senal_lista_puntajes.connect(
        ventana_ranking.lista_mejores_puntajes
    )

    #Ventana de Ranking
    #ABRE VENTANA DE INICIO DESDE VENTANA DE RANKING
    ventana_ranking.senal_enviar_inicio.connect(
        logica_ranking.abrir_inicio
    )
    logica_ranking.senal_abrir_inicio.connect(
        ventana_inicio.mostrar
    )

    #Ventana de Juego
    #ABRE VENTANA DE JUEGO DESDE VENTANA DE INICIO
    ventana_inicio.senal_enviar_login.connect(
        logica_inicio.abrir_juego
    )
    logica_inicio.senal_abrir_juego.connect(
        ventana_juego.mostrar
    )
    #INICIA EL JUEGO
    logica_inicio.senal_abrir_juego.connect(
        logica_juego.iniciar_juego
    )
    #INICIAR AUTOS
    logica_juego.senal_iniciar_autos.connect(
        ventana_juego.iniciar_autos
    )
    logica_juego.senal_mover_autos.connect(
        ventana_juego.animar_autos
    )
    #INICIAR TRONCOS
    logica_juego.senal_iniciar_troncos.connect(
        ventana_juego.iniciar_troncos
    )
    logica_juego.senal_mover_troncos.connect(
        ventana_juego.animar_troncos 
    )
    #INICIAR RANA
    logica_juego.senal_iniciar_rana.connect(
        ventana_juego.iniciar_rana
    )
    #MOVIMIENTO RANA (se mueve el hitbox de la rana en el backend)
    ventana_juego.senal_enviar_posicion_rana.connect(
        rana.nueva_posicion_rana
    )
    #SENAL PARA PAUSAR EL JUEGO
    ventana_juego.senal_enviar_pausar_juego.connect(
        logica_juego.detener_juego
    )
    #SENAL PARA DES-PAUSAR EL JUEGO
    ventana_juego.senal_enviar_despausar_juego.connect(
        logica_juego.reanudar_juego
    )
    #REINICIAR RANA SI CHOCA CON ALGO
    logica_juego.senal_reiniciar_rana.connect(
        ventana_juego.reiniciar_posicion
    )
    #RANA ENCIMA DE UN TRONCO
    logica_juego.senal_rana_en_tronco.connect(
        ventana_juego.rana_en_tronco
    )
    #SEÑAL PARA MOSTRAR UN OBJETO EN VENTANA DE JUEGO
    logica_juego.senal_mostrar_objeto.connect(
        ventana_juego.mostrar_objeto
    )
    #SEÑAL PARA ELIMINAR UN OBJETO EN VENTANA DE JUEGO
    logica_juego.senal_eliminar_objeto.connect(
        ventana_juego.eliminar_objeto
    )
    #SENAL PARA ACTUALIZAR DATOS DEL JUEGO EN VENTANA DE JUEGO
    logica_juego.senal_actualizar_datos.connect(
        ventana_juego.actualizar_datos
    )
    #SENAL PARA CERRAR LA VENTANA DE JUEGO CUANDO SE GANA O PIERDE
    logica_juego.senal_cerrar_juego.connect(
        ventana_juego.esconder
    )

    #Ventana de PostNivel
    #SENAL PARA IR A VENTANA POSTNIVEL LUEGO DE PERDER
    logica_juego.senal_ir_postnivel.connect(
        ventana_postnivel.actualizar_atributos
    )
    #SENAL DE PARA ACTUALIZAR LOS VALORES DEL PROXIMO NIVEL
    ventana_postnivel.senal_actualizar_valores_juego.connect(
        logica_postnivel.actualizar_valores_nivel
    )
    logica_postnivel.senal_actualizar_valores_juego.connect(
        logica_juego.valores_nuevo_nivel
    )
    #SENAL PARA ABRIR EL JUEGO DESDE LA VENTANA DE POSTNIVEL
    ventana_postnivel.senal_abrir_juego.connect(
        ventana_juego.mostrar
    )
    ventana_postnivel.senal_abrir_juego.connect(
        logica_juego.reanudar_juego
    )
    #SENAL PARA ENVIAR DATA DE LOS JUGADORES AL RANKING
    ventana_postnivel.senal_data_ranking.connect(
        logica_postnivel.recibir_data_ranking
    )
    logica_postnivel.senal_data_ranking.connect(
        logica_ranking.actualizar_data_ranking
    )

    ventana_inicio.mostrar()

    sys.exit(app.exec_())