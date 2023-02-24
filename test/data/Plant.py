from dataclasses import dataclass
from enum import Enum
import datetime


class WaterType(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Plant:
    name: str
    waterType: WaterType
    lastWatered: datetime
    needsWater: bool = True
