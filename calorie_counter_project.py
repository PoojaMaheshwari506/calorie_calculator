import os
from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv

load_dotenv()  # .env file load karega

API_KEY = os.getenv("ROBOFLOW_API_KEY")

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=API_KEY
)

IMAGE_PATH = input("Enter the path of your image:").strip()

if not os.path.exists(IMAGE_PATH):
    print(f"Error: Image file '{IMAGE_PATH}' not found.")
    exit(1)


# Model ID 
MODEL_ID = "indian_food-6hxeg-cwy0e/1"

# Calories per item (aap apne hisaab se aur bhi add kar sakte ho)
calorie_db = {
    "curd": 60,
    "daal": 120,
    "rice": 130,
    "roti": 80,
    "salad": 30,
    "sweet": 150,
    "biryani": 200,
    "chutney": 30,
    "dry-curry": 100,
    "idli": 60,
    "poori": 70,
    "sambhar": 80,
    "vada": 100,
    "wet-curry": 120
}

# Inference (food detection)
result = CLIENT.infer(IMAGE_PATH, model_id=MODEL_ID)

# Count detected items
detected = {}
for pred in result['predictions']:
    label = pred['class'].lower()
    detected[label] = detected.get(label, 0) + 1  #count increase

print("\nDetected Items and Calories:")
total_cal = 0
for food, count in detected.items():
    cal = calorie_db.get(food, 0) * count
    total_cal += cal
    print(f"{food.title()}: {count} x {calorie_db.get(food, 0)} kcal = {cal} kcal")

print(f"\nTotal Estimated Calories: {total_cal} kcal")
