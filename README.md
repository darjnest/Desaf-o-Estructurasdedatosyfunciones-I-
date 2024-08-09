# Desaf-o-Estructurasdedatosyfunciones-I-
Desafío - Estructuras de datos y funciones (I)

# Desafío - Estructuras de Datos y Funciones (I)

Este repositorio contiene soluciones para un desafío que pone a prueba el uso de estructuras de datos y funciones en Python. A continuación, se detallan los requisitos y la implementación de tres programas.

## Requisitos

### 1. Conversión de Moneda

Crea un archivo llamado `conversiones.py` que permita ingresar tasas de conversión para las siguientes divisas mediante `sys.argv` en el siguiente orden:

- Sol
- Peso Argentino
- Dólar Americano

Además, ingresa un cuarto argumento que sea el valor en pesos chilenos a convertir. El programa debe devolver el valor en pesos chilenos convertido en las tres divisas ingresadas.

**Tasas de conversión de Peso Chileno:**
- a Sol peruano: 0.0046
- a Peso Argentino: 0.093
- a Dólar Americano: 0.00013

**Ejemplo de ejecución:**
```sh
python conversiones.py 0.0046 0.093 0.00013 10000
Respuesta esperada:

css
Copiar código
Los 10000 pesos equivalen a:
46.0 Soles
930.0 Pesos Argentinos
13.0 Dólares
2. Contador de Palabras y Caracteres
Crea un archivo llamado word_count.py que importe un texto desde un archivo y realice las siguientes tareas:

Contar la cantidad de caracteres distintos que componen el texto.
Contar el número de palabras distintas que componen el texto ingresado.
Utiliza el método .split() para separar el texto por espacios.

Ejemplo de ejecución:

sh
Copiar código
python word_count.py lorem_ipsum.txt
Respuesta esperada:

yaml
Copiar código
El número de caracteres distintos es: 40
El número de palabras distintas es: 243
3. Gestión de Recordatorios
Crea un archivo llamado recordatorios.py que incluye una serie de eventos con la siguiente estructura: fecha (año-mes-día), hora, y descripción del evento. Aplica las siguientes modificaciones para mantener el orden temporal:

Agrega un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
Cambia el evento del 15 de Julio al 16 de Julio.
Elimina el evento del Día del Trabajo.
Agrega una cena de Navidad el 24 de Diciembre y una cena de Año Nuevo el 31 de Diciembre, ambas a las 22:00.
Ejemplo de ejecución:

sh
Copiar código
python recordatorios.py
Respuesta esperada:

css
Copiar código
[['2021-01-01', '11:00', 'Levantarse y ejercitar'],
 ['2021-02-02', '06:00', 'Empezar el Año'],
 ['2021-07-16', '13:00', 'No hacer nada es feriado'],
 ['2021-09-18', '16:00', 'Ramadas'],
 ['2021-12-24', '22:00', 'Cena de Navidad'],
 ['2021-12-25', '00:00', 'Navidad'],
 ['2021-12-31', '22:00', 'Cena de Año Nuevo']]
Cómo Ejecutar

Conversión de Moneda:
sh
Copiar código
python conversiones.py <tasa_sol> <tasa_peso_arg> <tasa_dolar> <valor_peso_chileno>
Contador de Palabras y Caracteres:
sh
Copiar código
python word_count.py <archivo_texto>
Gestión de Recordatorios:
sh
Copiar código
python recordatorios.py