
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Kualitas Udara Beijing",
    page_icon="🌫️",
    layout="wide",
)

sns.set_theme(style="whitegrid")

POLLUTANTS = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
MONTH_LABELS = [
    "Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
    "Jul", "Agu", "Sep", "Okt", "Nov", "Des"
]


# Memuat dataset
@st.cache_data
def load_data():
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "main_data.csv"
    )
    return pd.read_csv(file_path)


def show_fig(fig):
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "File main_data.csv tidak ditemukan. "
        "Letakkan di folder yang sama dengan file ini."
    )
    st.stop()


# Sidebar
st.sidebar.header("Filter Data")

all_stations = sorted(df["station"].unique())

selected = st.sidebar.multiselect(
    "Pilih Stasiun",
    options=all_stations,
    default=all_stations,
)

year_min, year_max = int(df["year"].min()), int(df["year"].max())

if year_min < year_max:
    year_range = st.sidebar.slider(
        "Rentang Tahun",
        year_min,
        year_max,
        (year_min, year_max)
    )
else:
    year_range = (year_min, year_max)

month_range = st.sidebar.select_slider(
    "Rentang Bulan",
    options=list(range(1, 13)),
    value=(1, 12),
    format_func=lambda m: MONTH_LABELS[m - 1],
)

pollutant = st.sidebar.selectbox("Pilih Polutan", POLLUTANTS)

filtered_df = df[
    df["station"].isin(selected)
    & df["year"].between(*year_range)
    & df["month"].between(*month_range)
]


# Judul
st.title("Dashboard Analisis Kualitas Udara Beijing")

st.write(
    "Hasil analisis kualitas udara di stasiun pemantauan Beijing "
    "selama periode 2013–2017."
)


# Pemeriksaan filter
if not selected:
    st.info("Pilih minimal satu stasiun di sidebar untuk menampilkan grafik.")
    st.stop()

if filtered_df.empty:
    st.warning("Tidak ada data untuk kombinasi filter ini.")
    st.stop()


# Ringkasan data
col1, col2, col3, col4 = st.columns(4)

col1.metric("Jumlah Data", f"{len(filtered_df):,}")
col2.metric("Jumlah Stasiun", filtered_df["station"].nunique())
col3.metric(
    "Periode",
    f"{filtered_df['year'].min()}–{filtered_df['year'].max()}"
)
col4.metric(
    f"Rata-rata {pollutant}",
    f"{filtered_df[pollutant].mean():.1f}"
)

st.divider()


# 1. Rata-rata antarstasiun
st.subheader("1. Rata-rata Konsentrasi Polutan Antarstasiun")

station_avg = (
    filtered_df.groupby("station")[pollutant]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(12, 5))

sns.barplot(
    x=station_avg.index,
    y=station_avg.values,
    color="#4C78A8",
    ax=ax
)

ax.bar_label(
    ax.containers[0],
    fmt="%.1f",
    padding=2,
    fontsize=9
)

ax.set_xlabel("Stasiun")
ax.set_ylabel("Konsentrasi (µg/m³)")
ax.set_title(f"Rata-rata {pollutant} per Stasiun")

plt.setp(
    ax.get_xticklabels(),
    rotation=45,
    ha="right"
)

show_fig(fig)

st.divider()


# 2. Distribusi
st.subheader("2. Distribusi Konsentrasi Polutan")

fig, ax = plt.subplots(figsize=(10, 5))

sns.histplot(
    data=filtered_df,
    x=pollutant,
    bins=50,
    kde=True,
    ax=ax
)

ax.set_title(f"Distribusi Konsentrasi {pollutant}")
ax.set_xlabel("Konsentrasi (µg/m³)")
ax.set_ylabel("Frekuensi")

show_fig(fig)

st.divider()


# 3. Perubahan berdasarkan bulan
st.subheader("3. Perubahan Konsentrasi Polutan Berdasarkan Bulan")

monthly_avg = filtered_df.groupby("month")[pollutant].mean()

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    monthly_avg.index,
    monthly_avg.values,
    marker="o"
)

ax.set_title(f"Rata-rata {pollutant} Berdasarkan Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Konsentrasi (µg/m³)")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(MONTH_LABELS)
ax.set_ylim(bottom=0)

show_fig(fig)

st.divider()


# 4. Korelasi
st.subheader("4. Korelasi Polutan dan Kondisi Meteorologi")

correlation_cols = POLLUTANTS + [
    "TEMP", "PRES", "DEWP", "RAIN", "WSPM"
]

correlation = filtered_df[correlation_cols].corr()

fig, ax = plt.subplots(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1,
    ax=ax,
)

ax.set_title("Heatmap Korelasi")

show_fig(fig)

st.divider()


# 5. Analisis Lanjutan PM2.5
st.subheader(
    "5. Analisis Lanjutan: Kondisi Meteorologi terhadap PM2.5"
)

st.write(
    "Analisis ini mengamati hubungan antara kecepatan angin "
    "dan suhu udara dengan konsentrasi PM2.5."
)


# A. PM2.5 berdasarkan kategori kecepatan angin
st.markdown("#### A. Rata-rata PM2.5 Berdasarkan Kecepatan Angin")

wind_df = filtered_df.copy()

wind_df["Wind_Category"] = pd.cut(
    wind_df["WSPM"],
    bins=[-0.01, 1, 2, 3, float("inf")],
    labels=["Rendah", "Sedang", "Tinggi", "Sangat Tinggi"]
)

pm25_by_wind = (
    wind_df.groupby("Wind_Category", observed=False)["PM2.5"]
    .mean()
    .dropna()
)

fig, ax = plt.subplots(figsize=(9, 5))

sns.barplot(
    x=pm25_by_wind.index,
    y=pm25_by_wind.values,
    color="#4C78A8",
    ax=ax
)

ax.set_xlabel("Kategori Kecepatan Angin")
ax.set_ylabel("Rata-rata PM2.5")
ax.set_title("Rata-rata PM2.5 Berdasarkan Kecepatan Angin")

show_fig(fig)


# B. Suhu udara terhadap PM2.5
st.markdown("#### B. Hubungan Suhu Udara dengan PM2.5")

fig, ax = plt.subplots(figsize=(9, 5))

sns.scatterplot(
    data=filtered_df.sample(
        n=min(5000, len(filtered_df)),
        random_state=42
    ),
    x="TEMP",
    y="PM2.5",
    alpha=0.4,
    ax=ax
)

ax.set_xlabel("Suhu Udara (°C)")
ax.set_ylabel("Konsentrasi PM2.5 (µg/m³)")
ax.set_title("Hubungan Suhu Udara dengan PM2.5")

show_fig(fig)


# Sumber dataset
st.divider()

st.caption(
    "Sumber: Beijing Multi-Site Air-Quality Dataset | "
    "Periode Maret 2013 – Februari 2017"
)
