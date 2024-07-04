from src.automation import DataScrapingStations

class Main:
    def __init__(self) -> None:
        self.rautomation_stations = DataScrapingStations()

    def start_automation_stations(self):
        return self.rautomation_stations.start()
    

if __name__ == "__main__":
    parser = Main()
    parser.start_automation_stations()