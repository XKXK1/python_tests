import unittest
from data.Plant import *
import datetime
from service.plantService import *


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


if __name__ == '__main__':
    unittest.main()
