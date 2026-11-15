import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Kualitas Udara Beijing",
    page_icon="",
    layout="wide",
)

sns.set_theme(style="whitegrid")

MONTH_LABELS = [
    "Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
    "Jul", "Agu", "Sep", "Okt", "Nov", "Des"
]
SEASON_ORDER = ["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"]
SEASON_COLORS = ["#2ca02c", "#ff7f0e", "#8c564b", "#1f77b4"]


def get_season(month):
    if month in [3, 4, 5]:
        return "Musim Semi"
    if month in [6, 7, 8]:
        return "Musim Panas"
    if month in [9, 10, 11]:
        return "Musim Gugur"
    return "Musim Dingin"


# Memuat dataset
@st.cache_data
def load_data():
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "main_data.csv"
    )
    data = pd.read_csv(file_path)
    data["season"] = data["month"].apply(get_season)
    data["year_month"] = (
        data["year"].astype(str) + "-" + data["month"].astype(str).str.zfill(2)
    )
    return data


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

filtered_df = df[
    df["station"].isin(selected)
    & df["year"].between(*year_range)
    & df["month"].between(*month_range)
]


# Judul
st.title("Dashboard Analisis Kualitas Udara Beijing")

st.write(
    "Hasil analisis konsentrasi PM2.5 di stasiun pemantauan Beijing "
    "selama periode Maret 2013 – Februari 2017."
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
col4.metric("Rata-rata PM2.5", f"{filtered_df['PM2.5'].mean():.1f} µg/m³")

st.divider()


# 1. Rata-rata PM2.5 antarstasiun
st.subheader("1. Rata-rata Konsentrasi PM2.5 Antarstasiun")

station_avg = (
    filtered_df.groupby("station")["PM2.5"]
    .mean()
    .sort_values(ascending=False)
)

bar_colors = [
    "#d62728" if s == station_avg.idxmax()
    else "#2ca02c" if s == station_avg.idxmin()
    else "#9ecae1"
    for s in station_avg.index
]

fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(
    x=station_avg.index,
    y=station_avg.values,
    hue=station_avg.index,
    palette=bar_colors,
    legend=False,
    ax=ax
)
ax.bar_label(ax.containers[0], fmt="%.1f", padding=2, fontsize=9)
ax.set_xlabel("Stasiun")
ax.set_ylabel("Rata-rata PM2.5 (µg/m³)")
ax.set_title("Rata-rata PM2.5 per Stasiun")
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
show_fig(fig)

st.caption(
    f"Tertinggi: **{station_avg.idxmax()}** ({station_avg.max():.2f} µg/m³) | "
    f"Terendah: **{station_avg.idxmin()}** ({station_avg.min():.2f} µg/m³)"
)

st.divider()


# 2. Perubahan PM2.5 setiap bulan
st.subheader("2. Perubahan Rata-rata PM2.5 Setiap Bulan")

ym_avg = filtered_df.groupby("year_month")["PM2.5"].mean().sort_index()

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(ym_avg.index, ym_avg.values, marker="o", color="#1f77b4")
ax.scatter(
    [ym_avg.idxmax()], [ym_avg.max()],
    color="red", s=120, zorder=5,
    label=f"Tertinggi: {ym_avg.idxmax()} ({ym_avg.max():.2f})"
)
step = max(1, len(ym_avg) // 16)
ax.set_xticks(range(0, len(ym_avg), step))
ax.set_xticklabels(ym_avg.index[::step], rotation=45)
ax.set_ylim(bottom=0)
ax.set_title("Rata-rata PM2.5 Setiap Bulan")
ax.set_xlabel("Tahun-Bulan")
ax.set_ylabel("Rata-rata PM2.5 (µg/m³)")
ax.legend()
show_fig(fig)

month_avg = filtered_df.groupby("month")["PM2.5"].mean()

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(
    [MONTH_LABELS[m - 1] for m in month_avg.index],
    month_avg.values,
    color=["#d62728" if m == month_avg.idxmax() else "#9ecae1"
           for m in month_avg.index]
)
ax.set_title("Rata-rata PM2.5 Berdasarkan Bulan Kalender")
ax.set_xlabel("Bulan")
ax.set_ylabel("Rata-rata PM2.5 (µg/m³)")
show_fig(fig)

st.caption(
    f"Bulan kalender dengan rata-rata tertinggi: "
    f"**{MONTH_LABELS[month_avg.idxmax() - 1]}** ({month_avg.max():.2f} µg/m³)"
)

st.divider()


# 3. PM2.5 berdasarkan musim
st.subheader("3. Perbandingan Rata-rata PM2.5 Berdasarkan Musim")

season_avg = (
    filtered_df.groupby("season")["PM2.5"]
    .mean()
    .reindex(SEASON_ORDER)
    .dropna()
)

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(
    x=season_avg.index,
    y=season_avg.values,
    hue=season_avg.index,
    palette=[SEASON_COLORS[SEASON_ORDER.index(s)] for s in season_avg.index],
    legend=False,
    ax=ax
)
ax.bar_label(ax.containers[0], fmt="%.1f", padding=2, fontsize=10)
ax.set_title("Rata-rata PM2.5 Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata PM2.5 (µg/m³)")
show_fig(fig)

st.caption(
    f"Tertinggi: **{season_avg.idxmax()}** ({season_avg.max():.2f} µg/m³) | "
    f"Terendah: **{season_avg.idxmin()}** ({season_avg.min():.2f} µg/m³)"
)

st.divider()


# 4. Korelasi PM2.5 dengan meteorologi
st.subheader("4. Hubungan PM2.5 dengan Suhu, Curah Hujan, dan Kecepatan Angin")

meteo_cols = ["PM2.5", "TEMP", "RAIN", "WSPM"]
correlation = filtered_df[meteo_cols].corr()
pm25_corr = correlation["PM2.5"].drop("PM2.5")

col_a, col_b = st.columns(2)

with col_a:
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        vmin=-1,
        vmax=1,
        ax=ax,
    )
    ax.set_title("Heatmap Korelasi PM2.5 dan Meteorologi")
    show_fig(fig)

with col_b:
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.barplot(
        x=pm25_corr.index,
        y=pm25_corr.values,
        hue=pm25_corr.index,
        palette="coolwarm",
        legend=False,
        ax=ax
    )
    ax.bar_label(ax.containers[0], fmt="%.2f", padding=2)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("Korelasi PM2.5 terhadap Variabel Meteorologi")
    ax.set_xlabel("Variabel")
    ax.set_ylabel("Koefisien Korelasi")
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

st.divider()


# Sumber dataset
st.caption(
    "Sumber: Beijing Multi-Site Air-Quality Dataset | "
    "Periode Maret 2013 – Februari 2017"
)