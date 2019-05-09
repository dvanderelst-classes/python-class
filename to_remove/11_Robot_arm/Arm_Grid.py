import itertools

import numpy
from matplotlib import pyplot

from course import arm


###############################################
# DONT TOUCH THIS - UNLESS YOU KNOW WHAT YOUR DOING :)
###############################################

class Drawer:
    def __init__(self):
        self.x_locations = numpy.linspace(150, 250, 10)
        self.y_locations = numpy.linspace(-200, 200, 20)
        self.locations = itertools.product(self.x_locations, self.y_locations)
        self.locations = list(self.locations)
        self.symbols = {
            # /h\
            #   _d_
            # e|   |c
            #   _a_
            # f|   |b
            #   _g_
            # \i/
            #    a,b,c,d,e,f,g,h,i
            " ": [0, 0, 0, 0, 0, 0, 0, 0, 0],

            "0": [0, 1, 1, 1, 1, 1, 1, 0, 0],
            "1": [0, 1, 1, 0, 0, 0, 0, 0, 0],
            "2": [1, 0, 1, 1, 0, 1, 1, 0, 0],
            "3": [1, 1, 1, 1, 0, 0, 1, 0, 0],
            "4": [1, 1, 1, 0, 1, 0, 0, 0, 0],
            "5": [1, 1, 0, 1, 1, 0, 1, 0, 0],
            "6": [1, 1, 0, 1, 1, 1, 1, 0, 0],
            "7": [0, 1, 1, 1, 0, 0, 0, 0, 0],
            "8": [1, 1, 1, 1, 1, 1, 1, 0, 0],
            "9": [1, 1, 1, 1, 1, 0, 1, 0, 0],

            "'": [0, 0, 0, 0, 0, 0, 0, 1, 0],
            ",": [0, 0, 0, 0, 0, 0, 0, 0, 1],

            # hex from https://en.wikipedia.org/wiki/Seven-segment_display#Displaying_letters
            "A": [1, 1, 1, 1, 1, 1, 0, 0, 0],
            "b": [1, 1, 0, 0, 1, 1, 1, 0, 0],
            "C": [0, 0, 0, 1, 1, 1, 1, 0, 0],
            "d": [1, 1, 1, 0, 0, 1, 1, 0, 0],
            "E": [1, 0, 0, 1, 1, 1, 1, 0, 0],
            "F": [1, 0, 0, 1, 1, 1, 0, 0, 0],

            # misc
            "-": [1, 0, 0, 0, 0, 0, 0, 0, 0],
            "_": [0, 0, 0, 0, 0, 0, 1, 0, 0],
            u"‾": [0, 0, 0, 1, 0, 0, 0, 0, 0],  # U+203E OVERLINE
            "=": [1, 0, 0, 0, 0, 0, 1, 0, 0],
            u"≡": [1, 0, 0, 1, 0, 0, 1, 0, 0],  # U+2661 IDENTICAL TO
            "u": [0, 1, 0, 0, 0, 1, 1, 0, 0],
            "o": [1, 1, 0, 0, 0, 1, 1, 0, 0],
            "|": [0, 0, 0, 0, 1, 1, 0, 0, 0],
            "y": [1, 1, 1, 0, 1, 0, 1, 0, 0],
            "P": [1, 0, 1, 1, 1, 1, 0, 0, 0],
            "H": [1, 1, 1, 0, 1, 1, 0, 0, 0],
            "h": [1, 1, 0, 0, 1, 1, 0, 0, 0],
            "r": [1, 0, 0, 0, 0, 1, 0, 0, 0],

            # only for the middle group
            ".": [0, 0, 0, 0, 0, 1, 0, 0, 0],
            ":": [0, 0, 0, 0, 1, 1, 0, 0, 0],
            u"·": [0, 0, 0, 0, 1, 0, 0, 0, 0],
        }

    def plot(self):
        pyplot.figure(figsize=(10, 5))
        n = len(self.locations)
        for i in range(n):
            x = self.locations[i][0]
            y = self.locations[i][1]

            pyplot.text(y, x, str(i))
            pyplot.scatter(y, x)
        pyplot.xlabel('Y')
        pyplot.ylabel('X')
        pyplot.gca().invert_xaxis()
        pyplot.gca().set_aspect('equal', 'box')
        pyplot.title('Top down view from behind the robot')
        pyplot.show()

    def draw_line(self, p1, p2, height, robot):
        position1 = self.locations[p1]
        position2 = self.locations[p2]
        robot.goto(position1[0], position1[1], height + 50, wait=True)
        robot.goto(position1[0], position1[1], height, wait=True)

        robot.goto(position2[0], position2[1], height, wait=True)
        robot.goto(position2[0], position2[1], height + 50, wait=True)

    def draw_line2(self, r1, c1, r2, c2, height, robot):
        p1 = r1 * 20 + c1
        p2 = r2 * 20 + c2
        self.draw_line(p1, p2, height, robot)

    def draw_segments(self, start_column, segments, height, robot):
        sr = 8
        # start_column = 15

        # left two segments F E
        if segments[4]: self.draw_line2(sr, start_column, sr - 3, start_column, height, robot)
        if segments[5]: self.draw_line2(sr - 3, start_column, sr - 6, start_column, height, robot)

        # right two segments B C
        if segments[2]: D.draw_line2(sr, start_column - 2, sr - 3, start_column - 2, height, robot)
        if segments[1]: D.draw_line2(sr - 3, start_column - 2, sr - 6, start_column - 2, height, robot)

        # top D
        if segments[3]: self.draw_line2(sr, start_column, sr, start_column - 2, height, robot)
        # mid A
        if segments[0]: self.draw_line2(sr - 3, start_column, sr - 3, start_column - 2, height, robot)
        #if segments[0]: self.draw_line2(sr - 4, start_column, sr - 4, start_column - 2, height, robot)
        #  bottom G
        if segments[6]: self.draw_line2(sr - 6, start_column, sr - 6, start_column - 2, height, robot)

    def draw_symbol(self, symbol, start_column, height, robot):
        segments = self.symbols[symbol]
        self.draw_segments(start_column, segments, height, robot)


D = Drawer()
D.plot()

###############################################
# TOUCH THIS - EVEN IF YOU DON'T KNOW WHAT YOUR DOING :)
###############################################

##
## Example 1: Drawing shapes
##

height = -5
robot = arm.connect()

# letter H
D.draw_line(179, 39, height, robot)
D.draw_line(99, 97, height, robot)
D.draw_line(97, 37, height, robot)

# letter E
D.draw_line(175, 35, height, robot)

D.draw_line(175, 173, height, robot)
D.draw_line(95, 93, height, robot)
D.draw_line(35, 33, height, robot)

# letter L1
D.draw_line(172, 32, height, robot)
D.draw_line(32, 31, height, robot)

# letter L2
D.draw_line(170, 30, height, robot)
D.draw_line(30, 28, height, robot)

# letter O
D.draw_line(166, 26, height, robot)
D.draw_line(164, 24, height, robot)
D.draw_line(166, 164, height, robot)
D.draw_line(26, 24, height, robot)

robot.disconnect()

##
## Example 2: 7 segment display
##

# height = -5
# robot = arm.connect()
#
# now = datetime.datetime.now()
# minutes = now.minute
# hours = now.hour
#
# hours = str(hours)
# hours = hours.rjust(2, '0')
#
# minutes = str(minutes)
# minutes = minutes.rjust(2, '0')
#
# text = hours + minutes
#
# sc = 19
#
# D.draw_symbol(text[0], sc, height, robot)
# D.draw_symbol(text[1], sc - 3, height, robot)
# D.draw_symbol(text[2], sc - 6, height, robot)
# D.draw_symbol(text[3], sc - 9, height, robot)
#
# robot.disconnect()
