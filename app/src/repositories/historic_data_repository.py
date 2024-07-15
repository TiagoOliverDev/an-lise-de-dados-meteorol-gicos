from sqlalchemy.orm import Session
from ..models.models import HistoricData

class HistoricDataRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_historic_data(self, name_data: str, value_data: str, station_id: int) -> HistoricData:
        if name_data == 'DataHora (GMT)':
            existing_data = self.db.query(HistoricData).filter(
                HistoricData.name_data == name_data,
                HistoricData.value_data == value_data,
                HistoricData.station_id == station_id
            ).first()

            if existing_data:
                print(f"Dados históricos já existem no banco de dados para station_id '{station_id}' com DataHora '{value_data}'.")
                return existing_data

        historic_data = HistoricData(name_data=name_data, value_data=value_data, station_id=station_id)
        self.db.add(historic_data)
        self.db.commit()
        self.db.refresh(historic_data)
        return historic_data

    def get_historic_data_by_id(self, data_id: int):
        return self.db.query(HistoricData).filter(HistoricData.id == data_id).first()

