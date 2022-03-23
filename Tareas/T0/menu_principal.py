import menu_inicio as mi
import menu_publicaciones as mp
import menu_publicaciones_realizadas as mpubr

class MenuPrincipal:

    def __init__(self, usuario):
        self.usuario = usuario 

        self.menu_principal()
        
    #MENU PRINCIPAL
    def menu_principal(self):
        print(f"""
🟪 Menu Principal 🟪

Usuario: {self.usuario}

[1] Menú de Publicaciones
[2] Menú de Publicaciones Realizadas
[3] Volver
""" )

        input_usuario = input("🟢 Indique su opción: ")

        if input_usuario == str(1):
            mp.MenuPublicaciones(self.usuario)
        
        elif input_usuario == str(2):
            mpubr.MenuPublicacionesRealizadas(self.usuario)


        elif input_usuario == str(3):
                mi.MenuInicio().menu_inicio()
            
        else:
            print("\n⚠️ POR FAVOR INGRESE UNA OPCIÓN VÁLIDA ⚠️")
            self.menu_principal()
            