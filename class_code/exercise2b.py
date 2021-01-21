import math
import random

degrees = random.randint(30, 45)
speed = random.randint(5,10)

radians = math.radians(degrees)

g = 10

distance = (speed * speed * math.sin(2 * radians))/g
time = (2 * speed *  math.sin(2 * radians)) / g


print(degrees)
print(speed)  
print(distance) 
print(time) 