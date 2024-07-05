from src.db.database import engine
from src.models.models import Base
from src.automation.data_scraping_stations import DataScrapingStations

def main():
    # Cria todas as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)

    # Inicie o processo de raspagem e inserção de dados
    # scraping = DataScrapingStations()
    # result = scraping.start()
    # print(result)

if __name__ == "__main__":
    main()
