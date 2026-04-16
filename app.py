import streamlit as st

st.title("🌦️ Sistem Cerdas Prediksi Cuaca")

st.write("Masukkan kondisi lingkungan untuk memprediksi cuaca")

# Form input
with st.form("form_cuaca"):
    suhu = st.number_input("Suhu (°C)", min_value=0.0, max_value=50.0)
    kelembapan = st.slider("Kelembapan (%)", 0, 100)
    angin = st.selectbox("Kondisi Angin", ["Tenang", "Sedang", "Kencang"])
    awan = st.slider("Tingkat Awan (%)", 0, 100)

    submit = st.form_submit_button("Prediksi")

# Logika sistem cerdas (rule-based)
if submit:
    if suhu > 30 and kelembapan < 60 and awan < 40:
        cuaca = "Cerah ☀️"
    elif kelembapan > 80 and awan > 70:
        cuaca = "Hujan 🌧️"
    elif awan > 50:
        cuaca = "Berawan ☁️"
    elif angin == "Kencang":
        cuaca = "Badai 🌪️"
    else:
        cuaca = "Cuaca Tidak Menentu 🌥️"

    st.subheader("Hasil Prediksi:")
    st.success(cuaca)

    # Saran otomatis (cerdas)
    if cuaca == "Cerah ☀️":
        st.info("Gunakan sunscreen dan tetap terhidrasi")
    elif cuaca == "Hujan 🌧️":
        st.info("Bawa payung atau jas hujan")
    elif cuaca == "Badai 🌪️":
        st.warning("Sebaiknya tetap di dalam rumah!")
    else:
        st.info("Tetap waspada dengan perubahan cuaca")