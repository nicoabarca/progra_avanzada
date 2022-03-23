# Tarea 1: DCCapitolio ⚔️ 🕊️ 🔥️

## Consideraciones generales :octocat:
* Implemente todo lo que se pedía por enunciado, a excepción del Bonus. 
* Las funciones y métodos de clases poseen comentarios, los cuales explican que hacen. Esto probablemente facilite la correción.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos: 38 pts (27%)
##### ✅ Diagrama 
##### ✅ Definición de clases, atributos y métodos 
##### ✅ Relaciones entre clases 
#### Simulaciones: 12 pts (8%)
##### ✅ Crear partida 
#### Acciones: 43 pts (30%)
##### ✅ Tributo 
##### ✅ Objeto 
##### ✅ Ambiente 
##### ✅ Arena 
#### Consola: 34 pts (24%)
##### ✅ Menú inicio 
##### ✅ Menú principal 
##### ✅ Simular Hora 
##### ✅ Robustez 
#### Manejo de archivos: 15 pts (11%)
##### ✅ Archivos CSV  
##### ✅ parametros.py 
#### Bonus: 3 décimas máximo
##### ❌ Guardar Partida 

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path.join()```
2. ```sys```: ```exit()```
3. ```random```: ```choice()```, ```uniform()```
4. ```abc```: ```ABC```, ```abstractmethod```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cargar_data.py```: Contiene las funciones necesarias para leer los archivos csv y asignar la data leída como los valores de algunos de los atributos de las clases ```Ambiente```, ```Arena```, ```Objeto``` y ```Tributos```.
2. ```ambiente.py```: Contiene la clase abstracta ```Ambiente(ABC)``` y sus subclases ```AmbientePlaya(Ambiente)```, ```AmbienteBosque(Ambiente)``` y ```AmbienteMontana(Ambiente)```. 
3. ```arena.py```: Contiene la clase ```Arena```
4. ```objeto.py```: Contiene la clase abstracta ```Objeto(ABC)``` y sus subclases ```ObjetoArma(Objeto)```, ```ObjetoConsumible(Objeto)``` y ```ObjetoEspecial(Objeto)```.
5. ```tributo.py```: Contiene la clase ```Tributo```
6. ```menu_capitolio.py```: Contiene las funciones necesarias que imprimen el menú de inicio, menú de tributos, menú de arenas y el menu principal. Además esta se encargan de manejar de manera correcta los inputs del usuario.
7. ```opciones_menu_principal.py```Contiene las funciones necesarias para trabajar con la lógica de las opciones disponibles en el menu principal.
8. ```parametros.py```: Posee valores que son constantes y que se ocupan en los módulos nombrados anteriormente.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:
1. Los objetos que se le pueden pedir a los patrocinadores se pueden acabar, esto quiere decir que no se puede sacar el mismo objeto 2 veces ya que este se elimina de la lista de objetos disponibles, además el tributo al utilizar un objeto, este se elimina de su mochila y "desaparece del programa".

PD: Al elegir una opción del menu de simulación de hora, lo más probable es que no se vea en la terminal el resultado de la opción elegida. Esto se debe a que si la acción es válida se imprimirá junto a la acción el resumen de lo que paso durante esa hora y este string del resumen ocupará gran parte de la ventana de la terminal, pero si alguien se mueve hacia arriba en la terminal se va a ver el resultado de la acción elegida por el usuario.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://github.com/IIC2233/Syllabus/blob/main/Actividades/AF1/main.py>: para hacer los menús de mi programa me base en la forma que se hicieron los menús de la Actividad Formativa 1.

