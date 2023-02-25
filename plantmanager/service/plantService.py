import datetime
from data.Plant import Plant


class PlantService:
    def waterPlant(self, plant: Plant):
        plant.lastWatered = datetime.datetime.now()
        plant.needsWater = False
