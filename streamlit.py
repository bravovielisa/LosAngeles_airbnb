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

# gif from local file
#Gif Info
file_ = open('img/la.gif', "rb")
contents = file_.read()
data_url1 = base64.b64encode(contents).decode("utf-8")
file_.close()
#Gif conclusiones
file_2 = open('img/hills.gif', "rb")
contents2 = file_2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_2.close()


# Crear elementos en el menú sidebar
st.sidebar.header('Menú')
selected_option = st.sidebar.selectbox('Selecciona una opción', ('Inicio','Preprocesamiento', 'Precios', 'Correlaciones', 'Irregularidades'))

#Dataframes
df = pd.read_csv("data/listings_details.csv.gz",  compression='gzip',index_col= "id", low_memory=False)
df1 = pd.read_csv('data/clean_listings_details.csv')

#--------------------gráficas----------------------------#
# Crear el gráfico con seaborn
fig, ax = plt.subplots()
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='inferno', ax=ax)

fig1, ax = plt.subplots()
sns.heatmap(df1.isnull(), yticklabels=False, cbar=False, cmap='inferno', ax=ax)

#--------------------gráficas----------------------------#


#-------------------TITLE-----------------------#
st.title('ANALIZANDO AIRBNB: LOS ÁNGELES')
#-------------------TITLE-----------------------#



# Lógica para cada opción seleccionada
if selected_option == 'Inicio':
    
    # Contenido de la página de inicio
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(' ')

    with col2:
        st.image(image1, width=800)

    with col3:
        st.write(' ')
    with col4:
        st.write(' ')
    with col5:
        st.write(' ')
    
#Texto  
    #Titulo:
    st.header('Origen de los datos:')
    #Intro. Para que quedará centrado y pueda editar el texto en según que ocasiones se utiliza lenguaje html:
    st.markdown("""<span style='text-align: center; color: black;'>Los datos se han obtenido de Insideairbnb.com.
                Inside Airbnb es un proyecto que proporciona datos y sensibiliza sobre el impacto de Airbnb en las comunidades residenciales de diferentes ciudades del mundo.
                http://insideairbnb.com/about/</h2>""", unsafe_allow_html=True)    
    
    
    
    
elif selected_option == 'Preprocesamiento':
    st.title('Página de preprocesamiento')
    # Contenido de la página de configuración
    
    st.pyplot(fig)
    st.pyplot(fig1)
    
elif selected_option == 'Precios':
    st.title('Página de precios')
    # Contenido de la página de ayuda
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(' ')

    with col2:
        st.image(image2, width=800)

    with col3:
        st.write(' ')
    with col4:
        st.write(' ')
    with col5:
        st.write(' ')
    def main():
            
        st.title("Aplicación Power BI")
        powerbi_embed_code = """ <iframe title="Report Section" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiMzYzOTQ5MjAtZTgxMy00ZGMwLTg4MWItYjUwNjE4NzVhZTg0IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>    """
        st.markdown(powerbi_embed_code, unsafe_allow_html=True)

        if __name__ == "__main__":
            main()

elif selected_option == 'Correlaciones':
    st.title('Página de correlaciones')
    # Contenido de la página de ayuda
    


elif selected_option == 'Irregularidades':
    st.title('Página de irregularidades')
    # Contenido de la página de ayuda