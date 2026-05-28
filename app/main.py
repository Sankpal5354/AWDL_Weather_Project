from fastapi import FastAPI
import requests
import mysql.connector

app = FastAPI()

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="student",
    database="weather_project"
)

cursor = db.cursor()

@app.get("/")
def home():
    return {"message": "Weather API Running Successfully"}

@app.get("/weather/{city}")
def get_weather(city: str):

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    current = data["current_condition"][0]

    temperature = current["temp_C"]
    humidity = current["humidity"]
    weather = current["weatherDesc"][0]["value"]

    # Insert into MySQL
    query = """
    INSERT INTO weather_history
    (city, temperature, humidity, weather)
    VALUES (%s, %s, %s, %s)
    """

    values = (city, temperature, humidity, weather)

    cursor.execute(query, values)

    db.commit()

    return {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "weather": weather
    }


@app.get("/history")
def history():

    cursor.execute("SELECT * FROM weather_history")

    rows = cursor.fetchall()

    return {"history": rows}