# WebScraping

## Componentes del grupo

- Paula Frías Arroyo
- Miguel Artigues Canaves

## Descripción ficheros

### VERSION 1

En esta versión se guardan los datos con formato tabular en un único fichero csv en el que se irán añadiendo los datos en cada ejecución.

- cryclass.py: clase que contiene las funciones para realizar web scraping y almacenar los datos en formato CSV.
- main.py: fichero principal que invoca a la clase `cryclass.py` para realizar el web scraping.

### VERSION 2

Esta versión hace un guardado de los datos en un estructura de carpetas por año, mes y día. Contiene opción para plotear datos.

- cryclass.py: contiene las funciones para scrapear, guardar y plotear datos.
- collect_data.py: contiene bucle para recoger datos.
- plot_data.py: plotea datos de una moneda y fecha concretas indicadas por parámetro.
- imports_func.py: contiene todos los comandos para cargar librerías
