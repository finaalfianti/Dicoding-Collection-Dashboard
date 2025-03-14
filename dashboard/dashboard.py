import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv("../data/day.csv")
hour_df = pd.read_csv("../data/hour.csv")

# Convert dteday to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'], errors='coerce')
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'], errors='coerce')

# Menentukan rentang waktu berdasarkan data
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

# Sidebar
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data berdasarkan rentang waktu
day_df = day_df[(day_df['dteday'] >= str(start_date)) & (day_df['dteday'] <= str(end_date))]
hour_df = hour_df[(hour_df['dteday'] >= str(start_date)) & (hour_df['dteday'] <= str(end_date))]

# Streamlit UI
st.title("Bike Sharing Data Visualization")

# 1. Grafik: Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='weathersit', y='cnt', hue='weathersit', data=day_df, palette='coolwarm', ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda (Data Harian)")
st.pyplot(fig)

# 2. Grafik: Pola Penyewaan Sepeda per Jam Berdasarkan Kondisi Cuaca
st.subheader("Pola Penyewaan Sepeda per Jam Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', hue='weathersit', data=hour_df, palette='coolwarm', ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Pola Penyewaan Sepeda per Jam Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

# 3. Grafik: Perbedaan Penyewaan Sepeda di Hari Kerja vs Akhir Pekan
st.subheader("Perbedaan Penyewaan Sepeda di Hari Kerja vs Akhir Pekan")
hour_df['day_type'] = hour_df['weekday'].apply(lambda x: 'Weekend' if x in [0, 6] else 'Weekday')
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="day_type", y="cnt", data=hour_df, palette=["red", "blue"], ax=ax)
ax.set_xlabel("Tipe Hari")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Perbedaan Penyewaan Sepeda di Hari Kerja vs Akhir Pekan")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12,6))
sns.lineplot(data=hour_df, x="hr", y="cnt", hue="day_type", palette=["red", "blue"], ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Pola Penyewaan Sepeda per Jam (Hari Kerja vs Akhir Pekan)")
st.pyplot(fig)
