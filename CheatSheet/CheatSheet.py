import pandas as pd
import numpy as np
import streamlit as st

st.title("Programming cheat sheet")
select_program_lang=st.sidebar.selectbox("Seleccione el lenguaje de programación",["Python",'HTML'])

if select_program_lang=="Python":
    st.markdown("## Python",unsafe_allow_html=True)

    select_tema=st.radio("Escoja el tema",["Python syntaxis","Pandas","Plotly","Folium"])

    if select_tema=="Pandas":
        st.markdown("### Pandas",unsafe_allow_html=True)
        pandas_radio=st.selectbox('',["Eliminar columnas","Modificar dataframe","Reemplazar valores","Añadir filas","Agrupar y contar ocurrencias"])
        if pandas_radio=="Eliminar columnas":
            st.markdown("#### Eliminar columnas",unsafe_allow_html=True)
            py_code_1="df.drop(columns={'col1','col2'},inplace=True)"
            st.code(py_code_1,language="python")