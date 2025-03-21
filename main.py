#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, InfraredSensor)
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from time import sleep
from threading import Thread
from motors.Drive import motors as robo
from env import LIMIT,GAIN, DISTANCE_LOWER, DISTANCE_UPPER, LIMIT_OBSTACLE, PORT_MOTOR_LEFT, PORT_MOTOR_RIGHT, PORT_SENSOR_COLOR, PORT_SENSOR_DISTACES, WHEL_DIAMETER, AXEL_TRACK, SPEED, TURN_CORRECTION

eve3 = EV3Brick()

# Inicializa o sensor de Cor.
Sensor_Color = ColorSensor(PORT_SENSOR_COLOR)
# Inicializa o sensor infravermelho
Sensor_Distance = InfraredSensor(PORT_SENSOR_DISTACES)

leftMotor = Motor(PORT_MOTOR_LEFT)
rightMotor = Motor(PORT_MOTOR_RIGHT)

robo = DriveBase(leftMotor, rightMotor, WHEL_DIAMETER, AXEL_TRACK)



isBlack = True
isBeforeBlack = False
signalRotate = 1

def printValue(text: str):
    print(text)
    eve3.screen.clear()
    eve3.screen.draw_text(1, 1, text)

def  desviarObstaculo():
    robo.stop()
    Turn_Rate = (GAIN * 13)
    robo.turn(90)
    robo.drive(SPEED, Turn_Rate)
    wait(1000)


    
    
# Loop para seguir a linha sem ponto de parada.
#isBlack = Curve < 0
#if isBlack and isBeforeBlack != isBlack:
#    signalRotate = -signalRotate
#isBeforeBlack = isBlack
while True:
    # Calcula o desvio do limite.
    Distance = Sensor_Distance.distance()
    # print(Distance)
    
    Light = Sensor_Color.reflection()
    print(Light)
    Curve = Light - LIMIT
    
    

    #if (signalRotate > 0):
    #    GAIN = 10
    #else :
    #    GAIN = 8
    # Calcula a taxa de rotação
    Turn_Rate = GAIN * (Curve* signalRotate)
    # Define a velocidade base e a taxa de rotação baseada nos cálculos anteriores
    robo.drive(SPEED, Turn_Rate)
    # if obstaculo
    #while Distance <= DISTANCE_UPPER and Distance >= DISTANCE_LOWER:
    #    desviarObstaculo()
    #    break
    wait(10)

    if Light > 70:
        robo.stop()
        break