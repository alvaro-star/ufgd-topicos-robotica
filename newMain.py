
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from time import sleep
from threading import Thread
from env import SPEED
from sensors.Color import COLOR_READED, readColor, calculateTurnRate, calculateCurveValue
from sensors.Distance import DISTANCE_READED, readDistance, isDistaneceBetweenLimits
from motors.Drive import motors,runRobot, turnRobot, stopRobot


# threadDitance = Thread(readDistanceThread)
# threadColor = Thread()

isColorBeforeBlack = True
isColorBlack = True
signalRotate = 1

def rodearObstaculo():
    stopRobot()
    Turn_Rate = calculateTurnRate(curve=13)
    turnRobot(90)
    runRobot(Turn_Rate)
    wait(1000)
while True:
    motors.drive(SPEED,1)
    readDistance()
    readColor()
    #print(DISTANCE_READED)
    
    # Calcula a taxa de rotação
    Curve = calculateCurveValue()
    print("Teste ")
    isColorBlack  = COLOR_READED < 0
    if (isColorBlack and isColorBeforeBlack != isColorBlack):
        signalRotate = -signalRotate
    isColorBeforeBlack = isColorBlack
    
    Turn_Rate = calculateTurnRate(curve=Curve*signalRotate)
    runRobot(Turn_Rate)
    # if obstaculo
    while isDistaneceBetweenLimits():
        rodearObstaculo()

    print("Teste 2")
    wait(10)

    if COLOR_READED > 70:
        stopRobot()
        break