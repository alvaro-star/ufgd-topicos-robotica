
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (ColorSensor)

from env import PORT_SENSOR_COLOR, LIMIT, GAIN
sensorColor = ColorSensor(PORT_SENSOR_COLOR)

COLOR_READED = 0

def readColor():
    COLOR_READED = sensorColor.reflection()
    
def calculateCurveValue():
    return COLOR_READED - LIMIT
def calculateTurnRate(curve):
    if curve is None:
        curve = COLOR_READED - LIMIT
    return GAIN * curve

    