import os
from datetime import datetime

def read_firebase(device_id):
    """
    Placeholder function to simulate reading data from Firebase.
    In a real application, this would involve interacting with 
Firebase's API.
    For demonstration purposes, it returns None or an outdated
dictionary.
    """
    return None  # Simulate no sensor reading

async def get_aqi_input(device_id: str, lat: float, lon: float) -> 
dict:
    """
    Fetches air quality index data for a given device ID. If the data       
is not available or is older than
    5 minutes, it falls back to fetching data using the get_fused_aqi       
function and adds a 'fallback' field.
    The result will include a 'source' field indicating the source of       
the data.

    Parameters:
    device_id (str): The ID of the sensor device.
    lat (float): Latitude coordinate of the location.
    lon (float): Longitude coordinate of the location.

    Returns:
    dict: A dictionary containing air quality index, PM2.5 estimate,        
wind speed,
          temperature, and source information.
    """
    # Attempt to fetch data from Firebase
    firebase_data = read_firebase(device_id)
    
    if not firebase_data or (firebase_data.get('timestamp') and
datetime.now() - datetime.fromisoformat(firebase_data['timestamp']) >       
timedelta(minutes=5)):
        # Data is either missing or older than 5 minutes, fall back to      
fused AQI
        aqi_data = await get_fused_aqi(lat, lon)
        aqi_data.update({'fallback': True})
    else:
        # Use the data directly from Firebase
        aqi_data = firebase_data

    # Set the source of the data
    aqi_data['source'] = "firebase" if 'timestamp' in firebase_data
else "api_fusion"

    return aqi_data

# Example usage
device_id = "sensor123"
lat = 40.7128
lon = -74.0060
aqi_result = get_aqi_input(device_id, lat, lon)
print(aqi_result)