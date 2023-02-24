import sys
from data.Plant import *
import datetime 
from service.plantService import *


def main():
    try:
        plant = Plant("Monstera", WaterType.MEDIUM, datetime.datetime.now())
        print(plant)
        waterPlant
        print(plant)
        
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())