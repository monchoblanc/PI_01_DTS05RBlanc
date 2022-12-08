
                                
                                Proyecto Individual 01, Data Science 05, por Ramon Blanc

Se nos pide que realicemos un proyecto de Data Engeneer, con proceso de ETL y realizacion de una FastApi dockerizada, pudiendo esta responder a consultas especificadas en las consignas, de tipo GET. 

Paso a describir el proceso llevado a cabo.

En primer lugar, cree la carpeta del proyecto, y guardé ahi los Datasets provistos en el repositorio. Por simpleza de procedimientos, elegi desde un primer momento realizar el ETL en python con pandas, ya que me parecio mas sencillo al momento de tener que dockerizar la applicacion, temiendo poder encontrar obstaculos mayores en ese aspecto para MySql u otras herramientas. 

Luego inicie el proceso de ETL, dentro del notebook 'ETL.ipynb'. Comence importando el modulo pandas (para mi sorpresa, no me fue necesario nigun otro modulo). A primera vista, los datasets presentaban caracteristicas similares en cuanto a tipos de dato y columnas, por lo que luego de chequear estas cosas basicas, procedí a concatenar todos los datasets. Para esto, primero diferencie el campo Show_id para que siga manteniendo su unicidad, y agregue ademas una columna que referencie al Dataset original. 

Nuevamente, por simplicidad, intente minimizar los cambios, por lo cual no elimine columnas, por mas de haber identificado cuales me eran utiles y cuales no, para realizar las consultas requeridas por consigna.
Al ser este mi primer proyecto de ETL mas alla de las practicas en el Bootcamp, preferi realizar las transformaciones 'a demanda', es decir, a medida que me fueran necesarias para poder desarrollar las funciones. Esto derivo finalmente en que varias de las transformaciones las realiza directamente la funcion. 

Como ultimo paso general en el proceso de ETL, desarrolle las funciones, dentro del mismo notebook. Se puede observar este proceso dentro del notebook, y cómo realizo algunas minimas modificaciones y chequeos, para asegurarme que los resutados van por buen camino (por ejemplo, que el numero de campos con mas de un actor no separados con coma, no represente un gran porcentaje del total de registros). Teniendo este Proyecto un tiempo total de ejecucion bastante acotado, decidi que era sufieciente ETL, una vez que las cuatro funciones requeridas estaban 'funcionales'. 

Pasé entonces a la siguiente etapa, crear la imagen de docker, correrla, y realizar las consultas a la API. Tuve varios intentos fallidos, hasta que finalmente, luego de mmodificar algunas rutas, lineas de codigo, y disposicion de archivos, logre lo deseado. 

Una vez seguro de que mi imagen ya podia correr una instancia de FastApi localmente, pase a incorporar mis funciones al archivo main.py. Ademas, me di cuenta que debia pasar mi DataFrame concatenado, nuevamente a csv, para que la API pueda levantarlo al iniciarse y correr el main.py. Esto no me trajo problemas. 

Una vez realizado todo lo anterior, probé realizar las consultas desde el navegardor, ingresando diferentes parametros para cada una. En todos los casos, la respuesta de la Api fue satisfactoria, con lo cual di por cumplido el objetivo del Proyecto. 

Tengo presente el hecho de que mi proceso de Transformacion y Normalizacion de datos podria haber sido mas extensivo, pero me parecio que para el alcance del proyecto era igualmente suficiente. 

Concluyendo, fueron dias de muchisimo aprendizaje y puesta en practica de conceptos, los cuales no habia podido revisar ya que hubo muy poco tiempo entre el final del M6 y el inicio de este Proyecto. 


