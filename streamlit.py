#-------------------LIBRERIAS-----------------------#
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image #Para poder leer las imagenes jpg
import base64 #Para el gif
import io #Para ver la df.info()
import folium
from streamlit_folium import st_folium
#-------------------LIBRERIAS-----------------------#


#-------------------CONFIGURACIÓN-----------------------#
#Hay dos opciones de layout, wide or centered:
st.set_page_config(page_title = 'LA Airbnb', page_icon = '🏝️', layout='wide')
# Para que a la gente que use el codigo no le aparezcan los warnings de cambios en las librerias ponemos:
st.set_option('deprecation.showPyplotGlobalUse', False)
#-------------------CONFIGURACIÓN-----------------------#

#-------------------COSAS QUE VAMOS A USAR EN TODA LA APP-----------------------#
#opening the image
image1 = Image.open('img/Airbnb_Logo.svg.png')
image2 = Image.open('img/Los-Angeles.png')
image3= Image.open('img/map-los-angeles.jpg')

# gif from local file
#Gif Info
file_ = open('img/la.gif', "rb")
contents = file_.read()
data_url1 = base64.b64encode(contents).decode("utf-8")
file_.close()
#Gif conclusiones
file_2 = open('img/hollywood.gif', "rb")
contents2 = file_2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_2.close()


# Crear elementos en el menú sidebar
st.sidebar.header('Menú')
st.sidebar.markdown(
        f'<img src="data:image/gif;base64,{data_url1}" alt="cat gif" width="300" height="200">',
        unsafe_allow_html=True,
    ) 
selected_option = st.sidebar.selectbox('Selecciona una opción', ('Inicio','Preprocesamiento', 'Análisis exploratorio con PowerBi', 'Irregularidades'))

#Dataframes
df = pd.read_csv("data/listings_details.csv.gz",  compression='gzip',index_col= "id", low_memory=False)
df1 = pd.read_csv('data/clean_listings_details.csv')
df_out=pd.read_csv('data/price_wo_out_list_d.csv')
df_30 = df1[df1['minimum_nights']<30]
host_listings = df_30.groupby(['host_id', 'host_name','neighbourhood_group_cleansed']).size().reset_index(name='num_listings').sort_values(by=['num_listings'], ascending=False)
hl=host_listings[(host_listings['num_listings']>1) & (host_listings['num_listings']<=5)]
Min = df_30[df_30['host_id']== 445571173][['name','host_id', 'host_name', 'latitude', 'longitude']]



#--------------------gráficas----------------------------#
# Crear el gráfico con seaborn
fig, ax = plt.subplots(figsize=(10, 3))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='Pastel1', ax=ax)

fig1, ax = plt.subplots(figsize=(10, 3))
sns.heatmap(df1.isnull(), yticklabels=False, cbar=False, cmap='Pastel1', ax=ax)

map2 = folium.Map(location=[34.0725, -118.3018], zoom_start=20)
for coord in Min.itertuples(index=False):
    folium.Marker((coord.latitude, coord.longitude), tooltip=coord.name).add_to(map2)



#--------------------gráficas----------------------------#


#-------------------TITLE-----------------------#
st.title('ANALIZANDO AIRBNB: LOS ÁNGELES')
#-------------------TITLE-----------------------#

#--------------------------------------INICIO--------------------------------------#

# Lógica para cada opción seleccionada
if selected_option == 'Inicio':
    
    # Contenido de la página de inicio
    


    
#Texto  
    #Titulo:
    st.header('Origen de los datos 📂:')
    #Intro. Para que quedará centrado y pueda editar el texto en según que ocasiones se utiliza lenguaje html:
    st.markdown("""<span style='text-align: center; color: black;'>Los datos se han obtenido de Insideairbnb.com.  
                Inside Airbnb es un proyecto que proporciona datos y sensibiliza sobre el impacto de Airbnb en las comunidades residenciales de diferentes ciudades del mundo.  
                http://insideairbnb.com/about/</h2>""", unsafe_allow_html=True)  
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        st.image(image1, width=400)

    with col3:
        st.write(' ')
#Texto  
    #Titulo:
    st.header('¿Por qué Los Ángeles?:')
    #Intro. Para que quedará centrado y pueda editar el texto en según que ocasiones se utiliza lenguaje html:
    st.markdown("""<span style='text-align: center; color: black;'>La ciudad de Los Ángeles, situada en el sur de California (Estados Unidos), es la ciudad que **más multimillonarios alberga**💸.  
                Ciudad icónica por su letrero de Hollywood alberga los **estudios más fámosos del cine y la televisión** 🎬.  
                </h2>""", unsafe_allow_html=True)

    st.image(image3, width=900)

     
    st.markdown('''La oferta de alojamientos por Airbnb tiene una **estricta norma**:  
                *Para hospedar a alguien en plazos inferiores a 30 días se tiene que registrar el alojamiento:  
                Sólo las residencias principales pueden registrarse. Los anuncios registrados solo pueden alojar hasta 120 días al año natural.  
                El Ayuntamiento de Los Ángeles define la residencia principal como «la propiedad en la que resides durante más de 6 meses cada año natural».  
                De acuerdo con las ordenanzas de Los Ángeles, no puedes  
                1) solicitar u obtener más de un registro o  
                2) operar más de un anuncio de Airbnb en el momento de la ciudad de Los Ángeles.*  
                https://www.airbnb.es/help/article/864?_set_bev_on_new_domain=1687464214_ZjI4OWNiNGU2NDIz#section-heading-3-0''')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url2}" alt="cat gif">',
        unsafe_allow_html=True,
        ) 

    with col3:
        st.write(' ')       

    
#--------------------------------------INICIO--------------------------------------#

 #--------------------------------------PREPROCESAMIENTO--------------------------------------#   
    
    
elif selected_option == 'Preprocesamiento':
    st.title('Preprocesamiento:')
    # Contenido de la página de configuración
    st.markdown('Entre los datasets que aparecen en la web Insideairbnb se ha escogido para analizar "listings_details".')
    st.markdown("- *Antes de limpiar los datos hay: " + str(df.count()[0]) + " observaciones o data points.*")
    st.markdown("- *Antes de limpiar los datos hay: " + str(len(df.columns)) + " columnas.*")
    st.subheader('Valores nulos')
    st.markdown('Heatmap de valores nulos del dataset:')
    st.pyplot(fig)
    st.markdown('''***Aparecen columnas con el 100% de los valores nulos. Con al menos un 20% aproximadamente hay 21 columnas.  
    Se eliminan las columnas con más de un 18% de valores nulos primero.***''')
    st.markdown('''Se analizan las variables restantes una por una para ver si es interesante para el análisis o de lo contrario eliminarla del dataset:''')
    code = '''
        # Elimino las columnas con valores nulos que no quiero para nada:
        df1 = df1.drop(columns=['bedrooms', 'description', 'beds','bathrooms_text','maximum_nights_avg_ntm', 'minimum_nights_avg_ntm', 'maximum_maximum_nights','minimum_maximum_nights','host_since','host_thumbnail_url','host_identity_verified','host_has_profile_pic','host_verifications','host_picture_url','host_listings_count','host_total_listings_count'] , axis=1)
  
        #Se rellenan los valores nulos de las variables que si que nos interesan en principio utilizar:
  
        string_columns = df1.select_dtypes(include=['object']).columns.tolist()
        numerical_columns = df1.select_dtypes(include=['int', 'float']).columns.tolist()
        
        #Para rellenar variables string/objeto con '?':
        df1[string_columns] = df1[string_columns].fillna('?')
  
        #Para rellenar variables numéricas con 0:
        df1[numerical_columns] = df1[numerical_columns].fillna(0)'''
    st.code(code, language='python')
    st.pyplot(fig1)
    st.markdown('✨¡Perfecto ya no hay valores nulos!✨')
    
    st.subheader('Valores duplicados')
    code1 = '''df1.duplicated().sum()'''
    st.code(code1, language='python')
    st.markdown('= 0')
    st.markdown('✨¡Perfecto no hay valores duplicados!✨')
    
    st.subheader('Variables inútiles')
    st.markdown('''En una excel he compiado todas las variables del database con la información relacionada y una vez revisadas he hecho una selección de ellas, por lo tanto, eliminaremos a continuación las que no me parecen interesantes para analizar: ''')
    code2='''df1 = df1.drop(columns=['listing_url', 'scrape_id', 'last_scraped', 'source','picture_url','host_url','amenities','maximum_nights', 'has_availability', 'availability_30',
       'availability_60', 'availability_90', 'availability_365',
       'calendar_last_scraped','number_of_reviews_ltm',
       'number_of_reviews_l30d'])'''
    st.code(code2, language='python')
    
    st.subheader('Tipo de datos de las variables:')
    st.markdown('''Vemos que hay un par de variables que deberíamos modificar:  
                host_id y price:''')
    st.markdown('**host_id** aparece como "integer" lo convertimos a string, no es un número, *es una variable categórica:*')
    code3='''df1['host_id']=df1['host_id'].astype(str)'''
    st.code(code3, language='python')
    st.markdown('''**price** aparece como object (es decir una cadena de texto) con el siguiente formato: $399.00.  
                Lo convertimos a string, no es un número como tal es un id, es decir, *es una variable categórica:*''')
    code4= '''df1['price'] = df1['price'].replace('[\$,]', '', regex=True).astype(float)'''
    st.code(code4, language='python')
    st.markdown('✨¡Perfecto las variables ya tienen el formato correcto!✨')
    
    st.subheader('Dataframes:')
    st.markdown('Trabajaremos con dos dataframes uno que contiene outliers en los precios y otro sin ellos:')
    st.markdown('**Dataframe con outliers:**')
    st.dataframe(df1)
    
    st.markdown('**Dataframe sin outliers:**')
    code5='''def outliers_df(df, columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1   
    df = df[(df[columna] >= Q1-1.5*IQR) & (df[columna] <= Q3 + 1.5*IQR)]
    return df

    df_out = df1.copy()
    columna_outliers = 'price'  
    df_out = outliers_df(df_out, columna_outliers)'''
    st.code(code5, language='python')
    st.dataframe(df_out)
    st.markdown('✨¡Perfecto ya tenemos los dataframes listos!✨')
    st.markdown("***-Después de limpiar los datos hay: " + str(df1.count()[0]) + " observaciones o data points.***")
    st.markdown("***-Después de limpiar los datos hay: " + str(len(df1.columns)) + " columnas.***") 


#--------------------------------------PREPROCESAMIENTO--------------------------------------#   
#--------------------------------------POWERBI--------------------------------------#   
elif selected_option == 'Análisis exploratorio con PowerBi':       

    def main():
            
        st.title("Analizando los precios y el tipo de alojamiento con Power BI:")
        powerbi_embed_code = """ <iframe title="Report Section" width="1700" height="850" src="https://app.powerbi.com/view?r=eyJrIjoiMzYzOTQ5MjAtZTgxMy00ZGMwLTg4MWItYjUwNjE4NzVhZTg0IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>    """
        st.markdown(powerbi_embed_code, unsafe_allow_html=True)

    if __name__ == "__main__":
        main()
#--------------------------------------POWERBI--------------------------------------#  
#--------------------------------------Irregularidades--------------------------------------#    
elif selected_option == 'Irregularidades':
    st.title('Análisis de irregularidades 👮‍♀️👮‍♂️:')
    
    st.markdown('''Airbnb impone una serie de normas al "host" o anfitrión en relación a estancias menores de 30 noches, como ya se ha mencionado en la página de Inicio.  
                ***Para hospedar a alguien en plazos inferiores a 30 días se tiene que registrar el alojamiento y sólo las residencias principales pueden registrarse.***  
                Es decir, que el anfitrión sólo puede ofrecer su vivienda habitual para estancias menores de 30 días.''')
    st.markdown('Vamos a ver que posibles anfitriones pueden estar infringiendo esta norma a partir del dataset filtrado por minimum_nights <30')
    st.dataframe(hl)
    st.markdown('''En este dataframe se ha filtrado por aquellos anfitriones que tienen entre 1 y 5 anuncios (por acotar la información).  
                Seleccionamos por ejemplo al "host" Min que tiene 5 anuncios:''')
    st.dataframe(Min)
    st.markdown('A primera vista se puede comprobar que hay diferentes coordenadas, por lo tanto, se ven ubicaciones diferentes, vamos a verlo en un mapa mejor:')
    st_data = st_folium(map2, width=725)
    st.markdown('''Vemos que efectivamente este anfitrión ofrece más de un alojamiento para estancias inferiores a 30 noches. 
                Por lo que esta persona está incumpliendo con la normativa.''')

#--------------------------------------Irregularidades--------------------------------------#     