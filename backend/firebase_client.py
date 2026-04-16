import os
from firebase_admin import credentials, db
from datetime import datetime, timedelta

def init_firebase_app():
    # Load credentials from environment variable FIREBASE_CRED_PATH
    cred_path = os.getenv("FIREBASE_CRED_PATH")
    
    if not cred_path:
        raise ValueError("Environment variable FIREBASE_CRED_PATH is        
not set.")
    
    # Initialize the Firebase Admin SDK with the credentials
    try:
        cred = credentials.Certificate(cred_path)
        db_instance = db.initialize_app(credentials=cred, 
options={"databaseURL": "YOUR_DATABASE_URL"})
        print("Firebase Admin initialized successfully.")
        return db_instance
    except Exception as e:
        print(f"Failed to initialize Firebase Admin: {e}")
        raise

def write_reading(device_id, data: dict):
    try:
        # Get the reference to the device's data in the Realtime
Database
        ref = db.reference().child("readings").child(device_id)
        
        # Write the data dictionary to the database
        ref.set(data)
        print(f"Writing reading for {device_id}...")
        return True
    except Exception as e:
        print(f"Failed to write reading: {e}")
        return False

def read_latest(device_id) -> dict | None:
    try:
        # Get the reference to the device's data in the Realtime
Database
        ref = db.reference().child("readings").child(device_id)
        
        # Query for recent data within the last 10 minutes
        latest_data = 
ref.order_by_child("timestamp").range(datetime.now() - 
timedelta(minutes=10)).limit_to_last(1).get()
        
        if latest_data:
            return list(latest_data.values())[0]
        
        print(f"No reading found in the last 10 minutes for 
{device_id}.")
        return None
    except Exception as e:
        print(f"Failed to read latest data: {e}")
        return None

def read_user_profile(user_id) -> dict | None:
    try:
        # Get the reference to the user's profile in the Realtime
Database
        ref = db.reference().child("users").child(user_id)
        
        # Read the user profile
        user_profile = ref.get()
        
        if user_profile:
            return user_profile

        print(f"No user profile found for {user_id}.")
        return None
    except Exception as e:
        print(f"Failed to read user profile: {e}")
        return None

# Example usage
if __name__ == "__main__":
    db_instance = init_firebase_app()
    
    # Example data and IDs for testing
    device_id = "12345"
    user_id = "user001"
    
    # Write reading
    write_reading(device_id, {"temperature": 22.5, "humidity": 60})
    
    # Read latest reading
    latest_reading = read_latest(device_id)
    print(f"Latest Reading: {latest_reading}")
    
    # Read user profile
    user_profile = read_user_profile(user_id)
    print(f"User Profile: {user_profile}")