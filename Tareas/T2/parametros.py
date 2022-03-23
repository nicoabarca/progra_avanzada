import os

#Teclas de Movimiento y Velocidad de Movimiento Rana
TECLA_ARRIBA = "w"
TECLA_IZQUIERDA = "a"
TECLA_ABAJO = "s"
TECLA_DERECHA = "d"

#Parametros Ventana de Inicio
MIN_CARACTERES = 4
MAX_CARACTERES = 15

#Parametros Ventana de Ranking

#Parametros Ventana de Juego
MOVIMIENTO = 10
PIXELES_SALTO = 40
VIDAS_INICIO = 3
TIEMPO_AUTOS = 1 #CAMBIARLO DESPUES
TIEMPO_TRONCOS = 1 #CAMBIARLO DESPUES
TIEMPO_OBJETOS = 60
CANTIDAD_MONEDAS = 0 #BONUS, CAMBIARLO DESPUES

DURACION_RONDA_INICIAL = 60
VELOCIDAD_AUTOS = 10 #CAMBIARLO DESPUES
VELOCIDAD_TRONCOS = 10 #CAMBIARLO DESPUES
PONDERADOR_DIFICULTAD = 0.1

#Parametros Ventana de Post-Nivel

#Parametros Logica Juego
MIN_X = 20
MAX_X = 1180
MIN_Y = 210
MAX_Y = 790
WIDTH_RANA = 30
HEIGHT_RANA = 30
WIDTH_AUTO = 100
HEIGHT_AUTO = 40
WIDTH_TRONCO = 100
HEIGHT_TRONCO = 40
WIDTH_OBJETO = 30
HEIGHT_OBJETO = 30

#Parametros generales y paths
RUTA_LOGO = os.path.join("frontend", "assets", "sprites", "Logo.png")

#sprites/Mapa/areas
RUTA_CARRETERA = os.path.join("frontend", "assets", "sprites", "Mapa", "areas", "carretera.png")
RUTA_PASTO = os.path.join("frontend", "assets", "sprites", "Mapa", "areas", "pasto.png")
RUTA_RIO = os.path.join("frontend", "assets", "sprites", "Mapa", "areas", "rio.png")

#sprites/Mapa/autos
RUTA_AUTO_RIGHT = os.path.join("frontend", "assets", "sprites", "Mapa", "autos", "morado_right.png")
RUTA_AUTO_LEFT = os.path.join("frontend", "assets", "sprites", "Mapa", "autos", "morado_left.png")
RUTA_TRONCO = os.path.join("frontend", "assets", "sprites", "Mapa", "elementos", "tronco.png")

#sprites/Objetos
RUTA_OBJETO = os.path.join("frontend", "assets", "sprites", "Objetos")
RUTA_CALAVERA = os.path.join("frontend", "assets", "sprites", "Objetos", "calavera.png")
RUTA_CORAZON = os.path.join("frontend", "assets", "sprites", "Objetos", "corazon.png")
RUTA_MONEDA = os.path.join("frontend", "assets", "sprites", "Objetos", "moneda.png")
RUTA_RELOJ = os.path.join("frontend", "assets", "sprites", "Objetos", "reloj.png")

#sprites/Personajes
RUTA_RANA_UP1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Verde", "up_1.png")