# main.py -- put your code here!

import random
import lcd160cr
import utime
import math

def prepare_screen():
    lcd = lcd160cr.LCD160CR('X')
    lcd.set_orient(lcd160cr.PORTRAIT)
    lcd.set_pos(0, 0)
    lcd.set_text_color(lcd.rgb(255, 0, 0), lcd.rgb(0, 0, 0))
    lcd.set_font(2)
    lcd.write('Hello MicroPython!')
    return lcd

def reset_screen(screen):
    screen.erase()
    screen.set_pos(0, 0)

def lcd_print(txt,screen):
    txt = str(txt) + '\n\r'
    screen.write(txt)

def button(x,y, txt, screen):
    w = 30
    h = 30
    dx = int(w/2)
    dy = int(h/2)
    x = x - dx
    y = y - dy
    screen.rect(x,y, h, w)
    screen.set_pos(x,y)
    screen.write(txt)

lcd = prepare_screen()

my_score = 0
your_score = 0

while True:
    choices = ['r','p','s']
    computer_choice = random.choice(choices)
    
    reset_screen(lcd)
    lcd_print('Choose a weapon!', lcd)
    button(16,130, 'R', lcd)
    button(64,130, 'P', lcd)
    button(112,130, 'S', lcd)
    
    while not lcd.is_touched(): utime.sleep(0.1)
    while lcd.is_touched(): utime.sleep(0.1)
    reset_screen(lcd)
    lcd_print('I choose', lcd)
    if computer_choice == 'r': lcd_print('rock', lcd)
    if computer_choice == 'p': lcd_print('paper', lcd)
    if computer_choice == 's': lcd_print('scissors', lcd)
    
    # Get user input
    touch = lcd.get_touch()
    d_r = math.fabs(touch[1] -  16)
    d_p = math.fabs(touch[1] -  64)
    d_s = math.fabs(touch[1] -  112)
    
    values = [d_r, d_p, d_s]
    min_value = min(values)
    index = values.index(min_value)
    user_choice = choices[index]
    
    lcd_print(' ', lcd)
    lcd_print('You choose', lcd)
    if user_choice == 'r': lcd_print('rock', lcd)
    if user_choice == 'p': lcd_print('paper', lcd)
    if user_choice == 's': lcd_print('scissors', lcd)
    
    #determine winner
    winner = 'tie'
    if user_choice == 'r' and computer_choice == 's': winner = 'user'
    if user_choice == 'p' and computer_choice == 'r': winner = 'user'
    if user_choice == 's' and computer_choice == 'p': winner = 'user'
    
    
    if user_choice == 'r' and computer_choice == 'p': winner = 'cmp'
    if user_choice == 'p' and computer_choice == 's': winner = 'cmp'
    if user_choice == 's' and computer_choice == 'r': winner = 'cmp'
    
    lcd_print(' ', lcd)
    if winner == 'tie': lcd_print('Tie', lcd)
    if winner == 'user': 
        lcd_print('You win!', lcd)
        your_score+=1
    if winner == 'cmp':
        lcd_print('I win!', lcd)
        my_score+=1
        
    score_board = 'Scores: ' + str(your_score) + '/' + str(my_score)
    lcd_print(score_board, lcd)
    
    utime.sleep(1)
    while not lcd.is_touched(): utime.sleep(0.1)
    while lcd.is_touched(): utime.sleep(0.1)
    
    

