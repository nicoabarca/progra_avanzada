# Tarea 0: DCComerce 🛒

## Consideraciones generales :octocat:

* Antes de ejecutar el código, por favor verificar que los archivos csv no contenga líneas vacías entre filas o después de la última línea de datos, ya que si hay líneas vacías las funciones que trabajan con los archivos csv (que estan en el módulo ```manejo.csv```) van a producir un error, debido a que a una función le van a faltar argumentos.
* El registro de usuarios nuevos es **case sensitive**, por ende si existe un usuario llamado **Gatochico** y se registra un usuario nuevo con el nombre **gatochico** van a ser dos usuarios distintos.
* Implemente todo lo que se pedía por enunciado y probe el programa bastantes veces con variedad de inputs, por ende no debería haber "bugs" o fallos.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Menú de Inicio (14pts) (14%)
##### ✅ Requisitos
##### ✅ Iniciar sesión
##### ✅ Ingresar como usuario anónimo
##### ✅ Registrar usuario
##### ✅ Salir
#### Flujo del programa (35pts) (35%) 
##### ✅ Menú Principal
##### ✅ Menú Publicaciones
##### ✅ Menú Publicaciones Realizadas
#### Entidades 15pts (15%)
##### ✅ Usuarios
##### ✅ Publicaciones
##### ✅ Comentarios
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos
#### General: 21 pts (21%)
##### ✅ Menús
##### ✅ Parámetros
##### ✅ Módulos
##### ✅ PEP8

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```operator```: ```itemgetter()```
2. ```collections```: ```namedtuple()```
3. ```datetime```: ```datetime.strftime()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```manejo_csv.py```: Contiene todas las funciones necesarias para leer los archivos csv y modificarlos. En el archivo hay comentarios que especifican que hace cada función. Es utilizado en todos los modulos siguientes.
2. ```menu_inicio.py```: Contiene ```class MenuInicio``` la cual mediante el método ```menu_inicio()``` es responsable del funcionamiento del menú de inicio.
3. ```menu_principal.py```: Contiene ```class MenuPrincipal``` la cual mediante el método ```menu_principal()``` se encarga del funcionamiento del menu principal
4. ```menu_publicaciones.py```: Contiene ```class MenuPublicaciones``` la cual mediante el método ```menu_publicaciones()``` y ```menu_publicaciones_detallado()``` muestran el Menu de Publicaciones y el Menu de una publicación en específico con sus comentarios y detalles.
5. ```menu_publicaciones_realizadas.py``` : Contiene ```class MenuPublicacionesRealizadas``` y los métodos ```menu_publicaciones_realizadas()``` y  ```menu_publicaciones_eliminar()```, que muestran el Menú de Publicaciones Realizadas y el Menú en el cual el usuario puede eliminar una publicación que haya hecho, respectivamente.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. En el Menú de Publicaciones realizadas, en el caso de que el usuario no tenga publicaciones, la opción de eliminar una publicación no aparece, ya que no tiene sentido eliminar algo que no existe.
2. En cualquiera de los menús, si se ingresa una opción inválida, se avisa al usuario que el input no es válido y se refreshea el menú y se pide denuevo un input hasta que este sea válido.

PD: 
* Revisar que los archivos csv no tengan lineas vacias. 
* El código tiene muchos comentarios que explican la funcionalidad de ciertas partes del programa, lo cual puede ayudar a su correción.

## Referencias de código externo :book:
Para realizar mi tarea saqué código de:
1. \<https://docs.python.org/3.8/howto/sorting.html#operator-module-functionsg>: esta documentación del módulo ```operator``` la utilice para saber como ordenar las publicaciones y los comentarios mediante su fecha de creación y emisión, respectivamente. Esta funcionalidad está implementada en el archivo ```manejo_csv.py``` en las líneas 34 y 67.