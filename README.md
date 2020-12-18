## POO con Python  

--- 

### Objetivos : 
- Entender cómo funciona la programación orienda a objetos (POO)
- Entender cómo medir la eficiencia temporal y espacial de nuestros algoritmos. 
- Entender cómo y por qué graficar.
- Aprender a resolver problemas de búsqueda, ordenación y optimización.

### Tipos de datos Abstractos: 
- En python todo es un objeto y tiene un tipo.
    - Representación de datos y formas de interactuar con ellos.

- Formas de interactuar con un objeto:
    - Creación
    - Manipulación
    - Destrucción

- Ventajas: 
    - Decomposición
    - Abstracción
    - Encapsulación

### Instancias 
- Mientras que la clase es un molde, a los objetos creados se les conoce como instancias. 
- Cuando se crea una instancia, se ejecuta el método *__init__* 
- Todos los métodos de una clase reciben implícitamente como primer parámetro self
- Los atributos de clase nos permiten: 
    - Representar datos
    - Procedimientos para interactuar con los mismos (métodos)
    - Mecanismos para esconder la representación interna.

- Se accede a los atributos con la notación de punto.
- Puede tener atributos privados. Por convención comienzan con _

### Decomposición
- Partir un problema en problemas más pequeños
- Las clases permiten crear mayores abstracciones en forma de componentes
- Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener

### Abstracción 
- Enfocarnos en la información relevante.
- Separar la información central de los detalles secundarios.
- Podemos utilizar variables y métodos (privados o públicos)

### Encapsulación
- Permite agrupar datos y su comportamiento.
- Controla el acceso a dichos datos
- Previene modificaciones no autorizadas.

### Herencia 
- Permite modelar una jerarquía de clases.
- Permite compartir comportamiento común en la jerarquía.
- Al padre se le conoce como superclase y al hijo como subclase.

### Polimorfismo
- La habilidad de tomar varias formas
- En Python, nos permite cambiar el comportamiento de una superclase para adaptarlo a la subclase

### Introducción a la complejidad algorítmica
- ¿Por qué comparamos la eficiencia de un algoritmo?
- Complejidad temporal vs complejidad espacial
- Podemos definirla como T(n)

### Aproximaciones 
- Cronometrar el tiempo en el que corre un algoritmo
- Contar los pasos con una medida abstracta de operación
- Contar los pasos conforme nos aproximamos al infinito.

### Crecimiento asintótico
- No importan variaciones pequeñas.
- El enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito
- Mejor de los casos, promedio, peor de los casos
- Big O
- Nada más importa el término de mayor tamaño

### Clases de complejidad algorítmica
- O(1) Constante
- O(n) Lineal
- O(log n) Logarítmica
- O (n log n) log lineal
- O(n**2) Polinomial
- O (2**n) Exponencial

## Algoritmos de Búsqueda y Ordenación
---

### Búsqueda Lineal
- Busca en todos los elementos de manera secuencial
- ¿Cuál es el peor caso?

### Búsqueda binaria
- Divide y conquista
- El problema se divide en 2 en cada iteración
- ¿Cuál es el peor caso?

### Ordenamiento de Burbuja
El ordenamiento de burbuja es un algoritmo que recorre repetidamente una lista que necesita ordenarse. Compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este procedimiento se repite hasta que no se requieren más intercambios, lo que indica que la lista se encuentra ordenada. 

### Ordenamiento por inserción
El ordenamiento por inserción es uno de los algoritmos más comunes que estudian
los Científicos del Cómputo. Es intuitivo y fácil de implementar, pero es muy
ineficiente para listas de gran tamaño.

Una de las características del ordenamiento por inserción es que ordena en “su
lugar.” Es decir, no requiere memoria adicional para realizar el ordenamiento
ya que simplemente modifican los valores en memoria.

### Ordenamiento por mezcla

El ordenamiento por mezcla es un algoritmo de divide y conquista. Primero divide una lista en partes iguales hasta que quedan sublistas de 1 a 0 elementos. Luego las recombina en forma ordenada

## Ambientes virtuales 

- Permiten aislar el ambiente para poder instalar diversas versiones de paquetes. 
- A partir de pyhton 3 se incluye en la librería estándar en el módulo venv
- Nin´gun ingeniero profesional de Python trabaja sin ellos.

### Pip

- Permite descargar paquetes de terceros para utilizar en nuestro programa.
- Permite compartir nuestros paquetes con terceros. 
- Permite especificar la versión del paquete que necesitamos.

## ¿Por qué graficar?
- Reconocimiento de patrones
- Predicción de una serie
- Simplifica la interpretación y las conclusiones acerca de los datos.

### Graficado simple
- Bokeh permite construir gráficas complejas de manera rápida y con comandos simples.
- Permite exportar a varios formatos como html, notebooks, imágenes, etc.
- Bokeh se puede utilizar en el servidor con Flask y DJango

### Introducción a la optimización
- El concepto de optimización permite resolver mucho problemas de manera computacional.
- Una función objetivo que debemos maximizar o minimizar
- Una serie de limitantes que debemos respetar