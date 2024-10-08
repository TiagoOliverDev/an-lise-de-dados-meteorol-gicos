from sqlalchemy.orm import Session
from ..models.models import Station

class StationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_station(self, name: str, latitude: str, longitude: str):
            existing_station = self.db.query(Station).filter(
                Station.name == name,
                Station.latitude == latitude,
                Station.longitude == longitude
            ).first()
            
            if existing_station:
                print(f"Estação '{name}' já existe no banco de dados.")
                return existing_station

            station = Station(name=name, latitude=latitude, longitude=longitude)
            self.db.add(station)
            self.db.commit()
            self.db.refresh(station)
            return station

    def get_station_by_id(self, station_id: int):
        return self.db.query(Station).filter(Station.id == station_id).first()
    

