import unittest
from service.plantService import *
from data.Plant import *
import datetime


class plant_manager_test(unittest.TestCase):

    def test_waterPlantTest(self):
        # given
        plantService = PlantService()

        testPlant = Plant(1,"Monstera", WaterType.MEDIUM,
                          datetime.datetime.now())
        self.assertTrue(testPlant.needsWater)

        # when
        plantService.waterPlant(testPlant)

        # then
        self.assertFalse(testPlant.needsWater)
        
    def test_plant_needs_water(self):
        #given
        plantService = PlantService()
        date = datetime.datetime.now() - timedelta(days=10)

        testPlant = Plant(1,"Monstera", WaterType.MEDIUM,
                          date)        
        #when
        needsWater = plantService.plant_needs_water(testPlant)
        
        #then
        self.assertTrue(needsWater)


if __name__ == '__main__':
    unittest.main()
