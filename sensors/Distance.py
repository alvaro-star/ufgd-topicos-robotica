from pybricks.ev3devices import (InfraredSensor)
from env import PORT_SENSOR_DISTACES, DISTANCE_LOWER, DISTANCE_UPPER

sensorDistance = InfraredSensor(PORT_SENSOR_DISTACES)

DISTANCE_READED = 0
def readDistance():
    DISTANCE_READED = sensorDistance.distance()

def isDistaneceBetweenLimits():
    return DISTANCE_LOWER <= DISTANCE_READED <= DISTANCE_UPPER