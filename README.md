# BIKE SHARING DATA ANALYSIS


## Project Overview
This project analyzes and visualizes bicycle rental data from the Capital Bikeshare system, Washington D.C., United States, which is publicly available at http://capitalbikeshare.com/system-data.

The Bike Sharing Dataset contains hourly and daily bike rental data from the Capital bike share system between 2011 and 2012, along with weather and seasonal information.

This dataset includes two files: hour.csv (hourly aggregated bike rental data) with 17,379 records, and day.csv (daily aggregated bike rental data) with 731 records. Both files contain columns such as date, season, year, month, hour (in hour.csv), holiday, working day, weather situation, temperature, humidity, wind speed, and the number of casual, registered, and total bike rentals.

This dataset can be used for various tasks, including predicting the number of bike rentals based on environmental and seasonal settings, and detecting anomalies or events by monitoring bike rental data. For example, the number of bikes rented can be associated with events in the city, such as Hurricane Sandy.


## Setup Environment - Pipenv
```
mkdir Bike-Sharing-DA
cd Bike-Sharing-DA
pipenv install
pipenv shell
pip install -r requirements.txt
```
## Install Library
```
numpy==2.2.0
pandas==2.2.3
matplotlib.pyplot==3.10.0
seaborn==0.13.2
folium==0.19.4
streamlit==1.41.1
scikit-learn==1.6.1
tensorflow==2.18.0
babel.numbers==2.16.0
```

## Features
1.  Data Cleaning
    - There are no missing values or duplicates in either the day_df or hour_df tables; both are complete.

2.  Exploratory Data Analysis (EDA)
    - Analyzing the correlations between variables within the bicycle dataset.
    - Exploring bike-sharing usage patterns through data analysis across factors including seasons, time of day, months, years, weekdays, working day status, and weather conditions.

3. Interactive Dashboard
    - Built by Streamlit to visualize bicycle rental trends.
    - Correlation between temperature and bicycle rentals.


## Run steamlit app
```
streamlit run "C:\Dicoding\Bike-Sharing-DA\dashboard\adp-submission.py"
```