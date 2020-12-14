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

