import sys
import time
import easygui

from course import arm

robot = arm.connect()
robot.speed = robot.speed * 1.75

msg = "What do you want to do?"
choices = ["pick up", "stop"]

while True:
    reply = easygui.buttonbox(msg, choices=choices)
    if reply == 'stop': break
    robot.goto(x=200,y=150, z=20)
    robot.goto(z=15)
    robot.set_pump(True)
    time.sleep(3)
    robot.goto(z=150)
    robot.goto(y=-150)
    robot.set_pump(False)
    robot.goto(y=0)

robot.disconnect()