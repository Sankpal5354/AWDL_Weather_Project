from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Weather API Running Successfully"}

@app.get("/weather/{city}")
def get_weather(city: str):

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    current = data["current_condition"][0]

    return {
        "city": city,
        "temperature": current["temp_C"],
        "humidity": current["humidity"],
        "weather": current["weatherDesc"][0]["value"]
    }