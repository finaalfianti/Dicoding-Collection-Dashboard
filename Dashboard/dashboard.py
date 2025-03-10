import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
st.title("Visualisasi dan Analisis Penyewaan Sepeda")
df_day = pd.read_csv("D:\TUGAS KULIAH\DICODING\Submission\Data\day.csv")
df_hour = pd.read_csv("D:\TUGAS KULIAH\DICODING\Submission\Data\hour.csv")

st.header("Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='weathersit', y='cnt', hue='weathersit', data=df_day, palette='coolwarm', legend=False, ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda (Data Harian)")
st.pyplot(fig)
st.write("\n**Insight:** Cuaca yang lebih cerah cenderung memiliki jumlah penyewaan lebih tinggi dibandingkan kondisi berawan atau hujan.")

st.header("Pola Penyewaan Sepeda per Jam Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', hue='weathersit', data=df_hour, palette='coolwarm', ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Pola Penyewaan Sepeda per Jam Berdasarkan Kondisi Cuaca")
st.pyplot(fig)
st.write("\n**Insight:** Pada jam sibuk (pagi & sore), meskipun cuaca buruk, tetap ada penyewaan, tetapi jumlahnya lebih rendah.")

st.header("Perbedaan Penyewaan Sepeda di Hari Kerja dan Akhir Pekan")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="workingday", y="cnt", data=df_day, palette=["red", "blue"], ax=ax)
ax.set_xticklabels(["Akhir Pekan", "Hari Kerja"])
ax.set_xlabel("Tipe Hari")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Perbedaan Penyewaan Sepeda di Hari Kerja vs Akhir Pekan")
st.pyplot(fig)
st.write("\n**Insight:** Hari kerja memiliki jumlah penyewaan yang lebih tinggi karena aktivitas ke kantor/sekolah.")

st.header("Pola Penyewaan Sepeda per Jam (Hari Kerja vs Akhir Pekan)")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=df_hour, x="hr", y="cnt", hue="workingday", palette=["red", "blue"], ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Pola Penyewaan Sepeda per Jam (Hari Kerja vs Akhir Pekan)")
st.pyplot(fig)
st.write("\n**Insight:** Hari kerja memiliki dua puncak (jam 8 pagi & jam 5-6 sore), sedangkan akhir pekan lebih rata.")
