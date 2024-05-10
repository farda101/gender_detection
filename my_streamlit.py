import streamlit as st
import pandas as pd
from pymongo import MongoClient

def load_data():
    df = pd.read_csv("object-detection.csv")
    client = MongoClient('mongodb://localhost:27017/')
    db = client['object-detection']
    collection = db['gender']
    return df

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Dataframe')
)

if option == 'Home' or option == '':
    st.write("""# Halaman Utama""") 
elif option == 'Dataframe':
    st.write("""## Dataframe""") 

    df = load_data()

    st.write("""## Draw Charts""")  

    men = df[(df['label']=='men')].count()['label']
    women = df[(df['label']=='women')].count()['label']
    label = df['label'].count()
    chart_data = pd.DataFrame(
        df, columns=['label']
    )
    total = men + women
    persentase = women / label * 100
    data = {
        'women': [women],
        'men' : [men],
        'Total Terdeteksi': [total],
        'Persentase deteksi gender': [persentase]
    }
    table = pd.DataFrame(data, index=['Jumlah Data'])
    
    chart_data = df['label'].value_counts()
    
    st.bar_chart(chart_data)
    st.write(table)
