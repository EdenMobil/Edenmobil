#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from functions.linefollower import LineFollower

# Create your objects here.
ev3 = EV3Brick()

color_sensor = ColorSensor(Port.S3)
ultrasonic_sensor = UltrasonicSensor(Port.S4)

right_motor = Motor(Port.B) 
left_motor = Motor(Port.C)

Drive = DriveBase(right_motor, left_motor, wheel_diameter=56, axle_track=152)

imagefile = ImageFile()
# Write your program here.
# Battery Info
print(ev3.battery.voltage())
print(ev3.battery.current())

Line = LineFollower(Drive, color_sensor, ev3, imagefile)
Line.follow()
