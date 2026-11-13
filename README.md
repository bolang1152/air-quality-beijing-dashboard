# Analisis Kualitas Udara di Beijing

## Deskripsi Proyek

Proyek ini merupakan analisis data kualitas udara di Beijing menggunakan **Beijing Multi-Site Air-Quality Dataset**. Dataset berisi catatan pengukuran kualitas udara dari 12 stasiun pemantauan selama periode Maret 2013 hingga Februari 2017.

Analisis dilakukan untuk memahami kondisi kualitas udara berdasarkan konsentrasi berbagai polutan, seperti PM2.5, PM10, SO2, NO2, CO, dan O3. Selain itu, dilakukan pengamatan terhadap beberapa faktor meteorologi untuk melihat keterkaitannya dengan konsentrasi polutan.

Proyek ini mencakup tahapan pengumpulan data, penilaian data (*assessing*), pembersihan data (*cleaning*), eksplorasi data (*exploratory data analysis*), visualisasi, serta penyusunan kesimpulan dan rekomendasi. Hasil analisis juga disajikan melalui dashboard interaktif menggunakan Streamlit.

## Fitur Dashboard

Dashboard dikembangkan menggunakan Streamlit untuk memudahkan pengguna dalam mengeksplorasi data kualitas udara. Beberapa fitur yang tersedia meliputi:

- **Filter Stasiun:** Memilih satu atau beberapa stasiun pemantauan untuk melihat data berdasarkan lokasi.
- **Filter Waktu:** Memilih rentang tahun dan bulan untuk membatasi data yang dianalisis.
- **Pemilihan Polutan:** Memilih jenis polutan yang ingin diamati.
- **Ringkasan Data:** Menampilkan jumlah data, jumlah stasiun, rentang tahun pengamatan, serta rata-rata konsentrasi polutan yang dipilih.
- **Perbandingan Antarstasiun:** Menampilkan rata-rata konsentrasi polutan pada masing-masing stasiun.
- **Distribusi Polutan:** Mengamati persebaran konsentrasi polutan melalui histogram.
- **Pola Bulanan:** Menampilkan perubahan rata-rata konsentrasi polutan berdasarkan bulan.
- **Analisis Korelasi:** Mengamati hubungan antarvariabel menggunakan heatmap korelasi.
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
4. Buka file `Proyek_Analisis_Data.ipynb`.
5. Pilih kernel Python yang sudah memiliki library yang dibutuhkan.
6. Pastikan folder `data/` berada pada direktori yang sama dengan notebook agar file CSV dapat dibaca.
7. Jalankan seluruh sel notebook secara berurutan dari awal hingga akhir.
8. Pastikan seluruh proses analisis dan visualisasi berhasil dijalankan tanpa error.

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

Proyek ini memberikan gambaran mengenai kondisi kualitas udara di Beijing berdasarkan data dari 12 stasiun pemantauan selama periode 2013–2017. Melalui proses pengolahan dan eksplorasi data, berbagai pola konsentrasi polutan dapat diamati berdasarkan lokasi, waktu, serta faktor meteorologi.

Hasil analisis kemudian disajikan dalam bentuk dashboard interaktif agar informasi lebih mudah dipahami dan dieksplorasi. Dengan demikian, proyek ini tidak hanya menerapkan proses analisis data menggunakan Python, tetapi juga menyajikan hasilnya melalui visualisasi yang dapat membantu pengguna memahami karakteristik kualitas udara di Beijing.