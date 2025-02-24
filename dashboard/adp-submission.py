import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style="dark")

def calculate_season_frequency(df):
    return df['season'].value_counts()

def calculate_atemp_stats(df):
    return df['atemp'].describe()

def calculate_correlation(df):
    return df[['atemp', 'cnt']].corr()

def create_contingency_table(df, col1, col2):
    return pd.crosstab(df[col1], df[col2])

all_df = pd.read_csv("all_data.csv")

st.title("Analisis Penggunaan Sepeda")

# Pilih dataset

day_df = pd.read_csv("C:\My Documents\Indira\Dicoding\Submission\day.csv")
hour_df = pd.read_csv("C:\My Documents\Indira\Dicoding\Submission\hour.csv")

dataset = st.selectbox("Pilih dataset", ['day', 'hour'])

if dataset == 'day':
    df = day_df
else:
    df = hour_df

# Pilih analisis
analysis = st.selectbox("Pilih analisis", ['Frekuensi Musim', 'Statistik Suhu', 'Korelasi', 'Tabel Kontingensi'])

if analysis == 'Frekuensi Musim':
    st.subheader("Frekuensi Musim")
    st.write(calculate_season_frequency(df))
elif analysis == 'Statistik Suhu':
    st.subheader("Statistik Suhu yang Dirasakan")
    st.write(calculate_atemp_stats(df))
elif analysis == 'Korelasi':
    st.subheader("Korelasi antara Suhu dan Jumlah Pengguna")
    st.write(calculate_correlation(df))
elif analysis == 'Tabel Kontingensi':
    st.subheader("Tabel Kontingensi")
    col1 = st.selectbox("Pilih kolom pertama", df.columns)
    col2 = st.selectbox("Pilih kolom kedua", df.columns)
    st.write(create_contingency_table(df, col1, col2))

def load_data():
  """Load the datasets."""
  day_df = pd.read_csv('C:\My Documents\Indira\Dicoding\Submission\day.csv')
  hour_df = pd.read_csv('C:\My Documents\Indira\Dicoding\Submission\hour.csv')
  return day_df, hour_df

def group_and_aggregate(df, group_cols, agg_col, agg_func):
  """Group the DataFrame and perform aggregation."""
  grouped_df = df.groupby(group_cols)[agg_col].agg(agg_func)
  return grouped_df

def display_results(results):
  """Display the results in Streamlit."""
  st.table(results)

def main():
  st.title("Bike Sharing Data Analysis")

  day_df, hour_df = load_data()

  # Select the analysis to perform
  analysis_options = [
      "Average 'cnt' by season (day_df)",
      "Total 'cnt' by hour (hour_df)",
      "Average 'cnt' by month and year (day_df)",
      "Median 'cnt' by weekday and workingday (hour_df)",
      "Standard deviation of 'atemp' by weathersit (hour_df)"
  ]
  selected_analysis = st.selectbox("Select Analysis", analysis_options)

  if selected_analysis == "Average 'cnt' by season (day_df)":
    results = group_and_aggregate(day_df, 'season', 'cnt', 'mean')
  elif selected_analysis == "Total 'cnt' by hour (hour_df)":
    results = group_and_aggregate(hour_df, 'hr', 'cnt', 'sum')
  elif selected_analysis == "Average 'cnt' by month and year (day_df)":
    results = group_and_aggregate(day_df, ['mnth', 'yr'], 'cnt', 'mean')
  elif selected_analysis == "Median 'cnt' by weekday and workingday (hour_df)":
    results = group_and_aggregate(hour_df, ['weekday', 'workingday'], 'cnt', 'median')
  elif selected_analysis == "Standard deviation of 'atemp' by weathersit (hour_df)":
    results = group_and_aggregate(hour_df, 'weathersit', 'atemp', 'std')

  display_results(results)

if __name__ == "__main__":
  main()
  
## Visualisasi Data
  
# Simulasi data (ganti dengan data Anda)
data = {'season': [1, 2, 1, 3, 2, 4, 1, 3, 2, 4, 1, 2, 3, 4, 1, 2, 3, 4]}
df = pd.DataFrame(data)

# Fungsi untuk membuat plot
def plot_penyewa_per_musim(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='season', data=df, ax=ax)
    plt.title('Distribusi Penyewa per Musim')
    st.pyplot(fig)

# Judul halaman
st.title('Visualisasi Distribusi Penyewa per Musim')

# Tombol untuk menampilkan plot
if st.button('Tampilkan Plot'):
    plot_penyewa_per_musim(df)
    
    
# Simulasi data (ganti dengan data Anda)
data = {'temp': [0.1, 0.2, 0.3, ], 'cnt': [1000, 2000, 3000]}  # Pastikan panjangnya sama

# Buat DataFrame
df = pd.DataFrame(data)

# Tampilkan DataFrame
print(df)

# Periksa tipe data dan tangani nilai yang hilang (jika perlu)
print(df.info())  # Melihat informasi tentang DataFrame
df.dropna(inplace=True)  # Menghapus baris dengan nilai hilang

# Fungsi untuk membuat plot
def plot_hubungan_suhu_penyewa(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='temp', y='cnt', data=df, ax=ax)
    plt.title('Hubungan Suhu dan Jumlah Penyewa')
    st.pyplot(fig)

# Judul halaman
st.title('Visualisasi Hubungan Suhu dan Jumlah Penyewa')

# Tombol untuk menampilkan plot
if st.button('Tampilkan Plot', key='show_plot'):
    plot_hubungan_suhu_penyewa(df)
    
    
import folium

df = day_df  # Or df = hour_df if that's the data you want to use

map_center = [37.7749, -122.4194]  # Replace with your desired center coordinates

map = folium.Map(location=map_center, zoom_start=12)

# The columns in day.csv are actually named 'temp' and 'hum' for latitude and longitude, not 'lat' and 'lng'
for index, row in df.iterrows():
    # Replace 'temp' and 'hum' with the actual latitude and longitude column names if different
    folium.Marker([row['temp'], row['hum']]).add_to(map)

map.save('bike_rental_locations.html')