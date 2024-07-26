import pandas as pd
from geopy.geocoders import Nominatim

def load_and_geocode(file_path):
    geolocator = Nominatim(user_agent="myGeocoder")
    df = pd.read_csv(file_path)

    def geocode(address):
        try:
            location = geolocator.geocode(address)
            return location.latitude, location.longitude
        except:
            return None, None

    df[['Latitude', 'Longitude']] = df['Address'].apply(lambda x: geocode(x)).apply(pd.Series)
    df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

    return df

def save_geocoded_data(df, save_path):
    df.to_csv(save_path, index=False)
