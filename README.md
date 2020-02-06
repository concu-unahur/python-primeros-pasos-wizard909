# Python primeros pasos

En `saludos.py`, `contador.py` y `dormilones.py` vas a encontrar lo que mostramos la clase pasada, como para que tengas una base.
En `saludos.py` hay cosas básicas de importar bibliotecas, y de funciones y clases.
En `contador.py` está cómo crear threads, y cómo lanzarlos (`start()`) y esperar a que terminen (`join()`).  Ahí estuvimos jugando un poco, y observamos el tema del indeterminismo cuando imprimíamos el valor del contador.
En `dormilones.py` vimos tres ejemplos básicos de ejecución (clásico secuencial, con threads, y con threads pero esperando que terminen) y cómo se ven afectados los tiempos de ejecución (más precisamente el valor del contador).

# Python segundos pasos

Ahora, para que no te aburras tanto, te toca meter mano un poco a vos. En lo que sigue te proponemos algunos ejercicios como para ir entrando en onda.
La idea esencial es más entender la lógica de lo que está pasando (con los threads en especial) más que codear técnicamente perfecto y/o complejo.

## Funciones, clases y bibliotecas

En `clasesYfunciones.py` están definidos sendos threads por una función y desde una clase. Más que nada para practicar al menos una vez cómo importar algo que hiciste vos:
* Hacete un archivo `definiciones.py` que contenga a las definiciones de la función y de la clase.
* Importá la función y la clase en `clasesYfunciones.py` (desde `definiciones.py` obviamente).

**Ayudas**
* La sintaxis para importar es `from <archivo sin .py> import <clase o funcion>`.

## Muchos threads

¿Y qué pasa si quiero crear y lanzar muchos threads? Sí, eso mismo, un loop.

### Parte 1
En `muchosThreads.py`:
* Completá el código para lanzar 10 threads.
* Medí el tiempo que se tarda entre crearlos y lanzarlos usando `tiempo.py`.

Asegurate de entender por qué tarda lo que tarda, a pesar de que son muchos threads.

### Parte 2
Ahora bien, creaste y lanzaste muchos threads perooo... ¿podés controlarlos? Por ejemplo ¿podés esperarlos a que terminen con el `join()`? No, porque no tenés manera de llamarlos o accederlos. ¿Cómo solucionás esto? Lo podés codear abajo de lo que acabás de hacer.

En `muchosThreads.py`:
* Inicializá una lista vacía (antes del `for`).
* En el `for`, luego de lanzar cada thread, agregalo a la lista.
* Hacete otro loop para esperar a que terminen todos los threads de la lista.
* Volvé a medir el tiempo desde que los creás hasta que terminan

¿Por qué tarda lo que tarda? Hacete un dibujito de la *traza*, es decir la línea de tiempo de ejecución, como para entender lo que pasa.

### Extra
* Modificá la función `dormir()` para que reciba un parámetro `segs` (los segundos que duerme). 
* Modificá el lanzamiento de los threads para pasarle este parámetro al `target`.

## Threads con operaciones no conmutativas

### Parte 1
En `operNoConm.py`:
* definí dos funciones: `sumarUno` y `multiplicarPorDos`, que operen sobre la misma variable;
* dale un valor inicial a la variable;
* ejecutá cada función en un thread separado y anotá los resultados.

¿Cúales serían los potenciales problemas de esto? Podés ir metiendo algunos `sleep` o `logger.info` como para ver cómo va cambiando el valor de la variable. También podés hacer `sleep` antes de alguna de las operaciones y ver cómo afecta esto al resultado.

**Ayudas**
* Acordate de usar `global` para poder usar la variable global desde las funciones.
* A las operaciones matemáticas en las que el orden de los operandos no importa se las llama **conmutativas**. Por ejemplo: la suma y la multiplicación son conmutativas (_"el orden de los factores no altera el producto"_) pero la división y la resta no.

### Parte 2
Usando las funciones definidas antes, escribí programas que siempre realicen estas operaciones:
* `3 + 1 / 2`;
* `3 / 2 + 1`
* `(3 + 1 / 2) / 2` 
* `(3 / 2 + 1) / 2`

Obviamente, las funciones tienen que ejecutar en threads diferentes, vale crear todos los threads que sean necesarios. Quizás te convenga usar varios archivos para cada una de las cuentas, e importarte las funciones de `operNoConm.py`.

## Unas cosas más

### Cosa 1
En `dowload.py` hay un código que se baja secuencialmente imágenes de un sitio.
* Miralo, correlo, y fijate de entenderlo.
* Ahora hacete la versión threads.

¿Mejora en algo? ¿Por qué de todos modos es mejor hacerlo con threads?

### Cosa 2
* Mirá `llenarLista.py`, asegurate de entenderlo.
* *Sin correrlo* intentá imaginarte y escribí los potenciales problemas que puede tener ese código. También escribí ideas sobre cómo arreglarlos.

## Extras

### Jugadores y dados

Supongamos que cuatro jugadores tienen que arrojar un dado una sola vez, no importa en qué orden, pero solo uno a la vez puede arrojar el dado.

- Si implementás esto de forma clásica secuencial, ¿más o menos cómo sería?
- Ahora la versión con threads, ¿aprox. cómo harías?
    - ¿Qué problemas surgen? Pensá soluciones e ideas para resolverlos

### ¿Secuencial clásico, concurrente o paralelo?

Para cada una de las siguiente situaciones, decidí si es secuencial clásico, concurrente o paralelo. Intentá justificar señalando las ideas esenciales de cada caso.

- Cuál persona de un total de 50 corre más rápido una maratón.
    - opción 1) Cada persona corre secuencialmente en la pista, y medimos cada tiempo.
    - opción 2) Todas las personas corren en la misma pista, y la que llega primero listo.
		- Preguntas: ¿hay algún recurso compartido? ¿genera problemas?
    - opción 3) Cada persona corre en una pista distinta, todas al mismo tiempo.
		- Pregunta: ¿hay un aumento de recursos respecto al anterior?
    - Pregunta: ¿pros y contras de cada opción?

- Competencia de triples en basquet: quién mete más en 10 intentos.
    - opción 1) Cada persona secuencialmente realiza 10 intentos, y anotamos la cantidad de triples.
    - opción 2) Todas las personas tiran los 10 intentos al mismo tiempo.
		- Preguntas: ¿hay algún recurso compartido? ¿genera problemas?
    - opción 3) Cada persona tira en un aro distinto, todas al mismo tiempo.
    - Pregunta: ¿pros y contras de cada opción?
