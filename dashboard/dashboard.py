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

orders_df = pd.read_csv("dashboard/main-data.csv")


st.title("Analisis Penggunaan Sepeda")

# Pilih dataset

day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

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
  day_df = pd.read_csv('data/day.csv')
  hour_df = pd.read_csv('data/hour.csv')
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

# Judul halaman
st.title('Visualisasi Distribusi Penyewa per Musim')
  
day_df['season'] = day_df['season'].replace({
    1: 'Musim Semi',
    2: 'Musim Panas',
    3: 'Musim Gugur',
    4: 'Musim Dingin'
})

# Hitung total penyewaan per musim
seasonal_rentals = day_df.groupby('season')['cnt'].sum().reset_index()

# Buat bar chart menggunakan matplotlib
plt.figure(figsize=(8, 6))
sns.barplot(x='season', y='cnt', data=seasonal_rentals)
plt.title('Total Penyewaan Sepeda per Musim')
plt.xlabel('Musim')
plt.ylabel('Total Penyewaan')

# Tampilkan plot di Streamlit
st.pyplot(plt)


# Judul halaman
st.title('Visualisasi Hubungan Suhu dan Jumlah Penyewa')
    
import folium

plt.figure(figsize=(8, 6)) # Sesuaikan ukuran gambar
sns.scatterplot(x='temp', y='cnt', data=day_df)
plt.title('Hubungan Suhu dan Jumlah Penyewa')
plt.xlabel('Suhu (temp)')
plt.ylabel('Jumlah Penyewa (cnt)')

# Tampilkan plot di Streamlit
st.pyplot(plt)