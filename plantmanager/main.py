import sys
from data.Plant import *
from service.plantService import PlantService
from repository.plant_storage import PlantStorage


def main():
    try:
        plantService = PlantService()
        plantStorage = PlantStorage()
        plant = plantStorage.getPlantById(4)

        print(plant)
        plantService.waterPlant(plant)
        print(plant)

    except ValueError as ve:
        return str(ve)


if __name__ == "__main__":
    sys.exit(main())
