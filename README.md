# Analisis Kualitas Udara di Beijing

## Deskripsi Proyek

Proyek ini merupakan analisis data kualitas udara di Beijing menggunakan **Beijing Multi-Site Air-Quality Dataset**. Dataset berisi catatan pengukuran kualitas udara dari 12 stasiun pemantauan selama periode Maret 2013 hingga Februari 2017.

Analisis difokuskan pada konsentrasi **PM2.5** sebagai indikator utama kualitas udara, dan dirancang untuk menjawab empat pertanyaan bisnis:

1. Stasiun pemantauan mana yang memiliki rata-rata konsentrasi PM2.5 tertinggi dan terendah?
2. Bagaimana perubahan rata-rata konsentrasi PM2.5 setiap bulan selama Maret 2013 hingga Februari 2017, dan bulan apa yang memiliki rata-rata tertinggi?
3. Bagaimana perbandingan rata-rata konsentrasi PM2.5 pada musim semi, musim panas, musim gugur, dan musim dingin?
4. Bagaimana hubungan antara konsentrasi PM2.5 dengan suhu, curah hujan, dan kecepatan angin?

Proyek ini mencakup tahapan pengumpulan data, penilaian data (*assessing*), pembersihan data (*cleaning*), eksplorasi data (*exploratory data analysis*), visualisasi, analisis lanjutan, serta penyusunan kesimpulan dan rekomendasi. Hasil analisis juga disajikan melalui dashboard interaktif menggunakan Streamlit.

## Fitur Dashboard

Dashboard dikembangkan menggunakan Streamlit untuk memudahkan pengguna dalam mengeksplorasi data kualitas udara. Beberapa fitur yang tersedia meliputi:

- **Filter Stasiun:** Memilih satu atau beberapa stasiun pemantauan untuk melihat data berdasarkan lokasi.
- **Filter Waktu:** Memilih rentang tahun dan bulan untuk membatasi data yang dianalisis.
- **Ringkasan Data:** Menampilkan jumlah data, jumlah stasiun, rentang tahun pengamatan, serta rata-rata konsentrasi PM2.5.
- **Perbandingan Antarstasiun (Pertanyaan 1):** Menampilkan rata-rata PM2.5 pada masing-masing stasiun, dengan stasiun tertinggi dan terendah ditandai.
- **Perubahan PM2.5 Setiap Bulan (Pertanyaan 2):** Menampilkan grafik rata-rata PM2.5 setiap bulan dari Maret 2013 hingga Februari 2017, serta rata-rata berdasarkan bulan kalender untuk mengetahui bulan tertinggi.
- **Perbandingan PM2.5 Berdasarkan Musim (Pertanyaan 3):** Membandingkan rata-rata PM2.5 pada musim semi, musim panas, musim gugur, dan musim dingin.
- **Korelasi PM2.5 dengan Meteorologi (Pertanyaan 4):** Menampilkan heatmap dan grafik korelasi PM2.5 dengan suhu, curah hujan, dan kecepatan angin.
- **Analisis Lanjutan PM2.5:** Mengamati rata-rata PM2.5 berdasarkan kategori kecepatan angin serta hubungan suhu udara dengan konsentrasi PM2.5.

## Struktur Direktori

```text
Submission_Fundamental_Analisis_Data_I_Made_Dwika_Rangga_Dinatha/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
│   ├── PRSA_Data_Changping_20130301-20170228.csv
│   ├── PRSA_Data_Dingling_20130301-20170228.csv
│   ├── PRSA_Data_Dongsi_20130301-20170228.csv
│   ├── PRSA_Data_Guanyuan_20130301-20170228.csv
│   ├── PRSA_Data_Gucheng_20130301-20170228.csv
│   ├── PRSA_Data_Huairou_20130301-20170228.csv
│   ├── PRSA_Data_Nongzhanguan_20130301-20170228.csv
│   ├── PRSA_Data_Shunyi_20130301-20170228.csv
│   ├── PRSA_Data_Tiantan_20130301-20170228.csv
│   ├── PRSA_Data_Wanliu_20130301-20170228.csv
│   └── PRSA_Data_Wanshouxigong_20130301-20170228.csv
├── notebook.ipynb
├── requirements.txt
└── README.md
```

**Keterangan:**
- `data/`: Berisi 12 file dataset CSV dari masing-masing stasiun pemantauan.
- `dashboard/`: Berisi file aplikasi Streamlit dan dataset hasil pembersihan yang digunakan untuk dashboard.
- `notebook.ipynb`: Notebook yang berisi seluruh tahapan analisis data.
- `requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek.
- `README.md`: Dokumentasi proyek dan panduan penggunaan.

## Menjalankan Notebook

Notebook digunakan untuk menjalankan seluruh tahapan analisis data, mulai dari pengumpulan data hingga penarikan kesimpulan dan rekomendasi.

Proses pengerjaan dilakukan menggunakan **Visual Studio Code (VS Code)** dengan bantuan ekstensi Python dan Jupyter.

Langkah-langkah menjalankan notebook:

1. Pastikan Python sudah terpasang pada perangkat.
2. Buka folder utama proyek menggunakan VS Code.
3. Pastikan ekstensi **Python** dan **Jupyter** sudah terpasang.
4. Buka file `notebook.ipynb`.
5. Pilih kernel Python yang sudah memiliki library yang dibutuhkan.
6. Pastikan folder `data/` berada pada direktori yang sama dengan notebook agar file CSV dapat dibaca.
7. Jalankan seluruh sel notebook secara berurutan dari awal hingga akhir.
8. Pastikan seluruh proses analisis dan visualisasi berhasil dijalankan tanpa error.
9. Sel terakhir akan memperbarui `dashboard/main_data.csv` (termasuk kolom `season` dan `year_month`) yang digunakan oleh dashboard.

## Instalasi dan Menjalankan Dashboard

Dashboard dapat dijalankan secara lokal melalui terminal VS Code dengan langkah-langkah berikut.

**1. Pastikan Python sudah terpasang**

Periksa instalasi Python melalui terminal:

```bash
python3 --version
```

**2. Buka direktori utama proyek**

Pastikan terminal berada di dalam folder utama proyek.

**3. Instal library yang dibutuhkan**

```bash
python3 -m pip install -r requirements.txt
```

**4. Jalankan aplikasi dashboard**

```bash
python3 -m streamlit run dashboard/dashboard.py
```

**5. Buka dashboard**

Setelah aplikasi berhasil dijalankan, buka alamat lokal yang ditampilkan pada terminal. Secara default, alamat dashboard adalah:

```text
http://localhost:8501
```

## Teknologi yang Digunakan

- **Python:** Bahasa pemrograman utama untuk pengolahan dan analisis data.
- **Pandas:** Digunakan untuk membaca, membersihkan, menggabungkan, dan menganalisis dataset.
- **Matplotlib:** Digunakan untuk membuat visualisasi data.
- **Seaborn:** Digunakan untuk menghasilkan visualisasi statistik yang lebih informatif.
- **Streamlit:** Digunakan untuk membangun dashboard interaktif berbasis web.
- **Jupyter Notebook:** Digunakan sebagai lingkungan untuk menulis dan menjalankan tahapan analisis data.
- **Visual Studio Code:** Editor kode yang digunakan selama proses pengerjaan proyek.

## Kesimpulan

Proyek ini memberikan gambaran mengenai konsentrasi PM2.5 di Beijing berdasarkan data dari 12 stasiun pemantauan selama periode Maret 2013 hingga Februari 2017. Melalui proses pengolahan dan eksplorasi data, pola PM2.5 dapat diamati berdasarkan lokasi (stasiun), waktu (bulan), musim, serta faktor meteorologi (suhu, curah hujan, dan kecepatan angin).

Hasil analisis kemudian disajikan dalam bentuk dashboard interaktif agar informasi lebih mudah dipahami dan dieksplorasi. Dengan demikian, proyek ini tidak hanya menerapkan proses analisis data menggunakan Python, tetapi juga menyajikan hasilnya melalui visualisasi yang dapat membantu pengguna memahami karakteristik kualitas udara di Beijing.