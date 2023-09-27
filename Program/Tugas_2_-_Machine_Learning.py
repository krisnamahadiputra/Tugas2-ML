import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tugas 2 - Machine Learning", page_icon="💡")
st.title("Tugas 2 - Machine Learning")
st.write("Oleh")

identitas = {
    'Nama': 'Putu Gede Krisna Mahadiputra',
    'NIM': '2005551035'
}

df_identitas = pd.DataFrame({"":identitas})
df_identitas = df_identitas.T
st.dataframe(df_identitas, width=800)
