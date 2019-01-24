import pygame
import math
import random
import time


# Assignments
# 1) Make the program wait until a button is pressed. Then begin the experiment.
# 2) Let the fixation point disappear before showing the stimulus
# 3) After each trial, show the reaction time (in milliseconds) on the screen
# 4) Have the script ask for a subject number before starting (at the command line)
# 5) Log the output to a file, also log the subject number


def polar2rectangular(r, a, screen_w, screen_h, pict_w):
    rad = math.radians(a)
    x = r * math.cos(rad) + int(screen_w / 2.0) - int(pict_w / 2.0)
    y = r * math.sin(rad) + int(screen_h / 2.0) - int(pict_w / 2.0)
    return x, y


def clear_keys():
    while True:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_SPACE]: break
        pygame.time.wait(10)


def wait_for_key(key):
    start = time.time()
    while 1:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[key]: break
        pygame.time.wait(1)
    end = time.time()
    reaction_time = end - start
    return reaction_time


width = 1500
height = 750
stim_size = 50

screen_size = (width, height)

pygame.init()

main_screen = pygame.display.set_mode(screen_size)
game_clock = pygame.time.Clock()

background_image = pygame.image.load('serengeti_cut.jpg')

black = pygame.color.Color(0, 0, 0, 0)

angles = [0, 120, 240]
distances = [200, 300]
stimuli = [1, 2, 3, 4, 5]
repeats = 2
rate = 60

# Make trial list

trials = []
for a in angles:
    for d in distances:
        for s in stimuli:
            trials.append([a, d, s])

trials = trials * repeats
random.shuffle(trials)

# The the experiment

for trial in trials:
    game_clock.tick(rate)

    # Show background
    main_screen.blit(background_image, [0, 0])
    pygame.draw.circle(main_screen, black, (int(width / 2), int(height / 2)), 25)
    pygame.display.update()

    # Load stimulus
    angle = trial[0]
    distance = trial[1]
    image = 'skin%s.jpg' % trial[2]
    skin = pygame.image.load(image)
    skin = pygame.transform.scale(skin, (stim_size, stim_size))

    # Wait random time
    wait_time = random.randrange(1500, 2500)
    pygame.time.wait(wait_time)

    # Get all pending key presses
    clear_keys()

    # Show stimulus
    x, y = polar2rectangular(distance, angle, width, height, stim_size)
    main_screen.blit(skin, (x, y))
    pygame.display.update()

    # Wait response
    response_time = wait_for_key(pygame.K_SPACE)
    print(angle, distance, image, response_time)

pygame.quit()



