import os
import sys
import opciones_menu_principal as omp
from cargar_data import cargar_tributos, cargar_arenas, cargar_objetos, cargar_ambientes

def menu_inicio():
    """"
    Imprime en pantalla el menu de inicio de DCCapitolio
    """
    while True:
        print("*** Menú de Inicio ***")
        print("----------------------")
        print("[1] Iniciar partida")
        print("[2] Salir \n")

        opcion = input("Indique su opción: ")

        if opcion == "1":
            menu_tributos()

        elif opcion == "2":
            print("\nSaliendo de DCCapitolio.")
            sys.exit()

        else:
            print("\nLa opción ingresada no es válida.\n")

def menu_tributos():
    """"
    Imprime en pantalla el menu de tributos de DCCapitolio 
    y se elige el tributo jugador (Tributo).
    """
    lista_tributos = cargar_tributos(os.path.join("data", "tributos.csv"))
    str_tributos = ""

    for indice in range(len(lista_tributos)):
        nombre = lista_tributos[indice].nombre
        distrito = lista_tributos[indice].distrito
        str_tributos += f"[{indice + 1}] {nombre} | Distrito: {distrito}\n"

    while True:
        print("\n*** Menú de Tributos ***")
        print("------------------------")
        print(str_tributos)
        print(f"[{len(lista_tributos) + 1}] Volver")
        print(f"[{len(lista_tributos) + 2}] Salir")

        opcion = input("\nIndique su opcion: ")

        try:
            if 1 <= int(opcion) <= len(lista_tributos):
                tributo_elegido = lista_tributos[int(opcion) - 1]
                tributos_enemigos = lista_tributos
                tributos_enemigos.remove(tributo_elegido)
                print(f"\nHa elegido a {tributo_elegido.nombre} como tributo.\n")
                menu_arenas(tributo_elegido, tributos_enemigos)

            elif int(opcion) == len(lista_tributos) + 1:
                print("")
                menu_inicio()

            elif int(opcion) == len(lista_tributos) + 2:
                print("\nSaliendo de DCCapitolio.")
                sys.exit()

            else:
                raise ValueError
        except ValueError:
            print("\nLa opción ingresada no es válida\n")

def menu_arenas(tributo_elegido, tributos_enemigos):
    """"
    Imprime en pantalla el menu de arenas de DCCapitolio 
    y se elige la arena en la cual se va a jugar.
    """
    lista_arenas = cargar_arenas(os.path.join("data", "arenas.csv"))
    str_arenas = ""

    for indice in range(len(lista_arenas)):
        nombre = lista_arenas[indice].nombre
        dificultad = lista_arenas[indice].dificultad
        riesgo = lista_arenas[indice].riesgo
        str_arenas += f"[{indice + 1}] {nombre} | Dificultad: {dificultad} | Riesgo: {riesgo}\n"

    while True:
        print(f"Jugando con: {tributo_elegido.nombre}\n")
        print("Seleccione el mapa en el cual desea jugar:")
        print("-" * 50)
        print(str_arenas)
        print(f"[{len(lista_arenas) + 1}] Volver")
        print(f"[{len(lista_arenas) + 2}] Salir")
    
        opcion = input("\nIndique su opcion: ")

        try:
            if 1 <= int(opcion) <= len(lista_arenas):
                arena_elegida = lista_arenas[int(opcion) - 1]
                arena_elegida.jugador = tributo_elegido
                arena_elegida.tributos = tributos_enemigos
                arena_elegida.ambientes = cargar_ambientes(os.path.join("data", "ambientes.csv"))
                arena_elegida.objetos = cargar_objetos(os.path.join("data", "objetos.csv"))
                arena_elegida.ambiente_actual = arena_elegida.ambientes[0]
                print(f"\nPara jugar ha elegido la arena: {arena_elegida.nombre}\n")
                menu_principal(tributo_elegido, tributos_enemigos, arena_elegida)

            elif int(opcion) == len(lista_arenas) + 1:
                print("")
                menu_tributos()

            elif int(opcion) == len(lista_arenas) + 2:
                print("\nSaliendo de DCCapitolio.")
                sys.exit()

            else:
                raise ValueError

        except ValueError:
            print("\nLa opción ingresada no es válida\n") 


def menu_principal(tributo_elegido, tributos_enemigos, arena_elegida):
    """"
    Imprime en pantalla el menu pricipal de DCCapitolio 
    el cual muestra las opciones por las cuales puede optar el
    tributo jugador.
    """
    while True:
        print("*** Menú Principal ***")
        print("----------------------")
        print(f"Jugando con: {tributo_elegido.nombre}\n")
        print(f"Mapa: {arena_elegida.nombre} | Ambiente: {arena_elegida.ambiente_actual.nombre}\n")
        print("[1] Simulación hora")
        print("[2] Mostrar estado del tributo")
        print("[3] Utilizar objeto")
        print("[4] Resumen DCCapitolio")
        print("[5] Volver")
        print("[6] Salir \n")

        opcion = input("Indique su opción: ")
        try:
            if opcion == "1":
                omp.menu_simulacion_hora(tributo_elegido, tributos_enemigos, arena_elegida)

            elif opcion == "2":
                omp.estado_tributo(tributo_elegido)

            elif opcion == "3":
                omp.mochila_objetos(tributo_elegido, tributos_enemigos, arena_elegida)

            elif opcion == "4":
                omp.resumen_dccapitolio(tributo_elegido, tributos_enemigos, arena_elegida)

            elif opcion == "5":
                print("\nVolviendo al Menú de Inicio\n")
                menu_inicio()

            elif opcion == "6":
                print("\nSaliendo de DCCapitolio.")
                sys.exit()
            
            else:
                raise ValueError

        except ValueError:
            print("\nLa opción ingresada no es válida\n")