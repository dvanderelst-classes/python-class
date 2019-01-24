import pygame
import random
import time
import numpy
from matplotlib import pyplot


##########################################################
# I define some functions to be used in the game
##########################################################

def sign(x):
    if x < 0: return -1
    if x >= 0: return 1


def place_image(surface, image, x, y):
    width = image.get_width()
    height = image.get_height()
    center_x = x - int(width / 2)
    center_y = y - int(height / 2)
    surface.blit(image, (center_x, center_y))
    return center_x, center_y


def move(x, y, step=5, random_x=0, random_y=0):
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]: random_y = 0
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]: random_x = 0

    if keys_pressed[pygame.K_UP]: y = y - step
    if keys_pressed[pygame.K_DOWN]: y = y + step
    if keys_pressed[pygame.K_LEFT]: x = x - step
    if keys_pressed[pygame.K_RIGHT]: x = x + step
    x = x + random_x
    y = y + random_y
    return x, y


def random_motion(random_scale=1, max_value=5):
    while True:
        x = random.choice([-1, 0, 1])
        y = random.choice([-1, 0, 1])
        if not x == 0: break
        if not y == 0: break
    x = int(x * random_scale)
    y = int(y * random_scale)
    if abs(x) > max_value: x = max_value * sign(x)
    if abs(y) > max_value: y = max_value * sign(y)
    return x, y


##########################################################
# End of functions
##########################################################

# Settings

screen_size = (750, 750)
error_threshold = 270
max_error_speed = 10
step_size = 5
dpi = 300
scale = 1

# Start the game and sound engines

pygame.init()
pygame.mixer.init()

# Load sounds, background and images

my_surface = pygame.display.set_mode(screen_size)
my_clock = pygame.time.Clock()

my_image = pygame.image.load('dieter_t.png')
my_background = pygame.image.load('circle.png')

mixer = pygame.mixer.music.load('blah.flac')
oh_effect = pygame.mixer.Sound('oh.wav')

# Set the window title

pygame.display.set_caption('Keep your professor in the center of attention')

# Start the music

pygame.mixer.music.play(-1)

# Get the initial position for the image (center of the screen)

x_position = screen_size[0] / 2
y_position = screen_size[1] / 2

# Get the first random motion

random_x, random_y = random_motion(scale)

# Run the game

distance_trace = []
start_time = time.time()
loop_nr = 0
run_game = True
while run_game:
    my_clock.tick(60)
    my_surface.fill((255, 255, 255))

    # Place the background image
    place_image(my_surface, my_background, screen_size[0] / 2, screen_size[1] / 2)
    quit_event = len(pygame.event.get(pygame.QUIT))

    # There is a 5% change on every loop for the game to become slightly more difficult
    if random.random() < 0.05:
        random_x, random_y = random_motion(scale, max_error_speed)
        scale = scale * 1.05

    # Get the new position for my head - note that this function also reads in the key presses
    x_position, y_position = move(x_position, y_position, step_size, random_x, random_y)
    # Place it on the screen
    place_image(my_surface, my_image, x_position, y_position)
    # Calculate and store the error
    distance = ((x_position - screen_size[0] / 2) ** 2 + (y_position - screen_size[1] / 2) ** 2) ** 0.5
    distance_trace.append(distance)
    # If the error is too large, end the game
    if distance > error_threshold: run_game = False
    if quit_event: run_game = False
    # Update the display
    pygame.display.update()

# Stop the background music
pygame.mixer.music.stop()
# Play a sound effect
oh_effect.play()
# Wait 1 second
pygame.time.delay(1000)

##########################################################
# The code below plots the error as a function of time and shows the image in the game screen
##########################################################

duration = time.time() - start_time
score_line = 1 - (numpy.array(distance_trace) / error_threshold)
time_line = numpy.linspace(0, duration, len(distance_trace))

score = int(numpy.sum(score_line))

pyplot.figure(figsize=(screen_size[0] / dpi, screen_size[1] / dpi), dpi=dpi)
pyplot.plot(time_line, score_line)
pyplot.title('Your score is ' + str(score))
pyplot.ylabel('Accuracy')
pyplot.xlabel('Time')
pyplot.tight_layout()
pyplot.savefig('plot.png', dpi=dpi)

my_plot = pygame.image.load('plot.png')
place_image(my_surface, my_plot, screen_size[0] / 2, screen_size[1] / 2)
pygame.display.update()

##########################################################
# Wait for the player to close the game
##########################################################

while True:
    my_clock.tick(60)
    quit_event = len(pygame.event.get(pygame.QUIT))
    if quit_event: break
    events = pygame.event.get()
    pygame.time.delay(250)

pygame.quit()
