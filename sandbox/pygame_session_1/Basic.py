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

x = 20
y = 20

while True:
    game_clock.tick(60)
    main_screen.fill(background_color)
    main_screen.blit(character, (x, y))
    pygame.display.update()
    x = x + 2
    y = y + 2
    if x > screen_size[0]: break

pygame.quit()