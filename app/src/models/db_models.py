from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class HistoricData(models.Model):
    name_data = models.CharField(max_length=255)
    value_data = models.CharField(max_length=255)
    station = models.ForeignKey(Station, related_name='historic_data', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_data} - {self.value_data}"
