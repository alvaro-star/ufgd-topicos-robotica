from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor)
from env import PORT_MOTOR_LEFT, PORT_MOTOR_RIGHT, WHEL_DIAMETER, AXEL_TRACK, SPEED, TURN_CORRECTION
leftMotor = Motor(PORT_MOTOR_LEFT)
rightMotor = Motor(PORT_MOTOR_RIGHT)

motors = DriveBase(leftMotor, rightMotor, WHEL_DIAMETER, AXEL_TRACK)



def runRobot(turnRate):
    motors.drive(SPEED, turnRate)
def turnRobot(angle):
    motors.turn(angle * TURN_CORRECTION)
def stopRobot():
    motors.stop()