import httpx

async def get_fused_aqi(lat:
float, lon: float) -> dict:
    """
    Asynchronously fetches air
quality index (AQI), PM2.5 estimate, wind speed,
    and temperature from Open-Meteo API and CPCB AQI API. The data is       
returned in a dictionary
    with keys 'aqi_estimate', 'pm2_5_estimate', 'wind_speed', 
'temperature', and 'source'.

    Parameters:
    lat (float): Latitude of the location.
    lon (float): Longitude of the location.

    Returns:
    dict: A dictionary containing air quality index, PM2.5 estimate,        
wind speed,
          temperature, and source information.
    """
    async with httpx.AsyncClient() as client:
        # Step 1: Fetch weather data from Open-Meteo API
        open_meteo_url = "https://api.open-meteo.com/v1/forecast"
        params_open_meteo = {
            'latitude': lat,
            'longitude': lon,
            'hourly': ['temperature_2m', 'wind_speed_10m'],
            'models': 'reanalysis_arome',
            'timezone': 'auto'
        }
        response_open_meteo = await client.get(open_meteo_url, 
params=params_open_meteo)
        weather_data = response_open_meteo.json()

        # Step 2: Fetch AQI data from CPCB API (Mocking the URL with        
an environment variable)
        cpcb_api_key = os.getenv("CPCB_API_KEY")
        if not cpcb_api_key:
            raise ValueError("CPCB API key is missing. Set it in
environment variables.")

        cpcb_aqi_url =
f"https://api.ccbike.org.cn/v1/aqis?lat={lat}&lon={lon}"
        response_cpcb_aqi = await client.get(cpcb_aqi_url,
headers={"Authorization": f"Bearer {cpcb_api_key}"})
        aqi_data = response_cpcb_aqi.json()

    # Extract relevant data
    aqi_estimate = aqi_data['aqis'][0]['aqi']
    pm2_5_estimate = weather_data['hourly']['temperature_2m'][-1]
    wind_speed = weather_data['hourly']['wind_speed_10m'][-1]
    temperature = weather_data['hourly']['temperature_2m'][-1]

    # Return the result as a dictionary
    return {
        'aqi_estimate': aqi_estimate,
        'pm2_5_estimate': pm2_5_estimate,
        'wind_speed': wind_speed,
        'temperature': temperature,
        'source': "api_fusion"
    }