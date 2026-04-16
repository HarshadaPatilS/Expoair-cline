class ExposureCalculator:
    def __init__(self):
        # Initialize any necessary variables or settings here if 
needed

    def calculate_dose(self, aqi: float, duration_minutes: float,
activity: str) -> float:
        """
        Calculate the exposure dose based on AQI, duration in minutes,      
and activity.

        :param aqi: Air Quality Index (AQI)
        :param duration_minutes: Duration of activity in minutes
        :param activity: Activity level ("resting", "walking", 
"cycling", "running")
        :return: Calculated dose of exposure
        """
        # Define multipliers for different activities
        activity_multipliers = {
            "resting": 0.5,
            "walking": 1.0,
            "cycling": 1.8,
            "running": 2.5
        }

        # Check if the activity is valid
        if activity not in activity_multipliers:
            raise ValueError("Invalid activity type")

        # Calculate the dose using the formula
        multiplier = activity_multipliers[activity]
        dose = aqi * (duration_minutes / 60) * multiplier
        return dose

    def daily_summary(self, readings: list[dict]) -> dict:
        """
        Calculate the total dose for each reading and determine the
average AQI and risk level.

        :param readings: List of dictionaries containing 'aqi' and 
'duration_minutes'
        :return: Dictionary with total_dose, avg_aqi, and risk_level
        """
        total_dose = 0.0
        total_duration_minutes = 0.0

        # Sum up doses from all readings
        for reading in readings:
            aqi = reading.get('aqi', 0)
            duration_minutes = reading.get('duration_minutes', 0)
            total_dose += self.calculate_dose(aqi, duration_minutes,        
'resting')
            total_duration_minutes += duration_minutes

        # Calculate average AQI
        avg_aqi = total_dose / total_duration_minutes if 
total_duration_minutes != 0 else 0.0

        # Determine risk level based on dose thresholds
        risk_level = "low"
        if avg_aqi > 200:
            risk_level = "very_high"
        elif avg_aqi > 100:
            risk_level = "high"
        elif avg_aqi > 50:
            risk_level = "moderate"

        # Return the summary dictionary
        return {
            'total_dose': total_dose,
            'avg_aqi': avg_aqi,
            'risk_level': risk_level
        }