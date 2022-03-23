#class MenuInicio perteneciente al módulo menu_inicio.py para mostrar el Menú de Inicio
from menu_inicio import MenuInicio 

class DCComerce():

    def __init__(self):
        
        print("---🛒 ¡Bienvenid@s a DCComerce! 🛒---")

        menu_inicio = MenuInicio()
        menu_inicio.menu_inicio()

if __name__ == '__main__':
    dccomerce = DCComerce()