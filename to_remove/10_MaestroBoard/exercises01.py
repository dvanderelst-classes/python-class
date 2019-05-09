import time
from course import board
import time
import random

b = board.Board()

n = 10
lst = []
for x in range(n):
    time.sleep(1)
    value = b.get_photo()
    lst.append(value)
    print(value)


while len(lst) < 10:
    time.sleep(1)
    value = b.get_photo()
    lst.append(value)
    print(value)

##############################################

n = random.randint(1, 21)

nr_guess = 0
while guess != n:
    guess = input('guess:')
    guess = int(guess)
    if guess < n: print('too low')
    if guess > n: print('too high')
    nr_guess = nr_guess + 1
print('correct', nr_guess)


for x in range(3):
    b.set_leds(False,False)
    time.sleep(0.5)
    b.set_leds(True,True)
    time.sleep(0.5)