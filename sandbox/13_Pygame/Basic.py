import pygame

# Assignments:
# Make the pig go faster/slower
# Make the pig start at another corner
# Make the pig bounce back on reaching a corner

screen_size = (750, 750)
background_color = (127, 115, 88)

pygame.init()

main_screen = pygame.display.set_mode(screen_size)
game_clock = pygame.time.Clock()
character = pygame.image.load('pig.png')

x = 1
y = 1

delta_x = 3
delta_y = 3

while True:
    game_clock.tick(60)
    main_screen.fill(background_color)
    main_screen.blit(character, (x, y))
    pygame.display.update()
    
    if x > 730 or x < 0:
        delta_x = - delta_x
        delta_y = - delta_y
    
    x = x + delta_x
    y = y + delta_y


    #if x > screen_size[0]: break

pygame.quit()