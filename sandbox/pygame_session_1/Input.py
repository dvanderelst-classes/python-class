# Assignments:
# 1) Alter the game to quit on pressing Q
# 2) Count the number of times the left and the right key were pressed
# 3) Make the background change color on each key press
# 4) Can you make the grunt sound play every time the man CHANGES position?

import pygame

screen_size = (750, 750)
background_color = (200, 200, 200)

pygame.init()
pygame.mixer.init()

pygame.display.set_caption('Exercise Man')

main_screen = pygame.display.set_mode(screen_size)
game_clock = pygame.time.Clock()
left = pygame.image.load('left.png')
right = pygame.image.load('right.png')
mid = pygame.image.load('mid.png')

grunt = pygame.mixer.Sound('grunt.wav')

x = 300
y = 300

while True:
    game_clock.tick(60)
    main_screen.fill(background_color)

    # Get the keys presses
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        main_screen.blit(left, (x, y))
    elif keys[pygame.K_RIGHT]:
        main_screen.blit(right, (x, y))
    else:
        main_screen.blit(mid, (x, y))

    # Update the display
    pygame.display.update()

pygame.quit()

