# Tarea 3: DCCalamar

## Consideraciones generales :octocat:
Solo alcance a implementar la ventana de inicio y de manera incompleta la comunicación entre el cliente y el servidor y el manejo (encriptación, decriptación y separación por bloques) de los mensajes que se enviaban. 
Todas las funciones tienen comentarios que explican lo que hacen. 

### Cosas implementadas y no implementadas :white_check_mark: :x:
#### Networking: 23 pts (18%)
##### ✅ Protocolo: la comunicación entre el socket del cliente y servidor es a través de TCP e IPv4
##### 🟠 Correcto uso de sockets: se instancia correctamente el socket del cliente y el servidor, y se crean threads para manejar la comunicación entre varios sockets, pero esta ultima funcionalidad no se probo del todo.
##### 🟠 Conexión: Al probar con 1-2 clientes, la conexión es constante, no alcance a probar si se caía con más. 
##### ❌ Manejo de clientes 
#### Arquitectura Cliente - Servidor: 31 pts (24%)
##### 🟠 Roles: se separa cliente y servidor, pero no se cumplen todas las responsabilidades que aparacen en el enunciado que deben cumplir cada uno.
##### ❌ Consistencia 
##### ❌ Logs 
#### Manejo de Bytes: 20 pts (15%)
##### ✅ Codificación: se utiliza little-big endian cuando se necesita y el mensaje se separa en bloques de 84 bytes
##### ✅ Decodificación: se decodifica el mensaje acorde a lo hecho en la codificación.
##### 🟠 Encriptación: se encripta bien el mensaje, pero al desencriptarlo puede fallar en algunos casos, no pude arreglar este bug, pero creo que se debe a ciertos caracteres que pueden afectar al hacer ```json.loads(mensaje)```
##### ✅ Integración: los mensajes se envia a través de un protocolo TCP
#### Interfaz gráfica: 31 pts (24%)
##### ✅ Modelación: para la ventana de inicio se hace distinción entre frontend y backend
##### 🟠 Ventana inicio: solo se visualiza la ventana con los elementos solicitados. 
##### ❌ Sala Principal 
##### ❌ Ventana de Invitación 
##### ❌ Sala de juego 
##### ❌ Ventana final 
#### Reglas de DCCalamar: 21 pts (16%)
##### ❌ Inicio del juego 
##### ❌ Ronda 
##### ❌ Termino del juego 
#### General: 4 pts (3%)
##### ✅ Parámetros (JSON) : en el cliente y servidor existe un archivo .json de donde se leen los parametros constantes del programa.
#### Bonus: 5 décimas máximo
##### ❌ Cheatcode 
##### ❌ Turnos con tiempo 

## Ejecución :computer:
Los módulos principalesde la tarea son ```cliente/main.py``` que inicializa los clientes y  ```servidor/main.py``` que inicializa el servidor.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: (debe instalarse)
2. ```socket```
3. ```threading```: ```Thread```, ```start()```
4. ```json```: ```dumps()```, ```loads()```
5. ```re```: ```match()```
6. ```dateutil.parser```: ```parse()```
7. ```os```: ```path.join()```
### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

*Módulos del ```cliente```*
1. ```backend/player.py```: Contiene a ```Player``` que es la clase que actua como cliente y la cual se conecta con el servidor
2. ```backend/start_window_logic.py```: Contiene a ```StartWindowLogic(QObject)```, clase que maneja la lógica de la ventana de inicio.
3. ```frontend/start_window.py```: Contiene a ```StartWindow(QWidget)```, clase que contiene los elementos de la ventana de inicio.
4. ```parametros.json```: Contiene los parametros del cliente.
5.  ```utils.py``` : Contiene la función ```get_json_data()```, la cual lee la data del json.

*Módulos del ```servidor```*
1. ```game_logic.py```: Contiene a ```GameLogic```, clase que se encarga de la lógica del juego y verificación de usuarios.
2. ```server.py```: Contiene a ```Server```, clase que actua como servidor y se encarga de enviar mensajes a los clientes y aceptar conexiones. 
3. ```parametros.json```: Contiene los parametros del servidor.
4.  ```utils.py``` : Contiene la función ```get_json_data()```, la cual lee la data del json.

## Supuestos y consideraciones adicionales :thinking:
PD: Perdón por lo poco que hice :(

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://python-commandments.org/pyqt-center-window:  hace que las ventanas aparezcan en la mitad de la pantalla, sin importar el tamaño de estas. Está implementado en ```cliente/frontend/start_window.py```, línea 73-78.
2. https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format : ocupe código de esta página para verificar con ```dateutil.parser.parse()``` si un string es una fecha válida. Esta implementado en ```servidor/game_logic.py```, en la función ```verify_user()```
