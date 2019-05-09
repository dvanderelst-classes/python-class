import datetime
import math

from course import arm


######################################

def polar2cart(diameter, angle, center_x=0, center_y=0):
    angle = math.radians(angle)
    x = diameter * math.cos(angle) + center_x
    y = diameter * math.sin(angle) + center_y
    return x, y


def hand_coordinates(length, angle, center_x=0, center_y=0):
    start = (center_x, center_y)
    end = polar2cart(length, angle, center_x, center_y)
    return start, end


def min_hand_coordinates(length, minutes, center_x=0, center_y=0):
    angle = min2angle(minutes)
    start = (center_x, center_y)
    end = polar2cart(length, angle, center_x, center_y)
    return start, end


def hour_hand_coordinates(length, hours, minutes, center_x=0, center_y=0):
    angle = hours2angle(hours, minutes)
    start = (center_x, center_y)
    end = polar2cart(length, angle, center_x, center_y)
    return start, end


def min2angle(minutes):
    angle = - 360 * minutes / 60
    return angle


def hours2angle(hours, minutes):
    correction = minutes / 60
    angle = - 360 * (hours + correction) / 12
    return angle


#####################################

height = -7
center_x = 250
diameter = 100

robot = arm.connect()

# draw circle
x, y = polar2cart(diameter, 0, center_x=center_x)
robot.goto(x, y, height + 50, wait=True)

for angle in range(0, 370, 10):
    x, y = polar2cart(diameter, angle, center_x=center_x)
    robot.goto(x, y, height, wait=True)
robot.goto(x, y, height + 50, wait=True)

# get time
now = datetime.datetime.now()
minutes = now.minute
hours = now.hour

# get hand coordinates

start, end = min_hand_coordinates(diameter * 0.9, minutes, center_x=center_x)
robot.goto(start[0], start[1], height + 50, wait=True)
robot.goto(start[0], start[1], height, wait=True)
robot.goto(end[0], end[1], height, wait=True)
robot.goto(end[0], end[1], height + 50, wait=True)

start, end = hour_hand_coordinates(diameter * 0.5, hours, minutes, center_x=center_x)
robot.goto(start[0], start[1], height + 50, wait=True)
robot.goto(start[0], start[1], height, wait=True)
robot.goto(end[0], end[1], height, wait=True)
robot.goto(end[0], end[1], height + 50, wait=True)

robot.disconnect()
