import sys
import time
import easygui

# This line adds the course module to the python path.
sys.path.insert(0, '/home/dieter/Dropbox/PythonRepos')

from course import arm

robot = arm.connect()
robot.speed = robot.speed * 1.75

msg = "What do you want to do?"
choices = ["pick up", "stop"]

while True:
    reply = easygui.buttonbox(msg, choices=choices)
    if reply == 'stop': break
    robot.goto(x=100,y=150, z=20, relative=False, wait=True, verbose=True)
    robot.goto(z=10, relative=False, wait=True, verbose=True)
    robot.set_pump(verbose=True)
    time.sleep(3)
    robot.goto(z=150, relative=False, wait=True, verbose=True)
    robot.goto(y=-150, relative=False, wait=True, verbose=True)
    robot.set_pump(status=False, verbose=True)
    robot.goto(y=0, relative=False, wait=True, verbose=True)

robot.disconnect()