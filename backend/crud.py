from sqlalchemy.orm import Session
from models import WeatherQuery
from datetime import datetime, timezone

def save_weather_to_db(db: Session, location: str, temperature: float, condition: str):
    query = WeatherQuery(
        location=location,
        temperature=temperature,
        condition=condition,
        timestamp=datetime.now(timezone.utc)
    )
    db.add(query)
    db.commit()
    db.refresh(query)
    return query

def get_all_weather_queries(db: Session):
    return db.query(WeatherQuery).order_by(WeatherQuery.timestamp.desc()).all()

def update_weather_query(db: Session, query_id: int, new_location: str):
    query = db.query(WeatherQuery).filter(WeatherQuery.id == query_id).first()
    if query:
        query.location = new_location
        db.commit()
        db.refresh(query)
        return query
    return None

def delete_weather_query(db: Session, query_id: int):
    query = db.query(WeatherQuery).filter(WeatherQuery.id == query_id).first()
    if query:
        db.delete(query)
        db.commit()
        return True
    return False
