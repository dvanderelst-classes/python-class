
import time
from course import board
from matplotlib import pyplot

b = board.Board()

all_values = []
for x in range(10):
  value = b.get_photo()
  print(value)
  all_values.append(value)
  time.sleep(1)


pyplot.plot(all_values)
pyplot.show()
