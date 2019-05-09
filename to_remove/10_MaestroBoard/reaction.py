from course import board
import time
import random
import time
b = board.Board()

covered = 0.6

value = 1
while value > covered:
    time.sleep(0.25)
    value = b.get_photo()

delay = random.randrange(10000,20000) / 10000
print(delay)
time.sleep(delay)
b.set_leds(True,True)


# Wait for the light to come on
start_time = time.time()
while value < covered:
    time.sleep(0.01)
    value = b.get_photo()
end_time = time.time()

print('done', end_time - start_time)