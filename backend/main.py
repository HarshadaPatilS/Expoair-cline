from fastapi import FastAPI, HTTPException, Query, Body, Request
from fastapi.responses import JSONResponse
import json
from typing import List

# Initialize the FastAPI application
app = FastAPI()

# Define Pydantic models for request/response bodies
class ReadingRequest(BaseModel):
    device_id: str
    lat: float
    lon: float
    pm2_5: int
    pm10: int

class AqiResponse(BaseModel):
    aqi: float

class ExposureDoseRequest(BaseModel):
    user_id: str
    lat: float
    lon: float
    activity: str
    duration_minutes: int

# Sample data for AQI calculation (incomplete)
aqi_data = {
    "1": {"pm2_5": 40, "pm10": 80},
    "2": {"pm2_5": 30, "pm10": 60},
    # Add more device readings as needed
}

# Sample data for exposure dose calculation (incomplete)
dose_data = {
    "user1": {"activity": "walking", "duration_minutes": 30},
    # Add more user activities as needed
}

# CORS middleware setup
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route to calculate and return fused AQI
@app.post("/reading")
async def calculate_aqi(request: Request, body: ReadingRequest):
    # Example calculation based on input values
    aqi = (body.pm2_5 + body.pm10) / 2
    response_body = AqiResponse(aqi=aqi)
    return JSONResponse(status_code=200, 
content=json.loads(response_body.json()))

# Route to get fused AQI using input_router
@app.get("/aqi")
async def get_fused_aqi(lat: float, lon: float, device_id: str):
    # Example lookup based on lat/lon and device_id
    if (lat, lon) in aqi_data:
        return JSONResponse(status_code=200, 
content=json.loads(AqiResponse(aqi=aqi_data[(lat, lon)]).json()))
    else:
        raise HTTPException(status_code=404, detail="No AQI data found      
for the given location.")

# Route to calculate and return exposure dose
@app.post("/dose")
async def get_exposure_dose(request: Request, body: 
ExposureDoseRequest):
    # Example calculation based on input values
    activity = body.activity.lower()
    duration_minutes = body.duration_minutes
    dose_factor = 0.5  # Placeholder for actual exposure factor
calculation
    total_dose = dose_factor * duration_minutes
    response_body = {"exposure_dose": total_dose}
    return JSONResponse(status_code=200, 
content=json.dumps(response_body))

# Route to predict 3-hour AQI forecast (incomplete)
@app.get("/predict")
async def get_3_hour_aqi(lat: float, lon: float):
    # Example prediction logic
    forecast_data = {
        "1": {"aqi": 45},
        "2": {"aqi": 50},
    }
    response_body = AqiResponse(aqi=forecast_data.get((lat, lon), 
{"aqi": None})["aqi"])
    return JSONResponse(status_code=200, 
content=json.loads(response_body.json()))

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)