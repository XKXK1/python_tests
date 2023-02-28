from datetime import datetime, timedelta
from data.Plant import *

WATER_TYPE_LOW_DAY_LIMIT = 1
WATER_TYPE_MID_DAY_LIMIT = 2
WATER_TYPE_HIGH_DAY_LIMIT = 3

class PlantService:
    def waterPlant(self, plant: Plant):
        plant.lastWatered = datetime.datetime.now()
        plant.needsWater = False
    
    def plant_needs_water(self, plant: Plant): 
        time = datetime.datetime.now()
        match plant.waterType:
            case WaterType.MEDIUM:
                return plant.lastWatered < time - timedelta(days=WATER_TYPE_LOW_DAY_LIMIT)
            case WaterType.MEDIUM:
                return plant.lastWatered < time - timedelta(days=WATER_TYPE_MID_DAY_LIMIT)
            case WaterType.HIGH:
                return plant.lastWatered < time - timedelta(days=WATER_TYPE_HIGH_DAY_LIMIT)
            case default:
                return "something"
