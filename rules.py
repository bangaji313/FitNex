def rekomendasi_latihan(kebugaran, usia, riwayat_kesehatan, pengguna_baru):
    if riwayat_kesehatan:
        return "Konsultasikan terlebih dahulu dengan dokter atau ahli medis sebelum memulai latihan."

    if pengguna_baru:
        return "Mulai dengan latihan ringan seperti jalan cepat, stretching, dan latihan bodyweight selama 15-30 menit setiap hari."

    if kebugaran == "Pemula":
        return "Lakukan latihan dasar seperti push-up, plank, squat, dan jogging ringan selama 3-4 kali seminggu."

    elif kebugaran == "Menengah":
        return "Tambahkan latihan kekuatan seperti angkat beban ringan dan interval training selama 4-5 kali seminggu."

    elif kebugaran == "Lanjutan":
        if usia > 40:
            return "Fokus pada latihan beban moderat, latihan fungsional, dan pemulihan aktif 5-6 kali seminggu."
        else:
            return "Latihan intens seperti HIIT, beban berat, dan kombinasi cardio dilakukan 5-6 kali seminggu."

    return "Data tidak cukup untuk memberikan rekomendasi latihan."


def rekomendasi_diet(tujuan):
    if tujuan == "Menambah Massa Otot":
        return "Konsumsi tinggi protein (ayam, telur, whey), karbohidrat kompleks (beras merah, oatmeal), dan sayuran. Perhatikan asupan kalori harian."

    elif tujuan == "Menurunkan Berat Badan":
        return "Pilih makanan rendah kalori, tinggi serat, dan protein tanpa lemak. Kurangi gula dan makanan olahan. Jaga defisit kalori."

    elif tujuan == "Menjaga Kebugaran":
        return "Konsumsi makanan seimbang, termasuk protein, karbohidrat kompleks, lemak sehat, dan sayuran. Fokus pada nutrisi harian."

    return "Data tidak cukup untuk memberikan rekomendasi diet."
