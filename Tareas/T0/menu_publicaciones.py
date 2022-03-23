from manejo_csv import datos_publicaciones, datos_comentarios, agregar_comentario
import menu_principal as mp
import menu_inicio as mi

class MenuPublicaciones:

    def __init__(self, usuario):
        self.nombre_usuario = usuario
        self.input_usuario = ""

        self.menu_publicaciones()
    #MENÚ DE PUBLICACIONES
    def menu_publicaciones(self):

        #TIPO DE USUARIO
        tipo = f"Usuario: {self.nombre_usuario}" if self.nombre_usuario != None else "Modo anónimo"
        print("\n🟪 Menú de Publicaciones 🟪")
        print(f"\n{tipo}\n") 

        #PRINT DE TODAS LAS PUBLICACIONES QUE ESTAN EN EL ARCHIVO publicaciones.csv
        contador = 1
        for publicacion in datos_publicaciones():
            print(f"[{contador}] {publicacion.nombre_publicacion}")
            contador += 1

        print(f"[{contador}] Volver")

        input_usuario = input("\n🟢 Indique su opción: ")

        #USUARIO ENTREGA UN INPUT VALIDO PARA -->
        if input_usuario.isdigit():
            #-> VER UNA PUBLICACION EN ESPECIFICO
            if 1 <= int(input_usuario) <= contador - 1:
                self.input_usuario = int(input_usuario)
                self.menu_publicacion_detallado(self.input_usuario)
            #-> VOLVER
            else:
                if self.nombre_usuario != None:
                    mp.MenuPrincipal(self.nombre_usuario)
                else:
                    mi.MenuInicio().menu_inicio()

        #USUARIO ENTREGA UN INPUT INVÁLIDO
        else:
            print("\n⚠️ POR FAVOR INGRESE UNA OPCIÓN VÁLIDA ⚠️")
            self.menu_publicaciones()

    #MENU DE PUBLICACION CON DETALLES Y COMENTARIOS
    def menu_publicacion_detallado(self, input_usuario):
        #LAS VARIABLES DE ABAJO SON NECESARIAS PARA MOSTRAR CORRECTAMENTE LA
        #PUBLICACIÓN ELEGIDA
        input_usuario = int(self.input_usuario) - 1
        lista_de_publicaciones = datos_publicaciones()
        publicacion = lista_de_publicaciones[input_usuario]
        comentarios_publicacion = [comentario 
        for comentario in datos_comentarios() 
        if comentario.id_publicacion == publicacion.id_publicacion]

        print(f"""
🟪 {publicacion.nombre_publicacion} 🟪

Creado: {publicacion.fecha_creacion}
Vendedor: {publicacion.usuario}
Precio: ${publicacion.precio}
Descripción: {publicacion.descripcion}

Comentarios de la publicación:
""")
        #COMENTARIOS DE LA PUBLICACIÓN
        for comentario in comentarios_publicacion:
            print(f"{comentario.fecha_emision} -- {comentario.usuario}: {comentario.contenido}")

        #OPCIONES PARA USUARIO ANÓNIMO
        if self.nombre_usuario == None:
            print("\n[2] Volver")
            input_usuario_comentario = input("\n🟢 Indique su opción: ")
            if input_usuario_comentario == str(2):
                self.menu_publicaciones()
            else:
                print("\n⚠️ POR FAVOR INGRESE UNA OPCIÓN VÁLIDA ⚠️")
                self.menu_publicacion_detallado(self.input_usuario)

        #OPCIONES PARA USUARIO CON NOMBRE (REGISTRADO)
        else:
            print(f"\n[1] Agregar comentario\n[2] Volver")
            input_usuario_comentario = input("\n🟢 Indique su opción: ")

            if input_usuario_comentario == str(1):
                #LLAMAR A FUNCION PARA AGREGAR UN COMENTARIO A LA PUBLICACIÓN
                contenido = str(input("\n🟢 Escribe un comentario: "))
                agregar_comentario(publicacion.id_publicacion, self.nombre_usuario, contenido)
                self.menu_publicacion_detallado(self.input_usuario)

            elif input_usuario_comentario == str(2):
                self.menu_publicaciones()

            else:
                print("\n⚠️ POR FAVOR INGRESE UNA OPCIÓN VÁLIDA ⚠️")
                self.menu_publicacion_detallado(self.input_usuario)

        








