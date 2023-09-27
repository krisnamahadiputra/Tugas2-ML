import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pengurutan Bilangan Secara Ascending & Descending", page_icon="🔢")
st.title('Pengurutan Bilangan Secara Ascending & Descending')

def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Tampilan
with st.form(key='input bilangan'):
    #input panjang array (jumlah bilangan yang akan diurutkan)
    jumlah_max = st.number_input("Jumlah Bilangan", max_value=100)

    bilangan_input = st.text_input("Masukkan Bilangan (gunakan koma sebagai pemisah)", "") #input bilangan
    bilangan_array = [int(bil) for bil in bilangan_input.split(',') if bil.strip()] #konversi menjadi bilangan & memisahkan koma
    bilangan_array = bilangan_array[:jumlah_max] #limitasi bilangan sesuai panjang array
    submitted = st.form_submit_button("Urutkan")

if submitted:
    st.header("Bilangan Sebelum diurutkan")
    df_sebelum = pd.DataFrame({"Bilangan Sebelum Diurutkan": bilangan_array.copy()})
    df_sebelum = pd.DataFrame({"Daftar Bilangan": bilangan_array})
    df_sebelum_trans = df_sebelum.T
    st.dataframe(df_sebelum_trans, width=800)

    #sortir ascending
    bubble_sort_asc(bilangan_array)
    
    #sortir descending
    bilangan_desc = bilangan_array.copy()
    bubble_sort_desc(bilangan_desc)

    #hasil ascending
    st.header("Bilangan Setelah Diurutkan")
    df_asc = pd.DataFrame({"Ascending": bilangan_array})
    df_asc_trans = df_asc.T
    st.dataframe(df_asc_trans, width=800)
    
    #hasil descending
    df_desc = pd.DataFrame({"Descending": bilangan_desc})
    df_desc_trans = df_desc.T
    st.dataframe(df_desc_trans, width=800)


