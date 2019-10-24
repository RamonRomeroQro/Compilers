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

    Special thanks to: 
    @Manchas2k4, @EduardoLarios and @dabeaz (PLY)
    

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
   
    statements  : T statement T statements	
                | T statement T 
    '''


    ```


3. Variables y constantes: 

Ruby es un lenguaje de tipado dinamico, por lo que no requiere de palabras reservadas como ```int``` o ```float```, unicamente que comiencen con una letra y sean seguidas de letras, numeros o underscore:  ```[a-z_][a-zA-Z0-9_]*' ```

Las constantes son identificadas son identificadas por que comienzan con una letra mayuscula [A-Z], sin embargo, permanece mutable y su comportamiento es homólogo al de las variables: ``` r'[A-Z][a-zA-Z0-9_]*' ```


> The Ruby interpreter does not actually enforce the constancy of constants.
>https://www.oreilly.com/library/view/the-ruby-programming/9780596516178/ch04s03.html
https://ruby-doc.org/docs/ruby-doc-bundle/UsersGuide/rg/constants.html



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

### Casos de prueba de unidad

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

---

## Casos de prueba

En directorio ``` /test_set2/ ```


También debes crear los siguientes casos de prueba, todos deben definir:

1. Un programa sencillo con la definición de una variable en el lugar incorrecto y en el orden incorrecto.
2. Un programa sencillo que utiliza una cadena, variable y constante en un lugar que no está permitido.
3. Un programa sencillo con un ciclo definido pero usando una gramática incorrecta.

Todos los tokens no definidos en la definición formal de tu lenguaje deberán generar un error.
Todos los errores contenidos en una entrada deben estar presentes.
Si alguno de estos requisitos no se aplica a tu lenguaje de programación, prepárate para explicar por qué.

## Ejecucion y resultados

**El script de bash ejecuta el lexer y parser de todos los casos de prueba definidos y el resultado del analisis esta en ``` results.txt ```** (ya existente).

A ejecutar:

``` bash

$ ./run_all.sh > results.txt

```

### Notas

+ Tras ejecutar las prubas, la identificación de tokens resulta exitosa.
+ De igual que la detección de errores se sintaxis en el segundo set de pruebas.


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

Si hay errores de sintaxis mostraran en el outout


----

## Segunda Entrega

### TestSet3

En directorio ``` /test_set3/ ```

Todos los casos de prueba previo todavía son válidos. Ademas, espero ver el AST (Abstract Syntax Tree)de estos casos:
1.  Un programa sencillo con la definición de una variable.
2.  Un programa sencillo con la definición de una constante.
3.  Un programa sencillo con un ciclo y una condicional. Un programa con todas las instrucciones defini-das.

### TestSet4

1. Un programa sencillo con la definición de una variable en el lugar incorrecto y en el orden incorrecto.
2.  Un programa sencillo que utiliza una cadena, variable y constante en un lugar que no está permitido.
3.  Un programa sencillo con un ciclo definido pero usando una gramática incorrecta.

### TestSet5

+ Los siguientes casos nuevos deben de pasar (aún cuando contengas entradas incorrectas).Asignar el valor a una variable que no corresponde con su tipo. Por ejemplo:

    ``` c
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

## Casos de prueba

En directorio ``` /test_set2/ ```


También debes crear los siguientes casos de prueba, todos deben definir:

1. Un programa sencillo con la definición de una variable en el lugar incorrecto y en el orden incorrecto.
2. Un programa sencillo que utiliza una cadena, variable y constante en un lugar que no está permitido.
3. Un programa sencillo con un ciclo definido pero usando una gramática incorrecta.

Todos los tokens no definidos en la definición formal de tu lenguaje deberán generar un error.
Todos los errores contenidos en una entrada deben estar presentes.
Si alguno de estos requisitos no se aplica a tu lenguaje de programación, prepárate para explicar por qué.

## Ejecucion y resultados

**El script de bash ejecuta el lexer y parser de todos los casos de prueba definidos y el resultado del analisis esta en ``` results.txt ```** (ya existente).

A ejecutar:

``` bash

$ ./run_all.sh > results.txt

```

### Notas

+ Tras ejecutar las prubas, la identificación de tokens resulta exitosa.
+ De igual que la detección de errores se sintaxis en el segundo set de pruebas.


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

Si hay errores de sintaxis mostraran en el outout

