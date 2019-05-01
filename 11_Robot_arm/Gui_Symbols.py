import itertools

import numpy
import pygame
from course import arm

 # Get robot and define letters
drawer = arm.RoboticDrawer(speed=10, invert=True)
drawer.height = -10
symbols = drawer.symbol_list
symbols.remove(' ')
print(symbols, len(symbols))
allowable = symbols
extra = ['Back', 'Space', 'Erase', 'Go']
letters = allowable + extra

# Setup screen

background_color = (200, 200, 200)

pygame.init()
pygame.font.init()
main_screen = pygame.display.set_mode((1100,900))
#main_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
info = pygame.display.Info()

screen_w = info.current_w
screen_h = info.current_h


myfont1 = pygame.font.SysFont("monospace", 50)
myfont2 = pygame.font.SysFont("monospace", 75)
game_clock = pygame.time.Clock()

column_locations = numpy.linspace(100, screen_w, 7)  # xs
rows_locations = numpy.linspace(100, screen_h - 500, 7)  # ys

grid_locations = itertools.product(column_locations, rows_locations)
grid_locations = list(grid_locations)

grid_array = numpy.array(grid_locations)

current_string = ''
while True:
    game_clock.tick(60)
    main_screen.fill(background_color)

    for letter, location in zip(letters, grid_locations):
        text_width, text_height = myfont1.size(letter)
        x = location[0] - int(text_width / 2)
        y = location[1] - int(text_height / 2)

        label = myfont1.render(letter, 1, (0, 0, 0))
        main_screen.blit(label, (x, y))

    events = pygame.event.get()

    # proceed events
    clicked_letter = None
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pos = numpy.array(pos)
            distances = numpy.sum((grid_array - pos) ** 2, axis=1)
            index = numpy.argmin(distances)
            if index < len(letters):
                clicked_letter = letters[index]
                print(pos, index, letters[index])

    # process string
    if clicked_letter == 'Quit': break

    if clicked_letter == 'Back':
        current_string = current_string[0:-1]
    if clicked_letter == 'Erase':
        current_string = ''
    if clicked_letter == 'Space':
        current_string = current_string + ' '
    if clicked_letter in allowable:
        current_string = current_string + clicked_letter

    current_string = current_string[0:6]

    if clicked_letter == 'Go':
        drawer.draw_symbols(current_string)
        drawer.robot.go_home()

    # print current string
    text_width, text_height = myfont1.size(current_string)
    x = (screen_w / 2) - int(text_width / 2)
    y = screen_h -300  - int(text_height / 2)

    label = myfont2.render(current_string, 1, (0, 150, 0))
    main_screen.blit(label, (x, y))

    pygame.display.update()

# drawer = arm.RoboticDrawer(speed=10, invert=True)
# drawer.height = 0
#
# print(symbols)

# drawer.draw_symbols('PAC123')
try:
    drawer.disconnect()
except:
    pass