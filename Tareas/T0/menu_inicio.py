from manejo_csv import datos_usuarios_registrados,agregar_usuario_nuevo
from parametros import MAX_CARACTERES, MIN_CARACTERES
import menu_principal as mp
import menu_publicaciones as mpub

class MenuInicio:

    def menu_inicio(self):
        print(f"""
🟪 Menu Inicio 🟪

Selecciona una opción:

[1] Ingresar sesión
[2] Registrar usuario
[3] Ingresar como usuario anónimo
[4] Salir
""" )

        input_usuario = input("🟢 Indique su opción: ")

        #INGRESAR SESIÓN
        if input_usuario == str(1):

            nombre_usuario = str(input("\n🟢 Ingrese su nombre de usuario: "))

            if nombre_usuario not in datos_usuarios_registrados():
                print("\n❌ USUARIO NO REGISTRADO ❌ | RETORNANDO -> Menú de Inicio.")
                self.menu_inicio()

            else:
                mp.MenuPrincipal(nombre_usuario)

        #REGISTRAR USUARIO
        elif input_usuario == str(2):

            nombre_usuario = str(input("\n🟢 Ingrese el nombre de usuario que desea registrar: "))

            condicion_1 = (MIN_CARACTERES <= len(nombre_usuario) <= MAX_CARACTERES) 
            condicion_2 = "," not in nombre_usuario 
            condicion_3 = nombre_usuario not in datos_usuarios_registrados()

            if condicion_1 and condicion_2 and condicion_3:
                print("\n✔️ NOMBRE DE USUARIO VÁLIDO ✔️ | INGRESANDO -> Menú Principal")  
                agregar_usuario_nuevo(nombre_usuario)
                mp.MenuPrincipal(nombre_usuario) 

            elif not condicion_1:
                print(f"\n❗ EL NOMBRE DE USUARIO DEBE TENER ENTRE {MIN_CARACTERES} Y {MAX_CARACTERES} CARACTERES ❗")
                self.menu_inicio()

            elif not condicion_2:
                print("\n❗ EL NOMBRE DE USUARIO NO PUEDE CONTENER COMAS \",\" ❗")
                self.menu_inicio()

            elif not condicion_3:
                print(f"\n❗ YA EXISTE EL NOMBRE DE USUARIO: {nombre_usuario}, DEBES ELEGIR OTRO ❗")
                self.menu_inicio()
        
        #INGRESAR COMO USUARIO ANÓNIMO
        elif input_usuario == str(3):
            mpub.MenuPublicaciones(None)
            
        #SALIR DE DCCOMERCE 
        elif input_usuario == str(4) :
            print("\n👋 Usted ha salido de DCComerce. Vuelva pronto 👋")
        
        #INPUT INVÁLIDO
        else:
            print("\n⚠️ POR FAVOR INGRESE UNA OPCIÓN VÁLIDA ⚠️")
            self.menu_inicio()