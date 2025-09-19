# TP Integrador - Algoritmia y Estructura de Datos I -  Equipo 2  - Hito 1

## Sobre el juego
El objetivo de Wordle es adivinar la palabra oculta en la menor cantidad posible de intentos con el fin de obtener la mayor cantidad posible de puntos.

## Sobre el programa y su desarrollo
El juego inicia en el menu principal, mostrando diferentes opciones que llevan a distintos modulos dentro del mismo:

  1. El juego propiamente dicho
  2. Instrucciones
  3. Estadisticas
  4. Finalizacion del programa

A lo largo de las ultimas semanas nos reunimos en Discord en varias oportunidades para idear los requerimientos del juego.

En los estadios iniciales el foco principal fue el desarrollo del algoritmo del juego, la comparacion de la entrada (variable asignada a la palabra ingresada por el jugador) y la palabra seleccionada al azar por el programa, la generacion de los bloques de color y su impresion a lo largo de cada intento.

Posteriormente, y en linea con los requisitos de complejidad del programa se agregaron funcionalidades, como el registro/inicio de sesion del jugador, calculo de puntos segun intentos y almacenamiento de estos datos en el diccionario jugadores_registrados.

Siguiendo la idea anterior, en estadios posteriores decidimos explorar la posibilidad de utilizar palabras mas largasm y consecuentemente, ajustar la cantidad de intentos disponibles segun la misma. Esto tambien incorporo el calculo del promedio (puntos/juegos) para poder, no solamente mostrar el registro de jugadores, sino tambien confeccionar un ranking de high scores.
Para finalizar, incluimos los modulos de instrucciones, documentacion.

A lo largo de todo este primer hito, en cada iteracion las funciones fueron cambiando o aumentando en numero siguiendo las incorporaciones periodicas de nuevas funcionalidades.
Todavia hay puntos a mejorar y optimizar, que seran progresivamente ajustados a medida que el desarrollo continue.

### NOTA
Existe tambien un modulo oculto, el de documentacion, al cual se accede escribiendo "documentacion" en este menu principal. El mismo lista todas las funciones del programa y permite seleccionar cada una de ellas para visualizar el docsign de la misma.

## Sobre el repositorio
El repositorio consta de 2 archivos:
  wordle_demo.py
  wordle_entrega.py

### wordle_demo.py
contiene datos ficticios de jugadores y un banco de palabras con palabras limitadas, a fin de poder probar todas las funcionalidades del juego sin tener que adivinar la palabra.

### wordle_entrega.py
es el juego con un banco de preguntas adecuado y con el registro de jugadores vacio.

## Uso de IA
Con el fin de enfocarnos unicamente en el desarrollo de la logica, utilizamos IA principalmente en la generacion de las palabras del diccionario banco_palabras, los datos de los jugadores ficticios y correcciones de ortografia sobre las strings que se imprimen en consola. Tambien se utilizo para facilitar la redaccion de los docstrings, a fin de que los mismos quedaran estandarizados siguiendo el mismo estilo. De la misma manera, las instrucciones del juego fueron bocetadas por AI.


