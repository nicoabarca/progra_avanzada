import menu_principal as mp
from manejo_csv import publicaciones_realizadas_usuario, crear_publicacion, eliminar_publicacion

class MenuPublicacionesRealizadas:

    def __init__(self, usuario):
        self.nombre_usuario = usuario

        self.menu_publicaciones_realizadas()

    #MENU DE PUBLICACIONES REALIZADAS   
    def menu_publicaciones_realizadas(self): 
        print(f"""
🟪 Menú de Publicaciones Realizadas 🟪

Usuario: {self.nombre_usuario}

Mis publicaciones: """)

        #OPCIONES PARA USUARIO SIN PUBLICACIONES
        if len(publicaciones_realizadas_usuario(self.nombre_usuario)) == 0:  

            print("No tienes publicaciones realizadas")
            print("\n[1] Crear una nueva publicación \n[2] Volver")

            input_usuario = input("\n🟢 Indique su opción: ")

            if input_usuario == str(1): #AGREGAR FUNCION QUE CREA UNA PUBLICACION
                nombre_pub = str(input("\n🟢 Ingrese el título de su publicación: "))
                descripcion_pub = str(input("\n🟢 Descripción de lo que quiere vender: "))
                precio_pub = str(input("\n🟢 Ingrese un precio de venta: "))

                crear_publicacion(nombre_pub, self.nombre_usuario, precio_pub, descripcion_pub)

                self.menu_publicaciones_realizadas()

            elif input_usuario == str(2): #VOLVER
                mp.MenuPrincipal(self.nombre_usuario)

            else: #INPUT INVALIDO
                print("\n⚠️ POR FAVOR INGRESE UNA OPCIÓN VÁLIDA ⚠️")
                self.menu_publicaciones_realizadas()

        #OPCIONES PARA USUARIO CON PUBLICACION/ES
        else:
            for publicacion in publicaciones_realizadas_usuario(self.nombre_usuario):
                print(f"- {publicacion.nombre_publicacion}")

            print("\n[1] Crear una nueva publicación \n[2] Eliminar publicación \n[3] Volver")

            input_usuario = input("\n🟢 Indique su opción: ")

            if input_usuario == str(1): # CREAR UNA PUBLICACION
                nombre_pub = str(input("\n🟢 Ingrese el título de su publicación: "))
                descripcion_pub = str(input("\n🟢 Descripción de lo que quiere vender: "))
                precio_pub = str(input("\n🟢 Ingrese un precio de venta: "))

                crear_publicacion(nombre_pub, self.nombre_usuario, precio_pub, descripcion_pub)

                self.menu_publicaciones_realizadas()

            elif input_usuario == str(2): #MENU PUBLICACIONES A ELIMINAR
                self.menu_publicaciones_eliminar()
                
            elif input_usuario == str(3): #VOLVER
                mp.MenuPrincipal(self.nombre_usuario)
            
            else: #INPUT INVÁLIDO
                print("\n⚠️ POR FAVOR INGRESE UNA OPCIÓN VÁLIDA ⚠️")
                self.menu_publicaciones_realizadas()
    
    #MENU DE PUBLICACIONES REALIZADAS A ELIMINAR
    def menu_publicaciones_eliminar(self):
    
        print("\n¿Cuál publicación deseas eliminar?\n")

        contador = 1
        for publicacion in publicaciones_realizadas_usuario(self.nombre_usuario):
            print(f"[{contador}] {publicacion.nombre_publicacion} -- {publicacion.fecha_creacion}")
            contador += 1
        
        print(f"[{contador}] Volver")

        input_usuario = input("\n🟢 Indique su opción: ")

        #INPUT ES DÍGITO
        if input_usuario.isdigit():

            if 1 <= int(input_usuario) <= contador - 1: #ELIMINAR PUBLICACION ELEGIDA
                eliminar_publicacion(input_usuario, self.nombre_usuario)
                self.menu_publicaciones_realizadas()

            elif int(input_usuario) == contador: #VOLVER
                self.menu_publicaciones_realizadas()

            else: #USUARIO ENTREGA UN INPUT INVÁLIDO
                print("\n⚠️POR FAVOR INGRESE UNA OPCIÓN VÁLIDA ⚠️")
                self.menu_publicaciones_eliminar()