import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Menyiapkan  dataframe
all_df = pd.read_csv("all_data.csv")

all_df["dteday"] = pd.to_datetime(all_df["dteday"])

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    st.image("https://logowik.com/content/uploads/images/free-vector-bicycle-with-wheat9165.logowik.com.webp")
    start_date, end_date = st.date_input(
        "Pilih Tanggal",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    day_type = st.radio("Pilih Jenis Hari", ["Semua Hari", "Hari Kerja", "Hari Libur"])

# Filter data berdasarkan tanggal dan jenis hari
filter_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                     (all_df["dteday"] <= str(end_date))]

if day_type == "Hari Kerja":
    filter_df = filter_df[filter_df["workingday_hour"] == 1]
elif day_type == "Hari Libur":
    filter_df = filter_df[filter_df["workingday_hour"] == 0]

st.title("Bike Sharing Dashboard")

# overview
st.subheader("Data Overview")
col1, col2 = st.columns(2)
with col1:
    total_sewa = filter_df["cnt_hour"].sum()
    st.metric("Total Peminjaman Sepeda", total_sewa)
with col2:
    avg_sewa = round(filter_df["cnt_hour"].mean())
    st.metric("Rata-rata Peminjaman per Hari", avg_sewa)

# pertanyaan_1
# Data peminjaman sepeda berdasarkan jam untuk hari kerja dan akhir pekan
st.subheader("Tren Peminjaman Pada Hari Kerja vs Hari Libur")
hari_kerja = filter_df[filter_df["workingday_hour"] == 1].groupby("hr")["cnt_hour"].mean()
hari_libur = filter_df[filter_df["workingday_hour"] == 0].groupby("hr")["cnt_hour"].mean()

# line chart
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hari_kerja.index, hari_kerja, marker='s', label="Hari Kerja", linestyle='-')
ax.plot(hari_libur.index, hari_libur, marker='o', label="Hari Libur", linestyle='--')

# judul dan label
ax.set_title("Rata-rata Peminjaman Sepeda per Jam (Hari Kerja vs Hari Libur)")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_xticks(range(0, 24))
ax.legend()
ax.grid(True)

# Menampilkan grafik
st.pyplot(fig)

st.subheader("Tren Peminjaman Berdasarkan Musim dan Cuaca")
# Data pinjam berdasarkan musim
musim_df = all_df.groupby("season_day")["cnt_day"].mean()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=musim_df.index, y=musim_df.values, hue=musim_df.index, palette="viridis", legend=False)
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")

# Menampilkan grafik
st.pyplot(fig)

# Data pinjam berdasarkan musim
cuaca_df = all_df.groupby("weathersit_day")["cnt_day"].mean()
print("\nJumlah peminjaman sepeda berdasarkan cuaca\n",musim_df)
fig,ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=cuaca_df.index, y=cuaca_df.values, hue=cuaca_df.index, palette="viridis", legend=False)
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca")
ax.set_xlabel("Cuaca")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")

# Menampilkan grafik
st.pyplot(fig)

st.caption("Dashboard Bike Sharing | Proyek Data Analisis")