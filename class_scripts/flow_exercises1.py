# Ernie's day

weekend = not True
temp = 90

if weekend:
    if temp >= 90:
        print('outside')
    if temp < 90:
        print('bed')
        
else:
    print('work')
    
    
# Rock paper scissors
import random

game = ['rock', 'scissors', 'paper']
playerA = random.choice(game)
playerB = random.choice(game)


winner = 'B'
if playerA == playerB: winner = 'draw'
if playerA == 'paper' and playerB == 'rock': winner = 'playerA'
if playerA == 'scissors' and playerB == 'paper': winner = 'A'
if playerA == 'rock' and playerB == 'scissors': winner = 'A'

#if playerB == 'paper' and playerA == 'rock': winner = 'B'
#if playerB == 'scissors' and playerA == 'paper': winner = 'B'
#if playerB == 'rock' and playerA == 'scissors': winner = 'B'

print(winner)

