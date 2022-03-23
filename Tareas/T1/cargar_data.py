from tributo import Tributo
from objeto import ObjetoArma, ObjetoConsumible, ObjetoEspecial
from ambiente import AmbienteBosque, AmbienteMontana, AmbientePlaya
from arena import Arena

def cargar_tributos(ruta):
    """
    Retorna una lista de Tributos, en base a la información en tributos.csv
    """
    lista_tributos = []
    with open(ruta, "r", encoding = "UTF-8") as archivo:
        for linea in archivo.readlines()[1:]:
            linea = linea.strip().split(",")
            tributo = Tributo( *linea)
            lista_tributos.append(tributo)

    return lista_tributos

def cargar_objetos(ruta):
    """
    Retorna una lista de Objetos, en base a la información en objetos.csv
    """
    lista_objetos = []
    with open(ruta, "r", encoding = "UTF-8" ) as archivo:
        for linea in archivo.readlines()[1:]:
            linea = linea.strip().split(",")
            if linea[1] == "arma":
                lista_objetos.append(ObjetoArma( *linea))
            elif linea[1] == "consumible":
                lista_objetos.append(ObjetoConsumible( *linea))
            else:
                lista_objetos.append(ObjetoEspecial( *linea))

    return lista_objetos

def cargar_ambientes(ruta):
    """
    Retorna una lista de Ambientes (AmbienteBosque, AmbientePlaya,
    AmbienteMontana), en base a la información en ambientes.csv
    """
    lista_ambientes = []
    with open(ruta, "r", encoding = "UTF-8") as archivo:
        for linea in archivo.readlines()[1:]:
            linea = linea.strip().split(",")
            eventos_linea = linea[1:]
            lista_eventos = [tuple(evento.split(";")) for evento in eventos_linea]
            if linea[0] == "bosque":
                lista_ambientes.append(AmbienteBosque(linea[0], lista_eventos))
            elif linea[0] == "playa":
                lista_ambientes.append(AmbientePlaya(linea[0], lista_eventos))
            else:
                lista_ambientes.append(AmbienteMontana(linea[0], lista_eventos))

    return lista_ambientes

def cargar_arenas(ruta):
    """
    Retorna una lista de Arenas, en base a la información en arenas.csv
    """
    lista_arenas = []
    with open (ruta, "r", encoding = "UTF-8") as archivo:
        for linea in archivo.readlines()[1:]:
            linea = linea.strip().split(",")
            lista_arenas.append(Arena( *linea))

    return lista_arenas

if __name__ == "__main__":
    print("cargar_data.py es un módulo para leer la data de los csv.")


