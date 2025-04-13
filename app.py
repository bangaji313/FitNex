import streamlit as st
from rules import rekomendasi_latihan, rekomendasi_diet
from fuzzy_module import fuzzy_rekomendasi_latihan
from ml_model import prediksi_rekomendasi

# Judul halaman
st.set_page_config(page_title="Sistem Pakar Fitness", layout="centered")
st.title("💪 Sistem Pakar Rekomendasi Latihan & Diet")

st.markdown("Masukkan data berikut untuk mendapatkan rekomendasi latihan dan pola makan:")

# Form input user
with st.form("user_input_form"):
    usia = st.slider("Usia", 15, 60, 25)
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=100, max_value=250, value=170)
    berat = st.number_input("Berat Badan (kg)", min_value=30, max_value=200, value=65)
    tujuan = st.selectbox("Tujuan", ["Menambah Massa Otot", "Menurunkan Berat Badan", "Menjaga Kebugaran"])
    kebugaran = st.selectbox("Tingkat Kebugaran", ["Pemula", "Menengah", "Lanjutan"])
    riwayat_kesehatan = st.checkbox("Memiliki Riwayat Kesehatan?")
    pengguna_baru = st.checkbox("Apakah kamu baru memulai program latihan?")
    submitted = st.form_submit_button("Dapatkan Rekomendasi")

# Saat form dikirim
if submitted:
    st.write("🔍 Sedang memproses data...")

    # Rule-based system
    latihan = rekomendasi_latihan(kebugaran, usia, riwayat_kesehatan, pengguna_baru)
    diet = rekomendasi_diet(tujuan)

    # Hasil rule-based
    st.subheader("🏋️ Rekomendasi Latihan")
    st.success(latihan)

    st.subheader("🍽️ Rekomendasi Diet")
    st.success(diet)

    # Fuzzy Logic
    intensitas_fuzzy = fuzzy_rekomendasi_latihan(usia, kebugaran)

    st.subheader("🔥 Intensitas Latihan (Fuzzy Logic)")
    st.info(intensitas_fuzzy)
    st.caption("✅ Rekomendasi ini dihasilkan menggunakan sistem logika fuzzy berdasarkan usia dan tingkat kebugaran kamu.")

    # Prediksi dari ML
    prediksi_ml = prediksi_rekomendasi(usia, tinggi, berat, kebugaran, tujuan)

    # Mapping angka ke label
    label_mapping = {
        0: "Latihan Ringan (Beginner)",
        1: "Latihan Menengah (Intermediate)",
        2: "Latihan Intens (Advanced)"
    }   
    label_prediksi = label_mapping.get(prediksi_ml, "Tidak diketahui")

    st.subheader("🤖 Prediksi dari Model Machine Learning")
    st.info(f"Hasil Prediksi: {label_prediksi}")
