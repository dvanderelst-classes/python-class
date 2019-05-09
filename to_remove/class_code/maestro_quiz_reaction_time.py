import time
from course import board
import random

b = board.Board()

#Wait for finger press
value = b.get_photo()
while value > 0.7:
    time.sleep(0.1)
    value = b.get_photo()
    print(value)
print('finger detected')

# Wait random number of seconds
sleep_time = random.random() * 4 + 3
time.sleep(sleep_time)

# Switch on LEDs
b.set_leds(True, True)

#Wait for finger lift
start = time.time()

value = b.get_photo()
#while value < 0.7:
#    time.sleep(0.05)
#    value = b.get_photo()
#    print(value)
 
while True:
    time.sleep(0.05)
    value = b.get_photo()
    print(value)
    if value > 0.7: break
   
end = time.time()

print(end - start)
print('lift detected')












