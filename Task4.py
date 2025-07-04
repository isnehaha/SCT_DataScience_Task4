
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Download latest version


df = pd.read_csv(r"C:/Users/asus/Documents/Task4/US_Accidents_March23.csv")
print(df.shape)
print(df.head())

df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()


df['hour'] = pd.to_datetime(df['start_time'], format='mixed').dt.hour

sns.histplot(df['hour'], bins=24, kde=False)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.show()

top_weather = df['weather_condition'].value_counts().head(10)
top_weather.plot(kind='bar')
plt.title("Top 10 Weather Conditions During Accidents")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.show()

road_conditions = ['amenity', 'bump', 'crossing', 'give_way', 'junction', 'no_exit',
                   'railway', 'roundabout', 'station', 'stop', 'traffic_calming', 'traffic_signal']
for col in road_conditions:
    if col in df.columns:
        print(f"{col} - Accidents: {df[col].sum()}")

accident_map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)  # Center on USA

heat_data = df[['start_lat', 'start_lng']].dropna()

if len(heat_data) > 10000:
    heat_data = heat_data.sample(10000, random_state=42)

heat_data = heat_data.values.tolist()


df['state'].value_counts().head(10).plot(kind='bar', title='Top 10 States by Number of Accidents')
plt.ylabel("Accidents")
plt.show()

