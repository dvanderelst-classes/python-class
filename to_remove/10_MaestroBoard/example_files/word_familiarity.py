import random
from course import board
import time
from matplotlib import pyplot


def calibrate(board):
    board.set_leds(True, False)
    counter = 0
    while 1:
        pot = board.get_pot()
        if pot > 0.45 and pot < 0.55: break
        if counter == 0: print('Please move the dial to center')
        counter += 1
        time.sleep(0.25)
    board.set_leds(False, True)


def get_response(board):
    base = 1
    print('Use the dial to rate the word. Touch the photocell to submit your response.')
    while 1:
        photo = board.get_photo()
        pot = board.get_pot()
        board.set_servo1(pot)
        if base - photo > 0.1: break
        time.sleep(0.1)
    board.set_servo1(0.5)
    return pot


low = ['thine', 'dale', 'kith', 'gall', 'gloaming']
high = ['house', 'boy', 'thief', 'evening', 'you']
words = low + high
responses = []
random.shuffle(words)

board = board.Board()

board.set_leds(False, False)
for x in words:
    calibrate(board)
    print('How familar is the word', x)
    response = get_response(board)
    responses.append(response)
    time.sleep(1)

pyplot.barh(range(0, 10), responses)
pyplot.yticks(range(0, 10), words)
pyplot.savefig('familiarity.png')
pyplot.show()
