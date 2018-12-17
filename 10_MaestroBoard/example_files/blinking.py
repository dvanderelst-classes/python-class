from course import board
import time
board = board.Board()
for x in range(0,10):
    
    time.sleep(1)
    board.set_servo1(1)
    
    board.set_led1(True)
    time.sleep(1)
    board.set_led2(False)
    board.set_servo1(0)

