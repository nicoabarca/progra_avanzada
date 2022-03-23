def verificar_edad(invitade):
    # Completar
    if invitade.edad < 0:
        raise ValueError(f"Error: la edad de {invitade.nombre} es menor negativa")
    else:
        return True

def corregir_edad(invitade):
    # Completar
    try:
        verificar_edad(invitade)
    except ValueError:
        invitade.edad = abs(invitade.edad)
        print(f"El error en la edad de {invitade.nombre} ha sido corregido")

def verificar_pase_movilidad(invitade):
    # Completar
    if not isinstance(invitade.pase_movilidad, bool):
        raise TypeError(f"Error: el pase de movilidad de {invitade.nombre} no es un bool")
    else:
        return True

def corregir_pase_movilidad(invitade):
    # Completar
    try:
        verificar_pase_movilidad(invitade)
    except TypeError:
        invitade.pase_movilidad = True
        print(f"El error en el pase de movilidad de {invitade.nombre} ha sido corregido")

def verificar_mail(invitade):
    # Completar
    if invitade.mail.startswith("uc@"):
        raise ValueError(f"Error: El mail de {invitade.nombre} no esta en el formato correcto.")
    else:
        return True


def corregir_mail(invitade):
    # Completar
    try:
        verificar_mail(invitade)
    except ValueError:
        indice_cl = int(invitade.mail.find(".cl"))
        nombre_mail = invitade.mail[3 : indice_cl]
        invitade.mail = f"{nombre_mail}@uc.cl"

        print(f"El error en el mail de {invitade.nombre} ha sido corregido")



def dar_alerta_colado(nombre_asistente, diccionario_invitades):
    # Completar
    try:
        if nombre_asistente not in diccionario_invitades:
            raise KeyError(f"{nombre_asistente } no esta en la lista")

    except KeyError as err:
        print(err)
        print(f"ERROR: {nombre_asistente} se está intentando colar al carrete")

    else:
        asistente = diccionario_invitades[nombre_asistente]

        print(f"{asistente.nombre} esta en la lista y tiene edad {asistente.edad}")
    
