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




def main():
            
    st.title("Aplicación Power BI")
    powerbi_embed_code = """<iframe title="power_bi_LA" width="1024" height="1060" src="https://app.powerbi.com/view?r=eyJrIjoiMzYzOTQ5MjAtZTgxMy00ZGMwLTg4MWItYjUwNjE4NzVhZTg0IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>"""
    st.markdown(powerbi_embed_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()