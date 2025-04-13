import joblib
import numpy as np
import pandas as pd

# Load model dan fitur
model = joblib.load("random_forest_model.pkl")
kolom_fitur = joblib.load("fitur_model.pkl")

def prediksi_rekomendasi(usia, tinggi, berat, kebugaran, tujuan):
    # Mapping kategori ke numerik → one-hot encoded secara manual
    input_dict = {
        'Usia': usia,
        'Tinggi': tinggi,
        'Berat': berat,
        'Tingkat_Kebugaran_Pemula': 0,
        'Tingkat_Kebugaran_Menengah': 0,
        'Tingkat_Kebugaran_Lanjutan': 0,
        'Tujuan_Menambah Massa Otot': 0,
        'Tujuan_Menurunkan Berat Badan': 0,
        'Tujuan_Menjaga Kebugaran': 0
    }

    # Set nilai kategori yang sesuai
    input_dict[f'Tingkat_Kebugaran_{kebugaran}'] = 1
    input_dict[f'Tujuan_{tujuan}'] = 1

    # Buat dataframe dan isi fitur yang tidak ada jadi 0
    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=kolom_fitur, fill_value=0)

    # Prediksi
    prediksi = model.predict(input_df)

    return prediksi[0]
