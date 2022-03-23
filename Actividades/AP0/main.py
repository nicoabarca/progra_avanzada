#Módulo para leer archivos csv
import csv
# Debes completar esta función para que retorne la información de los ayudantes
def cargar_datos(path):
    with open(path) as archivo_csv:
        csv_datos = csv.reader(archivo_csv, delimiter=',')
        lista_de_ayudantes = []
        for fila in csv_datos:
            lista_de_ayudantes.append(fila)
    return lista_de_ayudantes

# Completa esta función para encontrar la información del ayudante entregado
def buscar_info_ayudante(nombre_ayudante, lista_ayudantes):
    for ayudante in lista_ayudantes:
        if ayudante[0].lower() == nombre_ayudante.lower():
            return ayudante


# Completa esta función para que los ayudantes puedan saludar
def saludar_ayudante(info_ayudante):
     return f"Hola, mi nombre es {info_ayudante[0]} y soy ayudante {info_ayudante[1]} de IIC2233. Mi usuario en GitHub es {info_ayudante[2]} y me pueden econtrar en Discord como {info_ayudante[3]}"
    
if __name__ == '__main__':

    lista_ayudantes = cargar_datos("ayudantes.csv")

    ayudante_seleccionado = buscar_info_ayudante("Tamara Han", lista_ayudantes)

    print(saludar_ayudante(ayudante_seleccionado))
