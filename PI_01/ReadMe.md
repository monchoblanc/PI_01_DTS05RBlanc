                                                Individual Project 01, Data Science 05, by Ramon Blanc

We are asked to carry out a Data Engineer project, with an ETL process and the implementation of a dockerized FastAPI that can respond to specific GET queries as specified in the instructions.

Following, I will describe how I carried out the project.

First, I created the project folder and saved the datasets as where provided in the forked repository. For the sake of simplicity, I chose to perform the ETL process in Python using Pandas, as it seemed easier to Dockerize the application compared to using MySQL or other tools.

Next, I started the ETL process within the 'ETL.ipynb' notebook. I began by importing the Pandas module. At first glance, the datasets had similar characteristics in terms of data types and columns, so after checking these basic things, I proceeded to concatenate all the datasets. To do this, I first differentiated the 'Show_id' field to maintain its uniqueness and also added a column that referenced the original dataset.

Again, for simplicity, I tried to minimize changes, so I did not delete any columns, even though I had identified which ones were useful and which ones were not for the required queries. Since this was my first ETL project beyond the practices in the bootcamp, I preferred to perform transformations "on demand," meaning as they were needed to develop the functions. This ultimately resulted in several transformations being done directly within the function.

As the final general step in the ETL process, I developed the functions within the same notebook. This process can be observed in the notebook, including some minimal modifications and checks to ensure that the results were on the right track (for example, that the number of fields with more than one actor not separated by commas did not represent a large percentage of the total records). Given that the deadline for commiting this project was very soon, I decided that the ETL process was sufficient once the four required functions were working as expected.

I then moved on to the next stage, creating the Docker image, running it, and making queries to the API. I had several failed attempts until finally, after modifying some routes, lines of code, and file arrangements, I achieved the desired outcome.

Once I was confident that my image could run a FastAPI instance locally, I proceeded to incorporate my functions into the main.py file. Additionally, I realized that I needed to convert my concatenated DataFrame back to CSV so that the API could load it upon startup and run the main.py. This did not pose any problems.

After completing all of the above, I tested making queries from the browser, entering different parameters for each one. In all cases, the API's response was satisfactory, so I considered the project objective fulfilled.

I am aware that my data transformation and normalization process could have been more extensive, but I felt that it was sufficient for the scope of the project.

In conclusion, these were days packed with learning and practical application of concepts learned throughout the Bootcamp. 
                               
                               
SPANISH VERSION:                                
                               
                               Proyecto Individual 01, Data Science 05, por Ramon Blanc

Se nos pide que realicemos un proyecto de Data Engineer, con proceso de ETL y realizacion de una FastApi dockerizada, pudiendo esta responder a consultas especificadas en las consignas, de tipo GET. 

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


