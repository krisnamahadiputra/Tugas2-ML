import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Penentuan Kuadran", page_icon="🔍")
st.title("Penentuan Kuadran Berdasarkan Input Nilai x dan y")

def kuadran(x, y):
    if x > 0 and y > 0:
        kuadran = "Kuadran I"
    elif x < 0 and y > 0:
        kuadran = "Kuadran II"
    elif x < 0 and y < 0:
        kuadran = "Kuadran III"
    elif x > 0 and y < 0:
        kuadran = "Kuadran IV"
    elif x == 0 and y != 0:
        kuadran = "Berada pada sumbu Y"
    elif x != 0 and y == 0:
        kuadran = "Berada pada sumbu X"
    else:
        kuadran = "Titik Pusat"
    
    return kuadran

with st.form(key='input x dan y'):
    x = st.number_input("Masukkan nilai x", format="%.1f")
    y = st.number_input("Masukkan nilai y", format="%.1f")
    submitted = st.form_submit_button("Cari")

if submitted:
    kuadran = kuadran(x, y)

    st.subheader("Hasil Deteksi Kuadran")
    st.success(f"Titik (x = {x} dan y = {y}) berada di {kuadran}")

    #grafik kuadran
    plt.figure(figsize=(3, 3))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.scatter(x, y, color='red', marker='o')
    plt.title(f"Kuadran: {kuadran}")
    plt.xlabel("Nilai x")
    plt.ylabel("Nilai y")
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)

    st.pyplot(plt)
