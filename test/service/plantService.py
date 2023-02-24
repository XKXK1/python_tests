import datetime
from data.Plant import Plant


def waterPlant(plant: Plant):
    plant.lastWatered = datetime.datetime.now()
    plant.needsWater = False
