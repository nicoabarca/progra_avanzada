from excepciones_covid import RiesgoCovid


# NO DEBES MODIFICAR ESTA FUNCIÓN
def verificar_sintomas(invitade):
    if invitade.temperatura > 37.5:
        raise RiesgoCovid("fiebre", invitade.nombre)
    elif invitade.tos:
        raise RiesgoCovid("tos", invitade.nombre)
    elif invitade.dolor_cabeza:
        raise RiesgoCovid("dolor_cabeza", invitade.nombre)


def entregar_invitados(diccionario_invitades):
    # Completar
    lista_invitado_sanos = []
    for nombre_invitade in diccionario_invitades:
        try:
            invitade = diccionario_invitades[nombre_invitade]
            verificar_sintomas(invitade)
        except RiesgoCovid as err :
            print(err)
            err.alerta_de_covid()
        else:
            lista_invitado_sanos.append(diccionario_invitades[nombre_invitade].nombre)
    return lista_invitado_sanos





