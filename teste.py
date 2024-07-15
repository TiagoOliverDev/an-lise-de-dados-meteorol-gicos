from app.src.automation import DataScrapingStations

class Main:
    def __init__(self) -> None:
        self.rautomation_stations = DataScrapingStations()

    def start_automation_stations(self):
        init = self.rautomation_stations.start()
        print(init)
        print("*********************************")
        # print(init['historical_data'])
        return init
    

if __name__ == "__main__":
    parser = Main()
    parser.start_automation_stations()