# Tarea 2: DCCrossy Frog  🐸️ 🛣️ 🏞️

## Consideraciones generales :octocat:

Mi tarea no tiene implementado todo lo que se pedia por enunciado. Me falto implementar más que nada las animaciones del personaje, la pseudo aleatoridad del movimiento de los autos y troncos y las colisiones con el río. 
No obstante estan creadas todas las vistas que se pedían por enunciado y sus logicas correspondientes.  El código en general tiene hartos comentarios y también decidi dejar ciertos prints de consola, en caso de que estos sirvan para facilitar la correción, en caso de no ser así se pueden comentar y no pasaría nada. Se explica más en detalle lo que implemente y no implemente en el apartado a continuación.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Ventana de Inicio: Hecha completa. El único detalle es que la regex que ocupe para verificar que el nombre sea alfanumerico toma como incorrecto un nombre con la letra ñ. Pero todo lo demás funciona bien.
* Ventana de Ranking: Hecha completa.
* Ventana de Juego: Hecha completa.
* Ventana de Post-Nivel: Hecha completa. Puede ser que para puntajes muy grandes (más de 100.000), el text del QLabel puede ser muy chico para mostrar todo el número.
* Mecánicas de Juego:
    * Personaje: 
    1. Me falto hacer las animaciones de la rana al caminar. Solo se muestra el sprite ```still.png``` de la rana.
    2. El personaje puede saltar solo hacia adelante, y tampoco esta animado, es como si se moviera instantáneamente a otra posición.
    3. Si se choca con autos o bordes la rana se muere y vuelve a la posicion inicial, no logre implementar que muriera al tocar el rio.
    4. Si se chequea si la rana ha intersectado con un objeto especial, aunque este comportamiento esta un poco "buggeado".
    5. Si se chequea las colisiones con autos, la rana muere si choca con uno.
    6. Al estar la rana encima de un tronco, esta se mueve con él. Pero no muere si toca el río.
    * Mapa y Áreas de Juego:
    1. El mapa posee las tres zonas de juego.
    2. Se tienen 3 hileras de tronco y 3 hileras de autos por área.
    3. La velocidad de los autos aumenta al avanzar de nivel.
    4. Los autos de una hilera siempre van en una direccion.
    5. Los troncos de una hilera van en una direccion, pero su movimiento no es intercalado.
    * Objetos:
    Cabe destacar que el comportamiento de los objetos esta "buggeado", pero si generan cambios.
    1. El objeto corazon da una vida extra.
    2. El objeto moneda aumenta la cantidad de monedas del jugador.
    3. El objeto calavera aumenta.
    4. El objeto reloj, en base a mi testeo del juego, al parecer no aumenta el tiempo.
    5. Los objetos no aparecen en el rio ni meta.
    6. Los objetos si aparecen cada TIEMPO_OBJETOS segundos.
    * Fin de Nivel:
    1. Se calculan bien los puntajes.
    2. El nivel se acaba si la rana muere o se queda sin tiempo.
    3. Al llegar a la meta se abre la venta de post-nivel.
    * Fin del Juego:
    1. En caso de derrota o que el usuario haya avanzado de nivel, pero no quiera seguir jugando. Se guarda el puntaje en ```puntajes.txt```
    2. Si el usuario pierde, se notifica que no puede seguir jugando.
    3. Si el usuario gana, se notifica que puede seguir jugando
* Cheatcodes: Solo esta implementado que el juego se pause al apretar la tecla ```p```
* General: Distingui el juego entre backend y frontend. En gran parte el programa tiene un bajo acoplamiento y alta cohesion. Logre trabajar con los archivos entregados (no todos). Cree un archivo ```parametros.py``` con los parametros que se pedian por enunciado.
* Bonus: No implementado.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 
Además cabe destacar que si no existe un archivo ```puntajes.txt``` en la carpeta del backend. Al ejecutar ```main.py``` este archivo se creara automaticamente.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: ```QtCore```, ```QtWidgets```, ```QtGui``` (debe instalarse)
2. ```pathlib```: ```Path()``` 
3. ```re```: ```match()```
4. ```os```: ```path.join()```
5. ```random```: ```randint```, ```choice```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```backend/logica_inicio```: Contiene a ```LogicaInicio(QObject)```
2. ```backend/logica_juego```: Contiene a ```Logicajuego(QObject)```, ```Rana(QObject)```, ```Auto(QObject)```, ```Tronco(QObject)```, ```Objeto(QObject)```.
3. ```backend/logica_postnivel```: Contiene a ```LogicaPostNivel(QObject)```
4. ```backend/logica_ranking```: Contiene a ```LogicaRanking(QObject)```
5.```frontend/ventana_inicio```: Contiene a ```VentanaInicio(QWidget)```
6.```frontend/ventana_juego```: Contiene a ```VentanaJuego(QWidget)```
7.```frontend/ventana_postnivel```: Contiene a ```VentanaPostNivel(QWidget)```
8.```frontend/ventana_ranking```: Contiene a ```VentanaRanking(QWidget)```


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Para saltar se ocupa la tecla ```j```.
2. Para ocupar las teclas de movimiento ```w, a, s, d``` por favor verificar que no estan activadas las mayúsculas, porque en caso de que así sea, la rana no se va a mover.
3. Estan comentados todos los métodos y funciones del programa, para facilitar la correcion.
4. En el módulo ```main.py``` estan conectadas todas las señales del programa, y para facilitar su entendimiento, cada señal esta comentada con lo que hace y de donde viene.
5. También agregue comentario a la mayoria de Widgets que aparecen en las ventanas, para poder idenficarlos mejor.
6. Los parametros en ```parametros.py``` tambien tienen comentarios para saber en que módulo se ocuparon.


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://python-commandments.org/pyqt-center-window/ >: este hace que las ventanas esten aparezcan en la mitad de la pantalla, sin importar el tamaño de estas. Está implementado en todos los archivos ```.py``` del frontend.
2.  \<https://appdividend.com/2021/06/03/how-to-create-file-if-not-exists-in-python/ >: ocupe código de esta página para saber como crear un ```archivo.txt``` si este no existia. Esta implementado en ```backend/logica_ranking``` lineas 20-22.

