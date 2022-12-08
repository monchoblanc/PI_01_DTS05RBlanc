
from fastapi import FastAPI   #, HTTPException. VER SI LA LLEGO A UTILIZAR!!
import pandas as pd

app = FastAPI()

#creo el all_df para que lo usen mis funciones:
all_df=pd.read_csv('Datasets/all_platforms.csv')

@app.get('/')
async def read_root():
    return {'API Plataformas de Streaming. CONSULTAS: get_listedin/?genero=string , /get_count_platform/?plataforma=string , /get_max_duration/?anio=int&plataforma=string&duration=string , /get_actor/?plataforma=string&anio=int PLATAFORMAS: disney, amazon, hulu, netflix. DURATION: min o season.'}   

#agrego mis funciones, traidas del ETL.ipynb:

#1. Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo:
@app.get('/get_listedin/') #le saco el {genero} de aca, y asi me toma el url como /get_listedin/?genero=Comedy
async def get_listedin(genero:str): 
    # if genero not in all_df.listed_in.values ...return....o seria levantando un HTTPException 
    #para cada plataforma, calculo el numero para el genero:
    a=all_df[all_df['listed_in'].str.contains(genero) & (all_df['platform']=='amazon')].shape[0]
    d=all_df[all_df['listed_in'].str.contains(genero) & (all_df['platform']=='disney')].shape[0]
    h=all_df[all_df['listed_in'].str.contains(genero) & (all_df['platform']=='hulu')].shape[0]
    n=all_df[all_df['listed_in'].str.contains(genero) & (all_df['platform']=='netflix')].shape[0]
    #le tomo el maximo:
    m= max(a,d,h,n) #si aumentase el # de plataformas, recorro una lista con un for....
    if m==a:   #ver manera mas linda/corta de elegir la plat?
        plat='amazon'
    elif m==d:
        plat='disney'
    elif m==h:
        plat='hulu'
    else: 
        plat='netflix' 
    #faltaria ver si en algun caso da el mismo numero para alguna! una lista [a d h n] y ver si .unique() da menor que len(lista)?
    return f'el genero {genero} se repite con mayor frecuencia en la plataforma {plat} . Se repite {m} veces.'

#2. Cantidad de películas y series (separado) por plataforma:
@app.get('/get_count_platform/')  #{plataforma}
async def get_count_platform(plataforma:str):
    #if plataforma not in ['amazon', 'disney', 'hulu', 'netflix']..return   ingrese alguna de estas [lista platafs]'...
    #calculo el numero para 'TV Show' y para 'Movie':
    tv=all_df[(all_df['type']=='TV Show') & (all_df['platform']==plataforma)].shape[0]
    movie=all_df[(all_df['type']=='Movie') & (all_df['platform']==plataforma)].shape[0]
    return f'{plataforma} tiene {tv} TV Shows y {movie} Movies'

#3. Funcion duracion maxima por tipo, anio y plataforma:
@app.get('/get_max_duration/')  #{anio}{plataforma}{duration}
async def get_max_duration(anio:int, plataforma:str, duration:str): 
    #separo en casos para 'duration':
    if duration =='min':
        #filtro segun type=Movie, anio y plataforma:
        dur_movie = all_df[(all_df['type']=='Movie') & (all_df['platform']==plataforma) & (all_df['release_year']==anio)]
        serie = dur_movie.duration.str.strip('min')  #le saco el 'min'
        serie.dropna(inplace=True)     #tiro nulos para poder pasar todo a int (sino chilla).
        serie=serie.astype(int)        #lo paso a int. 
        max_ind = serie.idxmax() #indice del max_val. OJO me devuelve el 1er INDICE. tendria q luego buscar TODOS los indices con el max_val!!
        max_val = serie.max() #maximo valor. 
        #titulo=dur_movie.title.loc[max_ind] #agregue el for asiq ya no necesito esto, lo dejo por las dudas que el for rompa...
        #busco todos las filas tq tienen el valor maximo:
        ind=serie[serie==max_val].index #me da un typeIndex con el (o los) indices para el max. 
        #lo recorro guardando los titulos:(calculo q casi siempre sera uno solo o pocos asiq este for no hace mucho)
        titulos=[]
        for i in ind:
            titulos.append(dur_movie.title.loc[i])
        return f'duracion maxima para "Movie" en el anio {anio}, en {plataforma} es de {max_val} minutos, para el/los titulos: {titulos}.' #estaria bueno sacarle los '[]' asi queda mas lindo...escape character?

    #ahora misma cosa pero para 'TV Show':
    if duration=='season':
        dur_TV_Show=all_df[(all_df['type']=='TV Show') & (all_df['platform']==plataforma) & (all_df['release_year']==anio)]
        serie = dur_TV_Show.duration.str.strip('Seasons')  #le saco el 'Seasons', con lo cual tmb le saco 'Season'
        serie.dropna(inplace=True)     
        serie=serie.astype(int)   
        max_ind = serie.idxmax() #indice del max_val. OJO me devuelve el 1er INDICE. tendria q luego buscar TODOS los indices con el max_val!!
        max_val = serie.max() #maximo valor. 
        #titulo=dur_movie.title.loc[max_ind] #agregue el for asiq ya no necesito esto, lo dejo por las dudas que el for rompa...
        #busco todos las filas tq tienen el valor maximo:
        ind=serie[serie==max_val].index #me da un typeIndex con el (o los) indices para el max. 
        #lo recorro guardando los titulos:(calculo q casi siempre sera uno solo o pocos asiq este for no hace mucho)
        titulos=[]
        for i in ind:
            titulos.append(dur_TV_Show.title.loc[i])
        return f'duracion maxima para "TV Show" en el anio {anio}, en {plataforma} es de {max_val} temporadas, para el/los titulos: {titulos}.' 

    else:    
        return 'tercer parametro debe ser "min" o "season".'

#4. Actor que más se repite según plataforma y año:
@app.get('/get_actor/')   #{plataforma}{anio}
async def get_actor(plataforma:str, anio:int):
    #para plataforma==hulu, son todos None..luego salvo esa opcion:
    if plataforma=='hulu':
        return 'Informacion no disponible para plataforma hulu.'
    else:
        #if type(anio)!= int:        return 'anio debe ser un numero entero'    else... #esto lo puedo meter como HTPException mejor..
        data=all_df[(all_df['release_year']==anio) & (all_df['platform']==plataforma)] #filtro por los argumentos.
        serie=data.cast
        # separo por 'terminos' separados por coma, y los meto en la lista 'actores':
        actores=[]
        #serie.reset_index(drop=True, inplace=True) #NO HACIA FALTA pues al pasarla a lista se reindexa...
        serie=list(serie) #convierto a lista y la recorro:
        for i in range(0,len(serie)):
            if ',' not in str(serie[i]): #ie, si es un solo nombre (o son varios pero sin coma, lo tomo como uno solo, anda mal en algunos casos, peeero, si uso tipo regex (str.contains()) anda igual, y sino, igual no son muchos)
             actores.append(serie[i]) #NOTAR: son solo 49 las expresiones de .cast con mas de 3 palabras!. asiq no es mucho, casi q lo podria normalizar a mano...
            else:
                sep=str(serie[i]).split(",") #los separo en una serie, y nuevamente los agrego de a uno a actores. ME CHILLA SIN EL str(). x no converir el type de la columna?
                for j in range(0,len(sep)):
                    actores.append(sep[j])                 
    #AHORA 'actores' es una lista con todos los actores, ya filtrado por ese anio y plataforma.
    #resta ver cual se repite mas y cuantas veces. 
        actores=pd.Series(actores)
        actores.value_counts()
        winner=actores.value_counts().index[0]
        cantidad=actores.value_counts()[0]

        #hay q ver si son varios actores con el mismo count:
        k=1
        ganadores=[winner]
        while actores.value_counts()[k]==cantidad:
            ganadores.append(actores.value_counts().index[k])
            k+=1
        if k==1:
            return f'actor que mas se repite: {winner}, aparece {cantidad} veces.'
        else:
            return f'actores que mas se repiten: {ganadores}, aparecen {cantidad} veces.'