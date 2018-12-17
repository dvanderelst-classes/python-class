import pygame
from course import board


def get_image(file_name, position):
    # x, y, width, height
    x = position[0]
    y = position[1]
    width = position[2]
    height = position[3]
    sprite_sheet = pygame.image.load(file_name)
    sprite_sheet = sprite_sheet.convert()
    image = pygame.Surface([width, height]).convert()
    # Copy the sprite from the large sheet onto the smaller image
    image.blit(sprite_sheet, (0, 0), (x, y, width, height))
    image.set_colorkey([0, 0, 0])
    return image


offset_x = 32
offset_y1 = 3
offset_y2 = 6

screen_size = (300 - offset_x, 220 - offset_y2)
background_color = (255, 255, 255)

pygame.init()
pygame.mixer.init()

pygame.display.set_caption('Sun monitor')

main_screen = pygame.display.set_mode(screen_size)
game_clock = pygame.time.Clock()

level5 = [000, 000, 300, 220]
level6 = [300 + offset_x, 000, 300, 220]
level3 = [000, 220 + offset_y1, 300, 220]
level4 = [300 + offset_x, 220 + offset_y1, 300, 220]
level1 = [000, 440 + offset_y2, 300, 220]
level2 = [300 + offset_x, 440 + offset_y2, 300, 220]

my_board = board.Board()

while True:
    game_clock.tick(60)
    pygame.event.get()
    pressed = pygame.key.get_pressed()

    current_image = get_image('gauge.jpg', level1)
    value = my_board.get_photo()
    value = int(value * 5) + 1

    if value == 2: current_image = get_image('gauge.jpg', level2)
    if value == 3: current_image = get_image('gauge.jpg', level3)
    if value == 4: current_image = get_image('gauge.jpg', level4)
    if value == 5: current_image = get_image('gauge.jpg', level5)
    if value == 6: current_image = get_image('gauge.jpg', level6)

    # if pressed[pygame.K_2]: current_image = get_image('gauge.jpg', level2)
    # if pressed[pygame.K_3]: current_image = get_image('gauge.jpg', level3)
    # if pressed[pygame.K_4]: current_image = get_image('gauge.jpg', level4)
    # if pressed[pygame.K_5]: current_image = get_image('gauge.jpg', level5)
    # if pressed[pygame.K_6]: current_image = get_image('gauge.jpg', level6)

    if pressed[pygame.K_q]: break
    main_screen.fill(background_color)
    main_screen.blit(current_image, (0, 0))
    pygame.display.update()

pygame.quit()
