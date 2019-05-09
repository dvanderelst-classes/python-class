import pygame
import random
import time
import numpy
from matplotlib import pyplot

pygame.init()
pygame.mixer.init()

screen_size = (750, 750)
error_threshold = 270
max_error_speed = 10
step_size = 5
dpi = 300

my_surface = pygame.display.set_mode(screen_size)
my_clock = pygame.time.Clock()

my_image = pygame.image.load('dieter_t.png')
my_background = pygame.image.load('circle.png')

mixer = pygame.mixer.music.load('blah.flac')
oh_effect = pygame.mixer.Sound('oh.wav')

image_width = my_image.get_width()
image_height = my_image.get_height()

pygame.display.set_caption('Keep your professor in the center of attention')

white = (255, 255, 255)


def sign(x):
    if x < 0: return -1
    if x >= 0: return 1


def place_image(surface, image, x, y):
    width = image.get_width()
    height = image.get_height()
    center_x = x - int(width / 2)
    center_y = y - int(height / 2)
    surface.blit(image, (center_x, center_y))
    return center_x, current_y


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


current_x = screen_size[0] / 2
current_y = screen_size[1] / 2
scale = 1
loop_nr = 0
run_game = True

random_x, random_y = random_motion(scale)
distance_trace = []

start = time.time()
pygame.mixer.music.play(-1)
while run_game:
    my_clock.tick(60)
    my_surface.fill(white)
    place_image(my_surface, my_background, screen_size[0] / 2, screen_size[1] / 2)
    quit_event = len(pygame.event.get(pygame.QUIT))
    # events = pygame.event.get() # Needed for get pressed to work

    if random.random() < 0.05:
        random_x, random_y = random_motion(scale, max_error_speed)
        scale = scale * 1.05

    current_x, current_y = move(current_x, current_y, step_size, random_x, random_y)
    place_image(my_surface, my_image, current_x, current_y)
    distance = ((current_x - screen_size[0] / 2) ** 2 + (current_y - screen_size[1] / 2) ** 2) ** 0.5
    distance_trace.append(distance)
    if distance > error_threshold: run_game = False
    if quit_event: run_game = False

    pygame.display.update()

pygame.mixer.music.stop()
oh_effect.play()
pygame.time.delay(1000)

duration = time.time() - start
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

while True:
    my_clock.tick(60)
    quit_event = len(pygame.event.get(pygame.QUIT))
    if quit_event: break
    events = pygame.event.get()
    pygame.time.delay(250)

pygame.quit()
