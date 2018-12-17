from course import board
import time


# Connect to the board
my_board = board.Board()
# my_board is now a variable referring to the board attached to your computer

# Read the value of the photosensor (between 0 and 1)
value = my_board.get_photo()
print('The light level is', value)

# Read the position of the dial (between 0 and 1)
value = my_board.get_pot()
print('The dial position is', value)

# Switch LED1 on/off
for x in range(5):
    my_board.set_led1(True)
    time.sleep(0.5)
    my_board.set_led1(False)
    time.sleep(0.5)

# Switch LED2 on/off
for x in range(5):
    my_board.set_led2(True)
    time.sleep(0.5)
    my_board.set_led2(False)
    time.sleep(0.5)

# Set the motor positions
positions = [0, 0.25, 0.75, 1]
for p in positions:
    my_board.set_servo1(p)
    my_board.set_servo2(p)
    time.sleep(0.5)