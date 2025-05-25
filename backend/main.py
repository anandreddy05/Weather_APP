from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, get_db, engine
import crud
import requests
import os
from dotenv import load_dotenv

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/weather/live/{location}")
def get_live_weather(location: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Location not found")

    data = response.json()
    return {
        "location": data["name"],
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }


@app.post("/weather/save/{location}")
def save_weather(location: str, db: Session = Depends(get_db)):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Location not found")

    data = response.json()
    return crud.save_weather_to_db(db, location, data["main"]["temp"], data["weather"][0]["description"])


@app.get("/weather/history/")
def get_weather_history(db: Session = Depends(get_db)):
    return crud.get_all_weather_queries(db)


@app.put("/weather/update/{query_id}")
def update_weather(query_id: int, new_location: str, db: Session = Depends(get_db)):
    return crud.update_weather_query(db, query_id, new_location)


@app.delete("/weather/delete/{query_id}")
def delete_weather(query_id: int, db: Session = Depends(get_db)):
    return crud.delete_weather_query(db, query_id)


@app.get("/weather/forecast/{location}")
def get_5_day_forecast(location: str):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Location not found")

    data = response.json()
    daily_summary = {}

    for entry in data["list"]:
        date = entry["dt_txt"].split(" ")[0]
        temp = entry["main"]["temp"]
        condition = entry["weather"][0]["description"]
        if date not in daily_summary:
            daily_summary[date] = {"temps": [], "conditions": []}
        daily_summary[date]["temps"].append(temp)
        daily_summary[date]["conditions"].append(condition)

    forecast = []
    for date, details in daily_summary.items():
        avg_temp = sum(details["temps"]) / len(details["temps"])
        common_condition = max(set(details["conditions"]), key=details["conditions"].count)
        forecast.append({
            "date": date,
            "avg_temp": round(avg_temp, 1),
            "common_condition": common_condition
        })

    return forecast
