import unittest
from data.Plant import *
import datetime
from service.plantService import waterPlant



class plant_manager_test(unittest.TestCase):

    def test_waterPlantTest(self):
        # given
        testPlant = Plant("Monstera", WaterType.MEDIUM,
                          datetime.datetime.now())
        self.assertTrue(testPlant.needsWater)

        # when
        waterPlant(testPlant)

        # then
        self.assertFalse(testPlant.needsWater)


if __name__ == '__main__':
    unittest.main()

