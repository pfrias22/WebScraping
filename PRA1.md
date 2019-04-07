# PRÁCTICA 1 - WEB SCRAPING

## CONTEXTO

El contexto en que se ha recolectado la información ha sido en base a una de las fuentes más confiables para encontrar datos estadísticos sobre las criptodivisas en circulación. Su página principal (`https://coinmarketcap.com/`) es una de las más visitadas por los entusiastas e inversores en el terreno de las monedas digitales.

Nuestro contexto se ha centrado únicamente en el ranking actual de criptomonedas, sus precios y capitalizaciones de mercado actualizado en tiempo real.

En la versión 1 se recogen las 100 primeras criptomonedas del ranking de coinmarketcap, y en la versión 2 se recolectan solo las monedas indicadas por parámetro con el objetivo de tener siempre información de las mismas monedas (evitar tener información solo de ciertos momentos temporales de las monedas cercanas a la posición 100 del ranking).

## TÍTULO

El titulo de este dataset podría ser `CryptoCurrencyRanking`.

## DESCRIPCIÓN DEL DATASET

***Versión 1***
El conjunto de datos contiene el ranking de las 100 primeras criptomendas en base a sus precios y capitalizaciones de mercado, con una reseña de tiempo con el fin de poder ejecutar en más de una ocasión el fichero Python, para conseguir un modelo tabular en formato CSV.

***Versión 2***
El conjunto de datos contiene el ranking de las criptomendas indicadas por parámetro en base a sus precios y capitalizaciones de mercado, con una reseña de tiempo con el fin de poder ejecutar en más de una ocasión el fichero Python. En este caso, la creación de los CSV se realiza de forma jerárquica mediante una estructura de carpetas basadas en año, mes y día.

## REPRESENTACIÓN GRÁFICA

***Representación gráfica versión 1***
![Dataset v1](./images/v1.png)

***Representación gráfica versión 2***
![Dataset v2](./images/v2.png)

## CONTENIDO

***Campos del conjunto de datos***
El conjunto de datos extraído se compone de los siguientes atributos:

- Number: Posición en el ranking.
- Name: Nombre de la criptomoneda.
- Market cap: Capitalización de la moneda en el mercado.
- Price: Precio de la moneda en el mercado (en dicho momento).
- Volume (24h): Volumen total de la criptmoneda en 24 horas.
- Circulating Supply:
- Change (24h): Porcentaje de subida o bajada del valor de la criptomoneda.
- timestamp: datetime en el que se ha recolectado la información.

***Periodo de tiempo del conjunto de datos***
Al estar los datos recogidos a través de una web en tiempo real, el periodo de tiempo del conjunto de datos es únicamente sobre el instante de tiempo definido en la columna `timestamp`. 

***¿Cómo se han recogido los datos?***
Los datos se han recogido mediante el uso del paquete de Python `BeautifulSoup`.

En primer lugar, hemos accedido a la página web `https://coinmarketcap.com/` y hemos almacenado todo el html en una variable.

Tras esto, ambas versiones realizan el web scraping y el almacenamiento de maneras diferentes:

***Versión 1***
En la versión 1, se obtiene la cabecera del conjunto de datos directamente del html obtenido mediante el uso del paquete `BeautifulSoup` accediendo a las etiquetas `hr > td`. De esta manera obtendremos el nombre de las columnas que tendrá el conjunto de datos.

A continuación, se obtendrá el cuerpo del conjunto de datos. El acceso esta vez será a las etiquetas `tr > td`.

Una vez realizado esto, recorreremos el array bidimensional generado, para solo insertar los datos que nos interesan de los recogidos en el array.

Una vez limpiado el array bidimensional, se generará un fichero CSV mediante la cabecera obtenida al principio, y el cuerpo del fichero obtenido en el paso anterior.

Todo esto se realizará en un bucle que se lanzará cada minuto.

***Versión 2***
En la versión 2, generamos un conjunto de datos con la cabecera correspondiente a los datos que vamos a almacenar.

Tras el paso anterior, obtenemos el html de la página web mediante el uso del paquete `BeautifulSoup` accediendo a las etiquetas `td`. De los objetos encontrados, nos quedamos solo con los que contienen información (ignoramos los que tienen valor "None"). Acto seguido también comprobamos que el objeto obtenido contiene el número de valores adecuado y si es así lo añadimos al dataset. Una vez se han recogido los datos de todas la monedas indicadas, se comprueba si ya existe el fichero de datos correspondiente a la fecha de recogida. En caso positivo se le añaden las líneas obtenidas. De lo contrario lo creamos y le añadimos las líneas.

Todo esto se realizará en un bucle que se lanzará cada minuto.

## AGRADECIMIENTOS

Agradecer a Brandon Chez, fundador de CMC (CoinMarketCap), haber desarrollado esta página, la cual nos ha permitido contener en un dataset un histórico de las cotizaciones y precios de las primeras 100 o 5 criptomonedas.

## INSPIRACIÓN

Este conjunto de datos es interesante ya que de esta manera podemos disponer de un histórico de las cotizaciones y precios del ranking de criptomonedas.

Las preguntas que se pretenden responder serían las siguientes:

- Hacer predicciones sobre la tendencia y los cambios que sufriran los valores de las criptomonedas para así decidir cuando es un buen momento para invertir.
- Relacionar cambios en los valores de las criptomonedas con eventos. Podríamos preguntarnos por ejemplo que criptomoneda va a sufrir una mayor devaluación porque Reino Unido abandone la Unión Europea.

Además se puede utilizar el código para programar avisos en función de ciertos comportaminetos como cambios abruptos de valores.

## LICENCIA

La licencia que va a tener este conjunto de datos va a ser:

- Released Under CC0: Public Domain License

Hemos seleccionado este tipo de licencia puesto que
