from data.Plant import *
import datetime

plants = [
    Plant(1, "Monstera", WaterType.HIGH, datetime.datetime.now(),  False),
    Plant(2, "Palm Tree", WaterType.MEDIUM,
          datetime.datetime.now(), False),
    Plant(3, "Dracae", WaterType.LOW, datetime.datetime.now(), True),
    Plant(4, "Tree", WaterType.LOW, datetime.datetime.now(), False),
    Plant(5, "Tulip", WaterType.HIGH, datetime.datetime.now(), False)
]


class PlantStorage:

    def getAllPlants(self) -> list[Plant]:
        return self.plants

    def getPlantById(self, id: int) -> Plant:
        '''returns one plant by id'''
        # Using filter() Method
        plant = next(filter(lambda plant: plant.id == id, self.plants))

        if plant is None:
            raise Exception("Date provided can't be in the past")
        return plant

        # List Comprehension
        # filteredPlants = [plant for plant in self.plants if plant.id == id]
