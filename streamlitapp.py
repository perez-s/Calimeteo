import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Estación meteorologica - Univalle",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

calimeteo = pd.read_csv('cali_meteo.csv', low_memory=False)
calimeteo = calimeteo.dropna()
calimeteo['Time'] = pd.to_datetime(calimeteo['Time'], format='%H:%M')


calimeteo = calimeteo[(calimeteo['Time'].dt.time >= pd.Timestamp('11:00:00').time()) & (calimeteo["Time"].dt.time <= pd.Timestamp('17:00:00').time())]
print(calimeteo)
calimeteo1 = calimeteo[['Time','TempOut',]]
calimeteo['Temp_prom'] = calimeteo1.groupby(['Time']).transform('mean')
calimeteo['Temp_max'] = calimeteo1.groupby(['Time']).transform('max')
calimeteo = calimeteo[['Time','Temp_prom', 'Temp_max']]
calimeteo['Time'] = calimeteo['Time'].dt.strftime('%H:%M')
calimeteo = calimeteo.groupby(['Time']).mean()
#calimeteo = calimeteo.groupby(['Time'])
#calimeteo = calimeteo.groupby(['Time'])
#calimeteo = calimeteo.dropna()

print(calimeteo)


#st.dataframe(calimeteo)

st.title("Estación meteorológica")
st.subheader("Universidad del Valle")

Contenedor1 = st.container(border=True)


Contenedor1.subheader("Temperatura vs Hora", divider="red")
Contenedor1.markdown('Temperatura máxima y promedio entre las 11:00 y las 17:00 horas desde 09/03/2020 hasta 29/05/2023 en la estación meteorológica de la Universidad del Valle')
Contenedor1.line_chart(calimeteo, y=["Temp_prom","Temp_max"], x_label="Hora", y_label="Temperatura [°C]", color=["#FF4B4B","#FFFFFF"])


#calimeteo11to17.info()




#Contenedor1.subheader("Temperatura vs Hora", divider="red")
#Contenedor1.line_chart(calimeteo, x="Hora",y=["Temp_prom","Temp_max"], x_label="Hora", y_label="Temperatura [°C]", color=["#FF4B4B","#B5B6B8"])
