from mascota import Perro, Gato, Conejo


def cargar_mascotas(archivo_mascotas):
    # COMPLETAR
    with open(archivo_mascotas, "r", encoding = "utf-8") as mascotas:
        lista_mascotas_archivo = []
        for mascota in mascotas:
            datos_mascota = mascota.strip().split(",", 5)
            lista_mascotas_archivo.append(datos_mascota)
    del lista_mascotas_archivo[0]

    lista_mascotas = []
    
    for mascota in lista_mascotas_archivo:
        info_mascota = [
                        mascota[0], 
                        mascota[2],
                        mascota[3],
                        int(mascota[4]),
                        int(mascota[5])
                        ]
        if mascota[1] == "gato":
            lista_mascotas.append(Gato( *info_mascota))

        elif mascota[1] == "conejo":
            lista_mascotas.append(Conejo( *info_mascota))

        elif mascota[1] == "perro":
            lista_mascotas.append(Perro( *info_mascota))

    return lista_mascotas

