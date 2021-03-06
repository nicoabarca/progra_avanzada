import menu_principal as mp
from manejo_csv import publicaciones_realizadas_usuario, crear_publicacion, eliminar_publicacion

class MenuPublicacionesRealizadas:

    def __init__(self, usuario):
        self.nombre_usuario = usuario

        self.menu_publicaciones_realizadas()

    #MENU DE PUBLICACIONES REALIZADAS   
    def menu_publicaciones_realizadas(self): 
        print(f"""
馃煪 Men煤 de Publicaciones Realizadas 馃煪

Usuario: {self.nombre_usuario}

Mis publicaciones: """)

        #OPCIONES PARA USUARIO SIN PUBLICACIONES
        if len(publicaciones_realizadas_usuario(self.nombre_usuario)) == 0:  

            print("No tienes publicaciones realizadas")
            print("\n[1] Crear una nueva publicaci贸n \n[2] Volver")

            input_usuario = input("\n馃煝 Indique su opci贸n: ")

            if input_usuario == str(1): #AGREGAR FUNCION QUE CREA UNA PUBLICACION
                nombre_pub = str(input("\n馃煝 Ingrese el t铆tulo de su publicaci贸n: "))
                descripcion_pub = str(input("\n馃煝 Descripci贸n de lo que quiere vender: "))
                precio_pub = str(input("\n馃煝 Ingrese un precio de venta: "))

                crear_publicacion(nombre_pub, self.nombre_usuario, precio_pub, descripcion_pub)

                self.menu_publicaciones_realizadas()

            elif input_usuario == str(2): #VOLVER
                mp.MenuPrincipal(self.nombre_usuario)

            else: #INPUT INVALIDO
                print("\n鈿狅笍 POR FAVOR INGRESE UNA OPCI脫N V脕LIDA 鈿狅笍")
                self.menu_publicaciones_realizadas()

        #OPCIONES PARA USUARIO CON PUBLICACION/ES
        else:
            for publicacion in publicaciones_realizadas_usuario(self.nombre_usuario):
                print(f"- {publicacion.nombre_publicacion}")

            print("\n[1] Crear una nueva publicaci贸n \n[2] Eliminar publicaci贸n \n[3] Volver")

            input_usuario = input("\n馃煝 Indique su opci贸n: ")

            if input_usuario == str(1): # CREAR UNA PUBLICACION
                nombre_pub = str(input("\n馃煝 Ingrese el t铆tulo de su publicaci贸n: "))
                descripcion_pub = str(input("\n馃煝 Descripci贸n de lo que quiere vender: "))
                precio_pub = str(input("\n馃煝 Ingrese un precio de venta: "))

                crear_publicacion(nombre_pub, self.nombre_usuario, precio_pub, descripcion_pub)

                self.menu_publicaciones_realizadas()

            elif input_usuario == str(2): #MENU PUBLICACIONES A ELIMINAR
                self.menu_publicaciones_eliminar()
                
            elif input_usuario == str(3): #VOLVER
                mp.MenuPrincipal(self.nombre_usuario)
            
            else: #INPUT INV脕LIDO
                print("\n鈿狅笍 POR FAVOR INGRESE UNA OPCI脫N V脕LIDA 鈿狅笍")
                self.menu_publicaciones_realizadas()
    
    #MENU DE PUBLICACIONES REALIZADAS A ELIMINAR
    def menu_publicaciones_eliminar(self):
    
        print("\n驴Cu谩l publicaci贸n deseas eliminar?\n")

        contador = 1
        for publicacion in publicaciones_realizadas_usuario(self.nombre_usuario):
            print(f"[{contador}] {publicacion.nombre_publicacion} -- {publicacion.fecha_creacion}")
            contador += 1
        
        print(f"[{contador}] Volver")

        input_usuario = input("\n馃煝 Indique su opci贸n: ")

        #INPUT ES D脥GITO
        if input_usuario.isdigit():

            if 1 <= int(input_usuario) <= contador - 1: #ELIMINAR PUBLICACION ELEGIDA
                eliminar_publicacion(input_usuario, self.nombre_usuario)
                self.menu_publicaciones_realizadas()

            elif int(input_usuario) == contador: #VOLVER
                self.menu_publicaciones_realizadas()

            else: #USUARIO ENTREGA UN INPUT INV脕LIDO
                print("\n鈿狅笍POR FAVOR INGRESE UNA OPCI脫N V脕LIDA 鈿狅笍")
                self.menu_publicaciones_eliminar()