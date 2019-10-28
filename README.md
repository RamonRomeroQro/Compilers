# Ruby - PLY (Python Lex-Yacc)

-----

    Copyright 2019 © Ramón Romero @RamonRomeroQro
    Compilers, ITESM.
    A01700318 for ITESM
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    V.27102019

    Special thanks to: 
    @Manchas2k4, @EduardoLarios and @dabeaz (PLY)
    

-----

## Indice
+ [Características](#Características-a-considerar)

+ [Primera Entrega](#Primera-Entrega)
    + [Resultados](#Resultados-1)

+ [Segunda Entrega](#Segunda-Entrega)
    + [Resultados](#Resultados-2)



-----


## Características a considerar

1. Comentarios: 

    ``` ruby

    # Comentario de una linea

    =begin
    Comentario 
    multilinea
    =end

    ```
2. Estructuras anidadas: 

    + Debe haber una manera de crear estructuras anidadas como estructuras condicionales, ciclos o jerarquías (if, while)

    + Parte de la gramatica, el resto en  ``` parser.py ```:

    ``` python
    # Anidacion de statements

    '''
   
    statements  : statement statements	
                | statement 
    '''


    ```


3. Variables y constantes: 

Ruby es un lenguaje de tipado dinamico, por lo que no requiere de palabras reservadas como ```int``` o ```float```, unicamente que comiencen con una letra y sean seguidas de letras, numeros o underscore:  ```[a-z_][a-zA-Z0-9_]*' ```

Las constantes son identificadas son identificadas por que comienzan con una letra mayuscula [A-Z], sin embargo, permanece mutable y su comportamiento es homólogo al de las variables: ``` r'[A-Z][a-zA-Z0-9_]*' ```


> The Ruby interpreter does not actually enforce the constancy of constants.

>https://www.oreilly.com/library/view/the-ruby-programming/9780596516178/ch04s03.html

>https://ruby-doc.org/docs/ruby-doc-bundle/UsersGuide/rg/constants.html



4. Cadenas de caracteres (strings), cadenas de caracteres.

5. Tipos de datos (Ruby es un lenguaje de tipado dinamico):

    - numerico (int)
    - cadena de caracteres
    - booleano

6. Condicionales y ciclos:
    + Definidos en ```parser.py```
        
    ``` python
        '''
        if_statement : IF expression THEN statements END
                                | IF expression THEN statements ELSE statements END
        '''

        '''
        while_statement : WHILE expression DO statements END
        '''

    ```

----

## Primera Entrega

### Casos de Prueba de Unidad (TestSet1)

En directorio ``` /test_set1/ ```

1. Un programa sencillo con un comentario de una palabra.
2. Un programa sencillo con un comentario de una línea.
3. Un programa sencillo con la definición de una variable.
4. Un programa sencillo con la definición de una constante.
5. Un programa sencillo con cadenas.
6. Un programa sencillo con variables de todos los tipos de datos.
7. Un programa sencillo con un ciclo y una condicional.
8. Un programa sencillo usando las instrucciones de entrada y salida.
9. Un programa sencillo con todas las instrucciones que has definido (mixed).


### TestSet2

En directorio ``` /test_set2/ ```

También debes crear los siguientes casos de prueba, todos deben definir:

1. Un programa sencillo con la definición de una variable en el lugar incorrecto y en el orden incorrecto.
2. Un programa sencillo que utiliza una cadena, variable y constante en un lugar que no está permitido.
3. Un programa sencillo con un ciclo definido pero usando una gramática incorrecta.

Todos los tokens no definidos en la definición formal de tu lenguaje deberán generar un error.
Todos los errores contenidos en una entrada deben estar presentes.

Si alguno de estos requisitos no se aplica a tu lenguaje de programación, prepárate para explicar por qué (Descrito en [Características](#Características-a-considerar)).


## Resultados 1

+ Tras ejecutar las prubas, la identificación de tokens resulta exitosa.
+ De igual que la detección de errores se sintaxis en el segundo set de pruebas.

## Ejecucion 

**El script de bash ejecuta el lexer y parser de todos los casos de prueba definidos y el resultado del analisis esta en ``` results.txt ```** (ya existente).

A ejecutar:

``` bash

$ ./run_all.sh > results1.txt

```


----

## Segunda Entrega

>**Todos los casos de prueba previos todavía son válidos.**


### TestSet3

Ademas, espero ver el AST (Abstract Syntax Tree) de estos casos, en directorio ``` /test_set3/ ```:

1.  Un programa sencillo con la definición de una variable.
2.  Un programa sencillo con la definición de una constante.
3.  Un programa sencillo con un ciclo y una condicional. Un programa con todas las instrucciones definidas.

### TestSet4

1. Un programa sencillo con la definición de una variable en el lugar incorrecto y en el orden incorrecto.
2.  Un programa sencillo que utiliza una cadena, variable y constante en un lugar que no está permitido.
3.  Un programa sencillo con un ciclo definido pero usando una gramática incorrecta.

### TestSet5

+ Los siguientes casos nuevos deben de pasar (aún cuando contengas entradas incorrectas).Asignar el valor a una variable que no corresponde con su tipo. Por ejemplo:

    ``` c++
    int a;
    a = "hello";
    ```

+ Llamar un método usando una clase que no contenga tal método. Por ejemplo:

    ``` c++
    class Rectangle {
        private: 
            int width, height;
        public:
            void set_values(int,int);
            int area();
        };
        
        int main() {
            Rectangle rect;
            rect.init(); //THIS METHOD WAS NOT DEFINED...
            return 0;
            }
    ````

+ Usar una variable fuera de su alcance. Por ejemplo:
``` c++
    int max(int num1,int num2){
    int result;
    if (num1 > num2) {
        result = num1;
    }
    else {
        result = num2;
    }
    return result;
    }
    // ...
    printf("Max value is : %d\n", result ); //result is not global variable

```



### Resultados 2

+ La identificación de tokens resulta exitosa, tanto en los sets previos como en los recien añadidos.

+ **El análisis de sintaxis muestra el arbol de sintaxis haciendo uso de una representacion por niveles (BFS)**, de igual manera se muestran los errores inyectados a proposito en de ``` ./test_set2/ ```, ``` ./test_set4/ ``` y ``` ./test_set5/ ```.

+ Sobre el ``` ./test_set5/ ```:
    1. Por su naturaleza de Ruby, es una gramática aceptada ya que ruby al ser interpretado y de tipado dinamico permite la reasignacion de variable independientemente del tipo inicial con el que fueron definidos
    2. Dentro de las características inicialmente definidas, no se incluyo el paradigma de Programación Orientada a Objetos, por lo cual es una gramática no aceptada.
    3. Por su naturaleza de Ruby, es una gramática aceptada ya que ruby al ser interpretado y de tipado dinamico, su escope tambien es dinámico y global.

## Ejecución 

**El script de bash ejecuta el lexer y parser de todos los casos de prueba definidos y el resultado del analisis esta en ``` results2.txt ```** (ya existente).

A ejecutar:

``` bash

$ ./run2.sh > results2.txt

```

----
### Ejecución Lexer

``` bash

$ python3 main_lexer.py [ruby_file]

```
#### Output

El output sera un listado de todos los tokens


### Ejecución Parser

``` bash

$ python3 main_parser.py [ruby_file]

```
#### Output

Si hay errores de sintaxis mostraran en el output

