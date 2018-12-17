import random

items = ['R','S','P']
win1 = 0
win2 = 0

while (win1 < 3) and (win2 < 3):
    P1 = random.choice(items)
    P2 = random.choice(items)

 

    winner = '1'
    if P1 == P2: winner = 'draw'
    if P1 == 'R' and P2 == 'S': winner = '2'
    if P1 == 'P' and P2 == 'R': winner = '2'
    if P1 == 'S' and P2 == 'P': winner = '2'

    if winner == '1': win1 = win1 + 1
    if winner == '2': win2 = win2 + 1

print('winner :', winner)
print('score 1:', win1)
print('score 2:', win2)


for a in range(1,11):
    result = a * b
    print(a, 'X', b, '=', result)


word = 'pineapple pineapple pineapple y'
vowels = ['a', 'e', 'u', 'o', 'y', 'i']
for letter in word:
    if letter in vowels:
        print(letter, 'is a vowel')
    else:
        if letter == ' ':
            print('hey this is a space')
        if letter != ' ':
            print(letter, 'is a consonant')
