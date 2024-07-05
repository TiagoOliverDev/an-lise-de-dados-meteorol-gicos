from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base

class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    historic_data = relationship("HistoricData", back_populates="station")

class HistoricData(Base):
    __tablename__ = "historic_data"

    id = Column(Integer, primary_key=True, index=True)
    name_data = Column(String, nullable=False)
    value_data = Column(Float, nullable=False)
    station_id = Column(Integer, ForeignKey('stations.id'))

    station = relationship("Station", back_populates="historic_data")
