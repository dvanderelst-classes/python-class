import sys
import time
import easygui

from course import arm

robot = arm.connect()

robot.set_wrist(0)
robot.goto_polar(200,45, z=100)

robot.goto_polar(200,-45, z=80)
robot.set_wrist(90)

robot.goto(200, 0, 0)
time.sleep(10)
robot.disconnect()