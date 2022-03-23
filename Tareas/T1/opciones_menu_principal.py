import sys
import random
import menu_capitolio as mc

def menu_simulacion_hora(tributo, tributos_enemigos, arena_elegida):
    """"
    Imprime en pantalla el menu de simulación de hora de DCCapitolio 
    el cual muestra las opciones por las cuales puede optar el
    tributo jugador en una determinada hora.
    """
    accion_elegida = ""
    while True:
        print(f"\n¿Qué va a hacer {tributo.nombre} esta hora?")
        print("-" * 50 + "\n")
        print("[1] Acción heroica")
        print("[2] Atacar a un tributo")
        print("[3] Pedir objetos a patrocinadores")
        print("[4] Hacerse bolita")
        print("[5] Volver")
        print("[6] Salir")
        opcion = input("\nIndique su opcion: ")
        try:
            accion_elegida = "Acción heroica"
            if opcion == "1": 
                if tributo.accion_heroica():
                    resumen_simulacion_hora(accion_elegida, tributo, 
                    tributos_enemigos, arena_elegida)
                else:
                    print(f"\n{tributo.nombre} te falta energía para una acción heroica.")
                    print("\nElige otra opción.")

            elif opcion == "2": 
                accion_elegida = "Atacar tributo"
                tributos_vivos = list(filter(lambda tributo: tributo.esta_vivo, tributos_enemigos))
                str_tributos_vivos = ""

                for indice in range(len(tributos_vivos)):
                    str_tributos_vivos += f"[{indice + 1}] {tributos_vivos[indice].nombre}\n"

                while True:
                    print("\nTributos Enemigos con Vida")
                    print("--------------------------")
                    print(str_tributos_vivos)
                    print(f"[{len(tributos_vivos) + 1}] Volver")
                    print(f"[{len(tributos_vivos) + 2}] Salir")

                    opcion = input("\n¿Qué tributo desea atacar?: ")

                    try:
                        if 1 <= int(opcion) <= len(tributos_vivos):
                            tributo_a_atacar = tributos_vivos[int(opcion) - 1]
                            tributos_vivos.remove(tributo_a_atacar)
                            if tributo.atacar(tributo_a_atacar):
                                tributos_vivos.insert(int(opcion) - 1, tributo_a_atacar)
                                resumen_simulacion_hora(accion_elegida, tributo, 
                                tributos_enemigos, arena_elegida)

                            else:
                                print(f"\n{tributo.nombre} te falta energía para atacar.")
                                print("\nElige otra opción.")
                                mc.menu_principal(tributo, tributos_enemigos, arena_elegida)

                        elif int(opcion) == len(tributos_vivos) + 1:
                            print("")
                            mc.menu_principal(tributo, tributos_enemigos, arena_elegida)

                        elif int(opcion) == len(tributos_vivos) + 2:
                            print("\nSaliendo de DCCapitolio.")
                            sys.exit() 
                        
                        else:
                            raise ValueError

                    except ValueError:
                        print("\nLa opción ingresada no es válida.")

            elif opcion == "3":
                accion_elegida = "Pedir objeto a patrocinadores"
                if arena_elegida.objetos:
                    objeto_al_azar = random.choice(arena_elegida.objetos)
                    if tributo.pedir_objeto(objeto_al_azar):
                        arena_elegida.objetos.remove(objeto_al_azar)
                        resumen_simulacion_hora(accion_elegida, tributo, 
                        tributos_enemigos, arena_elegida)
                    else:
                        print(f"\n{tributo.nombre} te falta popularidad para pedir un objeto.")
                        print("\nElige otra opción.")
                else:
                    print("\nLos patrocinadores ya no tienen más objetos.\n")
                    print("Elige otra opción.")

            elif opcion == "4":
                accion_elegida = "Hacerse bolita"
                tributo.hacerse_bolita()
                resumen_simulacion_hora(accion_elegida, tributo, 
                tributos_enemigos, arena_elegida)

            elif opcion == "5":
                print("")
                mc.menu_principal(tributo, tributos_enemigos, arena_elegida)

            elif opcion == "6":
                print("\nSaliendo de DCCapitolio.")
                sys.exit()

            else:
                raise ValueError

        except ValueError:
            print("\nLa opción ingresada no es válida")

def estado_tributo(tributo):
    """"
    Imprime en pantalla el estado actual del tributo jugador.
    """
    print("Estado Tributo".center(80))
    print("-" * 80)
    print(f"Nombre: {tributo.nombre}")
    print(f"Distrito: {tributo.distrito}")
    print(f"Edad: {str(tributo.edad)}")
    print(f"Energia: {str(tributo.energia)}")
    print(f"Agilidad: {str(tributo.agilidad)}")
    print(f"Fuerza: {str(tributo.fuerza)}")
    print(f"Ingenio: {str(tributo.ingenio)}")
    print(f"Popularidad: {str(tributo.popularidad)}")
    print(f"Objetos: {tributo.mochila} ")
    print(f"Peso: {str(tributo.peso)} \n")

def mochila_objetos(tributo, tributos_enemigos, arena_elegida):
    """"
    Imprime en pantalla los objetos que tiene el tributo jugador en la mochila,
    en caso de no tener se avisa y se devuelve al menu principal.
    """
    if tributo.mochila:
        while True:
            print(f"\nQué objeto desea ocupar {tributo.nombre}")
            print("------------------------------------------")
            for indice in range(len(tributo.mochila)):
                print(f"[{indice + 1}] {tributo.mochila[indice]}")
            print(f"\n[{len(tributo.mochila) + 1}] Volver")
            print(f"[{len(tributo.mochila) + 2}] Salir")

            opcion = input("\nIndique su opción: ")

            try:
                if 1 <= int(opcion) <= len(tributo.mochila):
                    objeto_elegido = tributo.mochila[int(opcion) - 1]
                    tributo.utilizar_objeto(objeto_elegido, arena_elegida)

                    mc.menu_principal(tributo, tributos_enemigos, arena_elegida)

                elif int(opcion) == len(tributo.mochila) + 1:
                    mc.menu_principal(tributo, tributos_enemigos, arena_elegida)

                elif int(opcion) == len(tributo.mochila) + 2:
                    print("\nSaliendo de DCCapitolio.")
                    sys.exit()

                else:
                    raise ValueError

            except ValueError:
                print("\nLa opción ingresada no es válida")
    else:
        print("\nNo tienes objetos en tu mochila. Volviendo al Menú Principal.\n")
        mc.menu_principal(tributo, tributos_enemigos, arena_elegida)

def resumen_dccapitolio(tributo, tributos_enemigos, arena_elegida):
    """"
    Imprime en pantalla el estado actual de DCCapitolio.
    """
    tributos_vivos = list(filter(lambda tributo: tributo.esta_vivo, tributos_enemigos))
    print("Estado DCCapitolio".center(80))
    print("-" * 80)
    print(f"Dificultad: {arena_elegida.dificultad}\n")
    print("Tributos vivos:")
    print(f"  {tributo.nombre} : {tributo.vida} (Jugador)")
    for tributo in tributos_vivos:
        print(f"  {tributo.nombre} : {tributo.vida}")

    print(f"\nPróximo ambiente: {arena_elegida.ambiente_proximo()}\n")

def resumen_simulacion_hora(opcion, tributo_jugador, tributos_enemigos, arena_elegida):
    """"
    Imprime en pantalla lo ocurrido durante una simulación de hora,
    ademas de verificar si se ha cumplido o no la condición de término de DCCapitolio, 
    esto es cuando muere el tributo jugador o es el único vivo.
    """
    print("Resumen Simulación de Hora".center(80))
    print("-" * 80 + "\n")

    #Opción elegida por el jugador
    print(f"Opción elegida: {opcion}\n")

    #Encuentros entre tributos durante la simulación de hora
    arena_elegida.encuentros(tributo_jugador, tributos_enemigos)

    #Evento al final de la simulación de hora
    print("\nEvento:")
    print("----------")
    arena_elegida.ejecutar_evento()

    #Tributos con vida
    tributos_vivos = list(filter(lambda tributo: tributo.esta_vivo, tributos_enemigos))
    print("\nTributos con vida:")
    print("--------------------")
    if tributo_jugador.vida:
        print(f" {tributo_jugador.nombre} ({tributo_jugador.vida}) (Jugador)")
    for tributo in tributos_vivos:
        print(f" {tributo.nombre} ({tributo.vida})")

    #Tributos muertos
    tributos_muertos = list(filter(lambda tributo: tributo.esta_vivo == False, tributos_enemigos))
    print("\nTributos muertos:")
    print("--------------------")
    if tributos_muertos:
        if not tributo.vida:
            print(f" {tributo_jugador.nombre} ({tributo_jugador.vida}) (Jugador)")
        for tributo in tributos_muertos:
            print(f" {tributo.nombre}")
        print("")
    else:
        print("\nNo hay tributos muertos aún\n")

    #Cambio de ambiente
    arena_elegida.cambio_ambiente_actual()

    print(f"Proximo ambiente: {arena_elegida.ambiente_actual.nombre}\n")
    print("-------------------------------")

    #Verificar si el jugador ganó o esta muerto
    if not tributo_jugador.esta_vivo:
        print(f"{tributo_jugador.nombre} has perdido. Volviendo al Menú de Inicio.\n")
        mc.menu_inicio()

    elif len(tributos_vivos) == 0:
        print(f"{tributo_jugador.nombre} has ganado DCCapitolio.")
        sys.exit()

    else:
        mc.menu_principal(tributo_jugador, tributos_enemigos, arena_elegida)
    


