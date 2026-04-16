class HealthScorer:
    def __init__(self, user_profile: dict):
        """
        Initialize the HealthScorer with user profile.

        :param user_profile: Dictionary containing user profile data
        :type user_profile: dict
        """
        self.user_profile = user_profile

    def score(self, aqi: float) -> dict:
        """
        Calculate the health score based on the AQI and user profile.

        :param aqi: Air Quality Index (AQI)
        :return: Dictionary with calculated scores
        """
        # Initialize base score
        personal_score = aqi

        # Apply multipliers based on user profile
        if self.user_profile['has_asthma']:
            personal_score *= 1.5
        if self.user_profile['age'] > 60:
            personal_score *= 1.3
        if self.user_profile['is_pregnant']:
            personal_score *= 1.4
        if self.user_profile['has_heart_condition']:
            personal_score *= 1.6

        # Calculate risk level based on the personal score
        risk_level = "safe"
        if personal_score >= 300:
            risk_level = "avoid"
        elif personal_score >= 200:
            risk_level = "caution"

        # Prepare the result dictionary
        result = {
            'raw_aqi': aqi,
            'personal_score': personal_score,
            'risk_level': risk_level,
            'recommendation': self.get_recommendation(risk_level)
        }

        return result

    def get_recommendation(self, risk_level: str) -> str:
        """
        Determine recommendation based on the risk level.

        :param risk_level: Risk level ("safe", "caution", "avoid")
        :return: Recommendation message
        """
        if risk_level == "safe":
            return "Your exposure to air quality is within safe 
limits."
        elif risk_level == "caution":
            return "Consider reducing your exposure or staying indoors      
during high AQI periods."
        else:
            return "Take extra precautions, including avoiding outdoor      
activities and staying inside."

# Example usage:
if __name__ == "__main__":
    # Simulate user profile and AQI (replace with actual data)
    user_profile = {
        'age': 45,
        'has_asthma': False,
        'is_pregnant': True,
        'has_heart_condition': False
    }
    aqi_value = 250

    try:
        scorer = HealthScorer(user_profile)
        score_result = scorer.score(aqi_value)
        print("Health Score:", score_result)
    except ValueError as e:
        print(e)